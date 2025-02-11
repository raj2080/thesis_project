# import tensorflow as tf
# print("TensorFlow Version:", tf.__version__)
# print("GPU Available:", tf.config.list_physical_devices('GPU'))



# import tensorflow as tf
# print("TensorFlow Version:", tf.__version__)
# print("GPU Available:", tf.config.list_physical_devices('GPU'))
#
# # Check which device is being used for computations
# tf.debugging.set_log_device_placement(True)
#
# # Run a small computation
# a = tf.constant([[1.0, 2.0, 3.0]])
# b = tf.constant([[4.0, 5.0, 6.0]])
# c = tf.matmul(a, b, transpose_b=True)
# print(c)










import tensorflow as tf
import tensorflow as tf

if tf.test.gpu_device_name():
    print(f'Default GPU Device: {tf.test.gpu_device_name()}')
else:
    print("Please check your installation")
