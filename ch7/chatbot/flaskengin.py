from flask import Flask, request, jsonify, Response
from customscripts import conversationengine as cs
from flask_cors import CORS
import json
import os, uuid
from datetime import datetime
from pytz import timezone
from flask_pymongo import PyMongo

app = Flask(__name__)

# Mongo connection
app.config['MONGO_DBNAME'] = 'chatbot_user_data'
# app.config['']=''
# app.config['']=''
mongo = PyMongo(app)

# cross domain request & response handler
CORS(app)

# Seesion key generator id
app.secret_key = os.urandom(10)

# Post data  dict
post_data_lead_create = {}

# Conversation list variable
conversation_list_history = []
request_user_id = str(uuid.uuid4())
fmt = "%Y-%m-%d %H:%M:%S %Z%z"
now_utc = datetime.now(timezone('UTC'))
now_india = now_utc.astimezone(timezone('Asia/Kolkata'))
now_india_time = now_india.strftime(fmt)


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }

    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.errorhandler(500)
def internalservererror(error=None):
    message = {
        'status': 500,
        'message': 'Unexpected server error or Internal Server Error',
    }
    resp = jsonify(message)
    resp.status_code = 500

    return resp


@app.errorhandler(502)
def gatewaytimeout(error=None):
    message = {
        'status': 502,
        'message': 'Gateway time out error',
    }
    resp = jsonify(message)
    resp.status_code = 502

    return resp


