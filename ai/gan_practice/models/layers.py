import tensorflow as tf
import numpy as np

def weight_variable(shape, stddev=0.01):
    """
    새로운 가중치 변수를 주어진 shape에 맞게 선언하고,
    Normal(0.0, stddev^2)의 정규분포로부터의 샘플링을 통해 초기화함.
    :param shape: list(int).
    :param stddev: float, 샘플링 대상이 되는 정규분포의 표준편차 값.
    :return weights: tf.Variable.
    """
    weights = tf.get_variable('weights', shape, tf.float32,
                              tf.random_normal_initializer(mean=0.0, stddev=stddev))
    return weights


def bias_variable(shape, value=1.0):
    """
    새로운 바이어스 변수를 주어진 shape에 맞게 선언하고, 
    주어진 상수값으로 추기화함.
    :param shape: list(int).
    :param value: float, 바이어스의 초기화 값.
    :return biases: tf.Variable.
    """
    biases = tf.get_variable('biases', shape, tf.float32,
                             tf.constant_initializer(value=value))
    return biases

def conv_layer(x, filters, kernel_size, strides, padding='SAME', use_bias=True):
    return tf.layers.conv2d(x, filters, kernel_size, strides, padding, use_bias=use_bias, kernel_initializer=tf.initializers.random_normal(0.0, 0.02))

def deconv_layer(x, filters, kernel_size, strides, padding='SAME', use_bias=True):
    return tf.layers.conv2d_transpose(x, filters, kernel_size, strides, padding, use_bias=use_bias, kernel_initializer=tf.initializers.random_normal(0.0, 0.02))

def batchNormalization(x, is_train):
    """
    Add a new batchNormalization layer.
    :param x: tf.Tensor, shape: (N, H, W, C) or (N, D)
    :param is_train: tf.placeholder(bool), if True, train mode, else, test mode
    :return: tf.Tensor.
    """
    return tf.layers.batch_normalization(x, training=is_train, momentum=0.9, epsilon=1e-5, center=True, scale=True)


def conv_bn_lrelu(x, filters, kernel_size, is_train, strides=(1, 1), padding='SAME', bn=True, alpha=0.2):
    """
    Add conv + bn + Leaky Relu layers.
    see conv_layer and batchNormalization function
    If you want relu, just change alpha to 0
    If you don't want activation layer, change alpha to 1.0
    """
    conv = conv_layer(x, filters, kernel_size, strides, padding, use_bias=True)
    if bn:
        _bn = batchNormalization(conv, is_train)
    else:
        _bn = conv
    return tf.nn.leaky_relu(_bn, alpha)
    
def deconv_bn_relu(x, filters, kernel_size, is_train, strides=(1, 1), padding='SAME', bn=True, relu=True):
    """
    Add conv + bn + Relu layers.
    see conv_layer and batchNormalization function
    """
    deconv = deconv_layer(x, filters, kernel_size, strides, padding, use_bias=True)
    if bn:
        _bn = batchNormalization(deconv, is_train)
    else:
        _bn = deconv
    if relu:
        return tf.nn.relu(_bn)
    else:
        return _bn


def fc_layer(x, out_dim, **kwargs):
    """
    Add a new fully-connected layer.
    :param x: tf.Tensor, shape: (N, D).
    :param out_dim: int, the dimension of output vector.
    :return: tf.Tensor.
    """
    weights_stddev = kwargs.pop('weights_stddev', 0.02)
    biases_value = kwargs.pop('biases_value', 0.0)
    in_dim = int(x.get_shape()[-1])

    weights = weight_variable([in_dim, out_dim], stddev=weights_stddev)
    biases = bias_variable([out_dim], value=biases_value)
    return tf.matmul(x, weights) + biases


def fc_bn_lrelu(x, out_dim, is_train, alpha=0.2):
    """
    Add fc + bn + Leaky Relu layers
    see fc_layer and batchNormalization function
    """
    fc = fc_layer(x, out_dim)
    bn = batchNormalization(fc, is_train)
    return tf.nn.leaky_relu(bn, alpha)