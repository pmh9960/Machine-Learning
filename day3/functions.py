import numpy as np

def step(x):
    return np.array(x>0, dtype=np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def ReLU(x):
    return np.maximum(0, x)

def softmax(x):
    exp_x = np.exp(x-np.max(x))
    return exp_x/np.sum(exp_x)