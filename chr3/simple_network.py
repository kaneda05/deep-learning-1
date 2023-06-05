import numpy as np
from sigmoid import sigmoid
from softmax import softmax

def identity_function(x):
    return x

def init_network():
    network = {}
    network['w1'] = np.array([[0.1, 0.3, 0.5],[0.2, 0.4 ,0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['w2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['w3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network

def forward(network, x):
    w1, w2, w3 = network['w1'], network['w2'], network['w3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, w1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, w2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, w3) + b3
    y1 = identity_function(a3) # 出力をそのままにして返す
    y2 = softmax(a3)           # 出力をsoftmax関数にして返す(分類タスクでよく使用)

    return y1,y2