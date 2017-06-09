from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import os
import random
import sys
import time
import logging

import numpy as np
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf

#import data_utils
import nltk
from tensorflow.models.rnn.translate import seq2seq_model
from tensorflow.models.rnn.translate import data_utils
#import seq2seq_model

tf.app.flags.DEFINE_float("learning_rate", 0.5, "Learning rate.")
tf.app.flags.DEFINE_float("learning_rate_decay_factor", 0.99,
                          "Learning rate decays by this much.")
tf.app.flags.DEFINE_float("max_gradient_norm", 5.0,
                          "Clip gradients to this norm.")
tf.app.flags.DEFINE_integer("batch_size", 32,
                            "Batch size to use during training.")
tf.app.flags.DEFINE_integer("size", 512, "Size of each model layer.")
tf.app.flags.DEFINE_integer("num_layers", 2, "Number of layers in the model.")
tf.app.flags.DEFINE_integer("s_vocab_size", 30000, "Source language vocabulary size.")
tf.app.flags.DEFINE_integer("t_vocab_size", 30000, "Target language vocabulary size.")
tf.app.flags.DEFINE_string("data_dir", "/home/jalaj/PycharmProjects/NLPython/NLPython/ch9/MT/data", "Data directory")
tf.app.flags.DEFINE_string("train_dir", "/home/jalaj/PycharmProjects/NLPython/NLPython/ch9/MT/runs/de_en_lstm_reg/", "Training directory.")
tf.app.flags.DEFINE_integer("max_train_data_size", 0,
                            "Limit on the size of training data (0: no limit).")
tf.app.flags.DEFINE_integer("steps_per_checkpoint", 200,
                            "How many training steps to do per checkpoint.")
tf.app.flags.DEFINE_boolean("use_fp16", False,
                            "Train using fp16 instead of fp32.")

FLAGS = tf.app.flags.FLAGS

# We use a number of buckets and pad to the closest one for efficiency.
# See seq2seq_model.Seq2SeqModel for details of how they work.
_buckets = [(5, 10), (10, 15), (20, 25), (40, 50)]

def read_data(source_path, target_path, max_size=None):
  """Read data from source and target files and put into buckets.
  Args:
    source_path: path to the files with token-ids for the source language.
    target_path: path to the file with token-ids for the target language;
      it must be aligned with the source file: n-th line contains the desired
      output for n-th line from the source_path.
    max_size: maximum number of lines to read, all other will be ignored;
      if 0 or None, data files will be read completely (no limit).
  Returns:
    data_set: a list of length len(_buckets); data_set[n] contains a list of
      (source, target) pairs read from the provided data files that fit
      into the n-th bucket, i.e., such that len(source) < _buckets[n][0] and
      len(target) < _buckets[n][1]; source and target are lists of token-ids.
  """
  data_set = [[] for _ in _buckets]
  with tf.gfile.GFile(source_path, mode="r") as source_file:
    with tf.gfile.GFile(target_path, mode="r") as target_file:
      source, target = source_file.readline(), target_file.readline()
      counter = 0
      while source and target and (not max_size or counter < max_size):
        counter += 1
        if counter % 100000 == 0:
          print("  reading data line %d" % counter)
          sys.stdout.flush()
        source_ids = [int(x) for x in source.split()]
        target_ids = [int(x) for x in target.split()]
        target_ids.append(data_utils.EOS_ID)
        for bucket_id, (source_size, target_size) in enumerate(_buckets):
          if len(source_ids) < source_size and len(target_ids) < target_size:
            data_set[bucket_id].append([source_ids, target_ids])
            break
        source, target = source_file.readline(), target_file.readline()
  return data_set