@app.errorhandler(400)
def Badrequest(error=None):
    message = {
        'status': 400,
        'message': 'Bad request',
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp


@app.route('/')
def hello_world():
    return 'Hello from chat bot Flask...!'


@app.route("/welcomemsg_chat")
def welcomemsg_chat():
    welcome_msg = cs.loan_assistant_welcome_msg()
    conversation_list_history.append(welcome_msg)
    # db_handler = mongo.db.chathistory
    # db_handler.insert({"request_user_id": request_user_id, "conversation": conversation_list_history,
    #                    "time": now_india.strftime(fmt)})
    # db_handler.update({"request_user_id": request_user_id}, {
    #     '$set': {"request_user_id": request_user_id, "conversation": conversation_list_history, "time": now_india.strftime(fmt)},
    #     "$currentDate": {"lastModified": True}}, upsert=True)
    resp = Response(welcome_msg, status=200, mimetype='application/json')
    return resp


@app.route('/hi_chat', methods=['GET', 'POST'])
def start_coversation():
    if ('msg' in request.args):
        text = request.args['msg']
        start_conv_msg = cs.start_converation_action(text)
        conversation_list_history.append(start_conv_msg)
        # db_handler = mongo.db.chathistory
        # db_handler.insert({"request_user_id": request_user_id, "conversation": conversation_list_history,
        #                    "time": now_india.strftime(fmt)})
        # db_handler.update({"request_user_id": request_user_id}, {
        #     '$set': {"request_user_id": request_user_id, "conversation": conversation_list_history, "time": now_india.strftime(fmt)},
        resp = Response(start_conv_msg, status=200, mimetype='application/json')
        return resp


@app.route('/asking_borowers_full_name', methods=['GET', 'POST'])
def asking_borowers_full_name():
    if ('msg' in request.args):
        borrowers_name_asking_msg = request.args['msg']
        post_data_lead_create.update({"name": borrowers_name_asking_msg})
        borrowers_name_asking_msg_status = cs.borrowers_name_asking(borrowers_name_asking_msg)
        conversation_list_history.append(borrowers_name_asking_msg_status)
        # db_handler = mongo.db.chathistory
        # db_handler.insert({"request_user_id": request_user_id, "conversation": conversation_list_history,
        #                    "time": now_india.strftime(fmt)})
        # db_handler.update({"request_user_id": request_user_id}, {
        #     '$set': {"request_user_id": request_user_id, "conversation": conversation_list_history, "time": now_india.strftime(fmt)},
        #     "$currentDate": {"lastModified": True}}, upsert=True)
        #print post_data_lead_create
        resp = Response(borrowers_name_asking_msg_status, status=200, mimetype='application/json')
        return resp


@app.route('/asking_borowers_email_id')
def asking_borowers_email_id():
    if ('msg' in request.args):
        borrowers_emailid_asking_msg = request.args['msg']
        post_data_lead_create.update({"email": borrowers_emailid_asking_msg.lower()})
        borrowers_emailid_asking_msg_status = cs.borrowers_email_id_asking(borrowers_emailid_asking_msg)
        conversation_list_history.append(borrowers_emailid_asking_msg_status)
        # db_handler = mongo.db.chathistory
        # db_handler.insert({"request_user_id": request_user_id, "conversation": conversation_list_history,
        #                    "time": now_india.strftime(fmt)})
        # db_handler.update({"request_user_id": request_user_id}, {
        #     '$set': {"request_user_id": request_user_id, "conversation": conversation_list_history, "time": now_india.strftime(fmt)},
        #     "$currentDate": {"lastModified": True}}, upsert=True)
        #print post_data_lead_create
        resp = Response(borrowers_emailid_asking_msg_status, status=200, mimetype='application/json')
        return resp


@app.route('/mobilenumber_asking', methods=['GET', 'POST'])
def mobilenumber_asking():
    if ('msg' in request.args):
        mobilenumber_asking_msg = request.args['msg']
        post_data_lead_create.update({"phone": mobilenumber_asking_msg})
        mobilenumber_asking_status = cs.mobilenumber_asking(mobilenumber_asking_msg)
        generatedotpsys = json.loads(mobilenumber_asking_status)
        db_handler = mongo.db.chathistory
        try:
            generatedotpbysys = generatedotpsys['OTP']
            conversation_list_history.append(mobilenumber_asking_status, generatedotpbysys)
            # db_handler.insert({"request_user_id": request_user_id, "conversation": conversation_list_history,
            #                    "time": now_india.strftime(fmt)})
            # db_handler.update({"request_user_id": request_user_id}, {
            #     '$set': {"request_user_id": request_user_id, "conversation": conversation_list_history, "time": now_india.strftime(fmt)},
            #     "$currentDate": {"lastModified": True}}, upsert=True)
        except Exception:
            conversation_list_history.append(mobilenumber_asking_status)
            # db_handler.insert({"request_user_id": request_user_id, "conversation": conversation_list_history,
            #                    "time": now_india.strftime(fmt)})
            # db_handler.update({"request_user_id": request_user_id}, {
            #     '$set': {"request_user_id": request_user_id, "conversation": conversation_list_history, "time": now_india.strftime(fmt)},
            #     "$currentDate": {"lastModified": True}}, upsert=True)
            # resstr = mobilenumber_asking_status ,generatedotpbysys
        #print post_data_lead_create
        resp = Response(mobilenumber_asking_status, status=200, mimetype='application/json')
        return resp


@app.route('/loan_chat', methods=['GET', 'POST'])
def loan_ammount_asking_coversation():
    if ('msg' in request.args):
        loan = request.args['msg']
        post_data_lead_create.update({"loanAmount": loan})
        loan_conv_msg = cs.loan_ammount_asking(loan)
        conversation_list_history.append(loan_conv_msg)
        # db_handler = mongo.db.chathistory
        # db_handler.insert({"request_user_id": request_user_id, "conversation": conversation_list_history,
        #                    "time": now_india.strftime(fmt)})
        # db_handler.update({"request_user_id": request_user_id}, {
        #     '$set': {"request_user_id": request_user_id, "conversation": conversation_list_history, "time": now_india.strftime(fmt)},
        #     "$currentDate": {"lastModified": True}}, upsert=True)
        print post_data_lead_create
        resp = Response(loan_conv_msg, status=200, mimetype='application/json')
        return resp


@app.route('/end_chat', methods=['GET', 'POST'])
def user_bye_str():
    if ('msg' in request.args):
        user_bye_str_msg = request.args['msg']
        user_bye_str_msg_status = cs.user_bye_str(user_bye_str_msg)
        conversation_list_history.append(user_bye_str_msg_status)
        db_handler = mongo.db.chathistory
        db_handler.insert({"request_user_id": request_user_id, "conversation": conversation_list_history,
                           "time": now_india.strftime(fmt)})
        # db_handler.update({"request_user_id": request_user_id}, {
        #     '$set': {"request_user_id": request_user_id, "conversation": conversation_list_history, "time": now_india.strftime(fmt)},
        #     "$currentDate": {"lastModified": True}}, upsert=True)
        resp = Response(user_bye_str_msg_status, status=200, mimetype='application/json')
        return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, threaded=True, debug=True)
