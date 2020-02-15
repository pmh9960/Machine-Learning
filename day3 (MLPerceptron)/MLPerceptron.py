import numpy as np


def XOR(X):
    W1 = [
        [-0.5, -0.5, 0, 0, 0, 0.7],  # nand
        [0.5, 0.5, 0, 0, 0, -0.2],  # or
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
    ]
    W2 = [
        [0.5, 0.5, 0, 0, 0, -0.7],  # and
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    x = np.array(X)
    w1 = np.array(W1)
    w2 = np.array(W2)
    s1 = np.array([0.0] * len(x))  # Hidden layer
    s2 = np.array([0.0] * len(x))
    for num in range(len(x)):
        s1[num] = np.sum(x * w1[num]) > 0
    for num in range(len(x)):
        s2[num] = np.sum(s1 * w2[num]) > 0

    return s2
