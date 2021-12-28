import tensorflow.compat.v1 as tf
zero_out_module = tf.load_op_library('/Users/mtdp/tensorflow_source_code/tensorflow/bazel-bin/tensorflow/core/user_ops/zero_out.so')
with tf.Session(''):
    print(zero_out_module.zero_out([[1, 2], [3, 4]]).eval())