def create_model(session, use_lstm, forward_only):
  """Create translation model and initialize or load parameters in session."""
  dtype = tf.float16 if FLAGS.use_fp16 else tf.float32
  model = seq2seq_model.Seq2SeqModel(
      FLAGS.s_vocab_size,
      FLAGS.t_vocab_size,
      _buckets,
      FLAGS.size,
      FLAGS.num_layers,
      FLAGS.max_gradient_norm,
      FLAGS.batch_size,
      FLAGS.learning_rate,
      FLAGS.learning_rate_decay_factor,
      use_lstm=use_lstm,
      forward_only=forward_only,
      dtype=dtype)
  ckpt = tf.train.get_checkpoint_state(FLAGS.train_dir)
  if ckpt:
  # and tf.train.checkpoint_exists(ckpt.model_checkpoint_path):
    print("Reading model parameters from %s" % ckpt.model_checkpoint_path)
    model.saver.restore(session, ckpt.model_checkpoint_path)
  else:
    print("Created model with fresh parameters.")
    session.run(tf.initialize_all_variables())
  return model


def train():
  """Train a translation model using NMT data."""
  source = sys.argv[1]
  target = sys.argv[2]
  # Prepare NMT data.
  print("Preparing NMT data in %s" % FLAGS.data_dir)
  print("    source langauge: %s" % source)
  print("    target language: %s" % target)

  s_train, t_train, s_dev, t_dev, _,_ = data_utils.prepare_wmt_data(FLAGS.data_dir,
                                                                    FLAGS.s_vocab_size, FLAGS.t_vocab_size)
  with tf.Session() as sess:
    # Create model.
    print("Creating %d layers of %d units." % (FLAGS.num_layers, FLAGS.size))
    model = create_model(sess, False, False)

    # Read data into buckets and compute their sizes.
    print("Reading development and training data (limit: %d)."
          % FLAGS.max_train_data_size)
    dev_set = read_data(s_dev, t_dev)
    train_set = read_data(s_train, t_train, FLAGS.max_train_data_size)
    train_bucket_sizes = [len(train_set[b]) for b in xrange(len(_buckets))]
    train_total_size = float(sum(train_bucket_sizes))

    # A bucket scale is a list of increasing numbers from 0 to 1 that we'll use
    # to select a bucket. Length of [scale[i], scale[i+1]] is proportional to
    # the size if i-th training bucket, as used later.
    train_buckets_scale = [sum(train_bucket_sizes[:i + 1]) / train_total_size
                           for i in xrange(len(train_bucket_sizes))]

    # This is the training loop.
    step_time, loss = 0.0, 0.0
    current_step = 0
    previous_losses = []
    perplexity = 1e10
    train_steps, train_ppx, bucket_ppx = [], [], {0:[], 1:[], 2:[], 3:[]}
    
    while perplexity>20.:
      # Choose a bucket according to data distribution. We pick a random number
      # in [0, 1] and use the corresponding interval in train_buckets_scale.
      random_number_01 = np.random.random_sample()
      bucket_id = min([i for i in xrange(len(train_buckets_scale))
                       if train_buckets_scale[i] > random_number_01])

      # Get a batch and make a step.
      start_time = time.time()
      encoder_inputs, decoder_inputs, target_weights = model.get_batch(
          train_set, bucket_id)
      _, step_loss, _ = model.step(sess, encoder_inputs, decoder_inputs,
                                   target_weights, bucket_id, False)
      step_time += (time.time() - start_time) / FLAGS.steps_per_checkpoint
      loss += step_loss / FLAGS.steps_per_checkpoint
      current_step += 1

      # Once in a while, we save checkpoint, print statistics, and run evals.
      if current_step % FLAGS.steps_per_checkpoint == 0:
        train_steps.append(current_step)
        # Print statistics for the previous epoch.
        perplexity = math.exp(float(loss)) if loss < 300 else float("inf")
        train_ppx.append(perplexity)
        print("global step %d learning rate %.4f step-time %.2f perplexity "
              "%.2f" % (model.global_step.eval(), model.learning_rate.eval(),
                        step_time, perplexity))
        # Decrease learning rate if no improvement was seen over last 3 times.
        if len(previous_losses) > 2 and loss > max(previous_losses[-3:]):
          sess.run(model.learning_rate_decay_op)
        previous_losses.append(loss)
        # Save checkpoint and zero timer and loss.
        checkpoint_path = os.path.join(FLAGS.train_dir, "translate.ckpt")
        model.saver.save(sess, checkpoint_path, global_step=model.global_step)
        step_time, loss, eval_loss_tot = 0.0, 0.0, 0.0
        # Run evals on development set and print their perplexity.
        for bucket_id in xrange(len(_buckets)):
          if len(dev_set[bucket_id]) == 0:
            print("  eval: empty bucket %d" % (bucket_id))
            continue
          encoder_inputs, decoder_inputs, target_weights = model.get_batch(
              dev_set, bucket_id)
          _, eval_loss, _ = model.step(sess, encoder_inputs, decoder_inputs,
                                       target_weights, bucket_id, True)
          eval_ppx = math.exp(float(eval_loss)) if eval_loss < 300 else float("inf")
          bucket_ppx[bucket_id].append(eval_ppx)
          print("  eval: bucket %d perplexity %.2f" % (bucket_id, eval_ppx))
          eval_loss_tot += eval_loss
        eval_loss_avg = eval_loss_tot/len(_buckets)
        eval_ppx = math.exp(float(eval_loss_avg)) if eval_loss < 300 else float("inf")
        print("  eval: mean perplexity %.2f" % eval_ppx)
        sys.stdout.flush()
    print(train_steps)
    print(train_ppx)
    print(bucket_ppx)


