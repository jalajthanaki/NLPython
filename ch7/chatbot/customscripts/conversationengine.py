import random
import json
import sys, time, re
from bson import json_util
from num2words import num2words
import requests, ast

# Welcome msg
assistant_defualt_welcome_msg = [
    "Hi, I'm personal loan application assistant.",
    "You can apply for loan with help of mine.", "To keep going say Hi to me."]

# Error set
defualt_missing_data_error = [
    "Please say hi to me", "I guess you have not entered anything...! "]
defualt_error = ["I can't do that for you.", "To keep going say hi to me."]


def loan_assistant_welcome_msg():
    welcome_json_obj = json.dumps({'message_human': "", 'message_bot': assistant_defualt_welcome_msg,
                                   'suggestion_message': ["Hi"], 'current_form_action': "/welcomemsg_chat",
                                   'next_form_action': "/hi_chat?msg=", 'previous_form_action': "",
                                   'next_field_type': "button", 'previous_field_type': "",
                                   "placeholder_text": "Hi"},
                                  sort_keys=True, indent=4,
                                  separators=(',', ': '), default=json_util.default)
    # welcome_json_obj = json.dumps(welcome_json_obj)
    return welcome_json_obj

def start_converation_action(humanmessage):
    START_CONV_KEYWORDS = ("hello", "hi", "Hi", "Hello")
    START_CONV_RESPONSES = [
        "Please provide me borrower's full name"]
    text = humanmessage
    start_res = ""
    if text.lower() in START_CONV_KEYWORDS:
        # start_res = random.choice(START_CONV_RESPONSES)
        start_conv_json_obj = json.dumps(
            {'message_human': text, 'message_bot': START_CONV_RESPONSES,
             'suggestion_message': ["Please provide me borrower's full name"],
             'current_form_action': "/hi_chat?msg=",
             'next_form_action': "/asking_borowers_full_name?msg=", 'previous_form_action': "/welcomemsg_chat",
             'next_field_type': "text",
             'previous_field_type': "button", "placeholder_text": "Enter borrower's full name",
             "max_length": "255"},
            sort_keys=True, indent=4,
            separators=(',', ': '), default=json_util.default)
    elif text.lower() == "" or text.lower() is None or len(text) == 0:
        start_conv_json_obj = json.dumps({'message_human': text,
                                          'message_bot': defualt_missing_data_error,
                                          'suggestion_message': ["Hi"], 'current_form_action': "/hi_chat?msg",
                                          'next_form_action': "", 'previous_form_action': "/welcomemsg_chat",
                                          'next_field_type': "", 'previous_field_type': "button",
                                          "placeholder_text": "Hi"},
                                         sort_keys=True, indent=4,
                                         separators=(',', ': '), default=json_util.default)
    else:
        start_conv_json_obj = json.dumps({'message_human': text,
                                          'message_bot': defualt_error,
                                          'suggestion_message': ["Hi"], 'current_form_action': "/hi_chat?msg",
                                          'next_form_action': "", 'previous_form_action': "/welcomemsg_chat",
                                          'next_field_type': "", 'previous_field_type': "button",
                                          "placeholder_text": "Hi"
                                          },
                                         sort_keys=True, indent=4,
                                         separators=(',', ': '), default=json_util.default)
    return start_conv_json_obj


