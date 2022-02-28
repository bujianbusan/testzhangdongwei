

import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
print('GPU', tf.config.list_physical_devices('GPU'))

a = tf.constant(2.)
b = tf.constant(3.)
print(a*b)