def testBLEU():
  source = sys.argv[1]
  target = sys.argv[2]
  with tf.Session() as sess:
    # Create model and load parameters.
    model = create_model(sess, True, True)
    model.batch_size = 1  # We decode one sentence at a time.

    # Load vocabularies.
    s_vocab_path = os.path.join(FLAGS.data_dir,
                                "vocab%d.%s" % (FLAGS.s_vocab_size, source))
    t_vocab_path = os.path.join(FLAGS.data_dir,
                                "vocab%d.%s" % (FLAGS.t_vocab_size, target))
    s_vocab, _ = data_utils.initialize_vocabulary(s_vocab_path)
    _, rev_t_vocab = data_utils.initialize_vocabulary(t_vocab_path)

    # Decode from standard input.
    BLEUscore = {0:[], 1:[], 2:[], 3:[]}
    s_test_path = os.path.join(FLAGS.data_dir, "test.%s" % source)
    t_test_path = os.path.join(FLAGS.data_dir, "test.%s" % target)
    f_s = open(s_test_path, 'r')
    f_t = open(t_test_path, 'r')
    # print(f_s.readline())
    step = 0
    for sentence in f_s:
      print(step)
      # sentence = f_ja.readline()
      # Get token-ids for the input sentence.
      token_ids = data_utils.sentence_to_token_ids(tf.compat.as_bytes(sentence), s_vocab)
      # Which bucket does it belong to?
      bucket_id = len(_buckets) - 1
      for i, bucket in enumerate(_buckets):
        if bucket[0] >= len(token_ids):
          bucket_id = i
          break
      else:
        logging.warning("Sentence truncated: %s", sentence) 

      # Get a 1-element batch to feed the sentence to the model.
      encoder_inputs, decoder_inputs, target_weights = model.get_batch(
          {bucket_id: [(token_ids, [])]}, bucket_id)
      # Get output logits for the sentence.
      _, _, output_logits = model.step(sess, encoder_inputs, decoder_inputs,
                                       target_weights, bucket_id, True)
      # This is a greedy decoder - outputs are just argmaxes of output_logits.
      outputs = [int(np.argmax(logit, axis=1)) for logit in output_logits]
      # If there is an EOS symbol in outputs, cut them at that point.
      if data_utils.EOS_ID in outputs:
        outputs = outputs[:outputs.index(data_utils.EOS_ID)]
      # Print out Japanese sentence corresponding to outputs.
      candidate = [tf.compat.as_str(rev_t_vocab[output]) for output in outputs]
      reference = f_t.readline().split(' ')
      try:
        temp_score = nltk.translate.bleu_score.sentence_bleu([reference], candidate)
      except:
        temp_score = nltk.translate.bleu_score.sentence_bleu([reference], candidate, weights=(.5, .5))
      BLEUscore[bucket_id].append(temp_score)
      step += 1
      print(temp_score)
    for key,val in BLEUscore.iteritems():
      print(key, ": ", np.mean(val))
    # print(np.mean(BLEUscore))


def main(_):
  train()
  testBLEU()


if __name__ == "__main__":
  tf.app.run()