def borrowers_name_asking(namestr):
    Name_RESPONSE = ["Please enter borrower's email ID"]
    if namestr.lower() and not (namestr.isdigit()) and len(namestr) <= 255:
        name_conv_json_obj = json.dumps(
            {'message_human': namestr, 'message_bot': Name_RESPONSE,
             'suggestion_message': ["Enter borrower's email ID"],
             'current_form_action': "/asking_borowers_full_name?msg=",
             'next_form_action': "/asking_borowers_email_id?msg=", 'previous_form_action': "/hi_chat?msg=",
             'next_field_type': "text",
             'previous_field_type': "text", "placeholder_text": "Enter borrower's email ID", "max_length": "255"},
            sort_keys=True, indent=4,
            separators=(',', ': '), default=json_util.default)
    elif namestr.lower() == "" or namestr.lower() is None or len(namestr) == 0:
        name_conv_json_obj = json.dumps({'message_human': namestr,
                                         'message_bot': ["I guess you have't entered anything.",
                                                         "Please enter borrowe's full name."],
                                         'suggestion_message': ["I guess you have't entered anything.",
                                                                "Please enter borrowe's full name."],
                                         'current_form_action': "/asking_borowers_full_name?msg=",
                                         'next_form_action': "", 'previous_form_action': "/hi_chat?msg=",
                                         'next_field_type': "", 'previous_field_type': "button",
                                         "placeholder_text": "Hi"},
                                        sort_keys=True, indent=4,
                                        separators=(',', ': '), default=json_util.default)
    else:
        name_conv_json_obj = json.dumps({'message_human': namestr,
                                         'message_bot': [
                                             "I guess borrower's name is too long or you have entered only digits",
                                             "Please enter borrower's valid name "],
                                         'suggestion_message': ["Please enter borrower's full name"],
                                         'current_form_action': "/asking_borowers_full_name?msg=",
                                         'next_form_action': "", 'previous_form_action': "/hi_chat?msg=",
                                         'next_field_type': "", 'previous_field_type': "button",
                                         "placeholder_text": ["Enter borrower's full name"]
                                         },
                                        sort_keys=True, indent=4,
                                        separators=(',', ': '), default=json_util.default)
    return name_conv_json_obj


def borrowers_email_id_asking(emailid):
    text = emailid
    MOBILE_NUMBER_KEYWORDS = ["Provide me borrower's 10 digit mobile number"]
    flag = re.search(r"^[a-z0-9]+(\.[a-z0-9]+)*(\w+)*@[a-z0-9]+(\.[a-z0-9]+)*(\.[a-z]{2,4})$", text.lower())
    if flag != None:
        emailid_conv_json_obj = json.dumps(
            {'message_human': text,
             'message_bot': [
                 "Provide me borrower's 10 digit mobile number without putting 0 or country code before it"],
             'suggestion_message': MOBILE_NUMBER_KEYWORDS,
             'current_form_action': "/asking_borowers_email_id?msg=",
             'next_form_action': "/mobilenumber_asking?msg=", 'previous_form_action': "/asking_borowers_full_name?msg=",
             'next_field_type': "number",
             'previous_field_type': "text", "placeholder_text": "Enter borrower's 10 digit mobile no",
             "max_length": "10"},
            sort_keys=True, indent=4,
            separators=(',', ': '), default=json_util.default)
    elif flag == None:
        emailid_conv_json_obj = json.dumps({'message_human': text,
                                            'message_bot': ["Please provide valid email id"],
                                            'suggestion_message': ["Enter borrower's valid email id"],
                                            'current_form_action': "/asking_borowers_email_id?msg=",
                                            'next_form_action': "",
                                            'previous_form_action': "/asking_borowers_full_name?msg=",
                                            'next_field_type': "", 'previous_field_type': "text",
                                            "placeholder_text": "Enter valid email id"},
                                           sort_keys=True, indent=4,
                                           separators=(',', ': '), default=json_util.default)
    elif text.lower() == "" or text.lower() is None or len(text) == 0:
        emailid_conv_json_obj = json.dumps({'message_human': text,
                                            'message_bot': ["You have't entered anything",
                                                            "Please provide me valid email id"],
                                            'suggestion_message': ["Enter borrower's valid email id"],
                                            'current_form_action': "/asking_borowers_email_id?msg=",
                                            'next_form_action': "",
                                            'previous_form_action': "/asking_borowers_full_name?msg=",
                                            'next_field_type': "", 'previous_field_type': "text",
                                            "placeholder_text": "Enter valid email id"},
                                           sort_keys=True, indent=4,
                                           separators=(',', ': '), default=json_util.default)

    else:
        emailid_conv_json_obj = json.dumps({'message_human': text,
                                            'message_bot': ["Please enter valid email id"],
                                            'suggestion_message': ["Enter borrower's valid email id"],
                                            'current_form_action': "/asking_borowers_email_id?msg=",
                                            'next_form_action': "",
                                            'previous_form_action': "/asking_borowers_full_name?msg=",
                                            'next_field_type': "", 'previous_field_type': "text",
                                            "placeholder_text": "Enter borrower's email id"
                                            },
                                           sort_keys=True, indent=4,
                                           separators=(',', ': '), default=json_util.default)
    return emailid_conv_json_obj

def mobilenumber_asking(mobileno):
    if mobileno.isdigit() and len(mobileno) == 10:

        mobilenumber_asking_json_obj = json.dumps({'message_human': mobileno,
                                                   'message_bot': [
                                                       "Can you please tell me how much amount of loan do you need?",
                                                       ],
                                                   'suggestion_message': ['Enter loan amount'],
                                                   'current_form_action': "/mobilenumber_asking?msg=",
                                                   'next_form_action': "/loan_chat?msg=",
                                                   'previous_form_action': "/asking_borowers_email_id?msg=",
                                                   'next_field_type': "button",
                                                   'previous_field_type': "text",
                                                   "placeholder_text": ['Enter loan amount'], "max_length": "10"
                                                   },
                                                  sort_keys=True, indent=4,
                                                  separators=(',', ': '))


    elif not (mobileno.isdigit()) or len(mobileno) != 10 or len(mobileno) < 10:
        mobilenumber_asking_json_obj = json.dumps({'message_human': mobileno,
                                                   'message_bot': ["Enter valid mobile number."],
                                                   'suggestion_message': [
                                                       "Please, provide me borrower's valid 10 digit mobile number without putting 0 or country code before it "],
                                                   'current_form_action': "/mobilenumber_asking?msg=",
                                                   'next_form_action': "",
                                                   'previous_form_action': "/asking_borowers_email_id?msg=",
                                                   'next_field_type': "",
                                                   'previous_field_type': "text",
                                                   "placeholder_text": ["Enter valid mobile number."],
                                                   "max_length": "10"
                                                   },
                                                  sort_keys=True, indent=4,
                                                  separators=(',', ': '))

    elif mobileno.lower() == "" or mobileno.lower() is None or len(mobileno) == 0:
        mobilenumber_asking_json_obj = json.dumps({'message_human': mobileno,
                                                   'message_bot': "You have not entered borrower's mobile number",
                                                   'suggestion_message': ["I gusss you have not entered anything...!",
                                                                          "Please, provide me borrower's valid 10 digit mobile number without putting 0 or country code before it "],
                                                   'current_form_action': "/mobilenumber_asking?msg=",
                                                   'next_form_action': "",
                                                   'previous_form_action': "/asking_borowers_email_id?msg=",
                                                   'next_field_type': "",
                                                   'previous_field_type': "text",
                                                   "placeholder_text": ["Enter valid mobile number."],
                                                   "max_length": "10"
                                                   },
                                                  sort_keys=True, indent=4,
                                                  separators=(',', ': '))

    else:
        mobilenumber_asking_json_obj = json.dumps({'message_human': mobileno,
                                                   'message_bot': "please enter borrower's valid 10 digit mobile number",
                                                   'suggestion_message': [
                                                       "Please, provide me borrower's valid 10 digit mobile number without putting 0 or country code before it "],
                                                   'current_form_action': "/mobilenumber_asking?msg=",
                                                   'next_form_action': "",
                                                   'previous_form_action': "/asking_borowers_email_id?msg=",
                                                   'next_field_type': "",
                                                   'previous_field_type': "text",
                                                   "placeholder_text": ["Enter valid mobile number."],
                                                   "max_length": "10"},
                                                  sort_keys=True, indent=4,
                                                  separators=(',', ': '))

    return mobilenumber_asking_json_obj

def loan_ammount_asking(loanammount):
    if loanammount.isdigit():
        loanammount = int(loanammount)
        if loanammount >= 100000 and loanammount <= 5000000:
            loan_ammount_json_obj = json.dumps(
                {'message_human': loanammount, 'loan_ammount_in_words': num2words(int(loanammount)),
                 'message_bot': ['Ok we are considering the ' + str(
                     loanammount) + " as borrower's loan ammount."],
                 'suggestion_message': ["Bye"], 'current_form_action': "/loan_chat?msg=",
                 'next_form_action': "/end_chat?msg=", 'previous_form_action': "/mobilenumber_asking?msg",
                 'next_field_type': "button",
                 'previous_field_type': "number", "placeholder_text": ["Bye"]},
                sort_keys=True, indent=4,
                separators=(',', ': '))
        elif loanammount < 100000:
            loan_ammount_json_obj = json.dumps(
                {'message_human': loanammount, 'loan_ammount_in_words': num2words(int(loanammount)),
                 'message_bot': ['Sorry but we are doing loans in range of 100000 to 5000000.',
                                 'We can consider 1000000 ammount of loan for you at first glance.',
                                 ],
                 'suggestion_message': ["Bye"], 'current_form_action': "/loan_chat?msg=",
                 'next_form_action': "/end_chat?msg=", 'previous_form_action': "/mobilenumber_asking?msg",
                 'next_field_type': "button",
                 'previous_field_type': "number", "placeholder_text": ["Bye"]},
                sort_keys=True, indent=4,
                separators=(',', ': '))

        elif loanammount > 5000000:
            loan_ammount_json_obj = json.dumps({'message_human': loanammount,
                                                'message_bot': [
                                                    'Sorry but we are doing loans in range of 100000 to 5000000.',
                                                    'We can consider 50000000 ammount of loan for you at first glance.',
                                                    ],
                                                'suggestion_message': ["Bye"],
                                                'current_form_action': "/loan_chat?msg=",
                                                'next_form_action': "/end_chat?msg=",
                                                'previous_form_action': "/mobilenumber_asking?msg", 'next_field_type': "button",
                                                'previous_field_type': "number",
                                                "placeholder_text": ["Bye"]},
                                               sort_keys=True, indent=4,
                                               separators=(',', ': '))
    elif not (loanammount.isdigit()):
        loan_ammount_json_obj = json.dumps({'message_human': loanammount,
                                            'message_bot': [
                                                "Please enter the loan ammount in digits between the range of 1000000 and 5000000."],
                                            'suggestion_message': [""],
                                            'current_form_action': "/loan_chat?msg=",
                                            'next_form_action': "",
                                            'previous_form_action': "/mobilenumber_asking?msg", 'next_field_type': "",
                                            'previous_field_type': "number",
                                            "placeholder_text": "Please enter the loan ammount in digits between the range of 1000000 and 5000000."},
                                           sort_keys=True, indent=4,
                                           separators=(',', ': '))
    return loan_ammount_json_obj

def user_bye_str(userbye):
    USER_BYE_KEYWORDS = (
        "ok.", "take care", "ok take tare", "ok tc", "thanks", "thank you", "thx", "bye", "ok bye", "bye and thanks",
        "thanks and bye", "bye & thanks", "thanks & bye", "Bye")
    USER_BYE_RESPONSE = [
        "Thanks for connecting with loan application assistant..!",
        "Our loan executive will connect you soon...!",
        "Have a great day...!",
        "Bye!"]

    if userbye.lower() in USER_BYE_KEYWORDS:
        user_bye_str_json_obj = json.dumps({'message_human': userbye,
                                            'message_bot': USER_BYE_RESPONSE,
                                            'suggestion_message': "",
                                            'current_form_action': "/end_chat?msg=",
                                            'next_form_action': "/end_chat?msg=",
                                            'previous_form_action': "/last_itr_status?msg=",
                                            'next_field_type': "",
                                            'previous_field_type': "number",
                                            "placeholder_text": ""
                                            },
                                           sort_keys=True, indent=4,
                                           separators=(',', ': '))

    elif userbye.lower() == "" or userbye.lower() is None or len(userbye) == 0:
        user_bye_str_json_obj = json.dumps({'message_human': userbye,
                                            'message_bot': ["You have entered nothing...!", " Say Bye to me"],
                                            'suggestion_message': ["Say bye"],
                                            'current_form_action': "/end_chat?msg=",
                                            'next_form_action': "",
                                            'previous_form_action': "/last_itr_status?msg=",
                                            'next_field_type': "",
                                            'previous_field_type': "number",
                                            "placeholder_text": ""
                                            },
                                           sort_keys=True, indent=4,
                                           separators=(',', ': '))

    else:
        user_bye_str_json_obj = json.dumps({'message_human': userbye,
                                            'message_bot': USER_BYE_RESPONSE,
                                            'suggestion_message': "",
                                            'current_form_action': "/end_chat?msg=",
                                            'next_form_action': "/end_chat?msg=",
                                            'previous_form_action': "/last_itr_status?msg=",
                                            'next_field_type': "",
                                            'previous_field_type': "number",
                                            "placeholder_text": ""
                                            },
                                           sort_keys=True, indent=4,
                                           separators=(',', ': '))

    return user_bye_str_json_obj