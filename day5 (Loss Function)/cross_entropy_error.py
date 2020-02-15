import numpy as np

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y01 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
y02 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]


def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))


print(cross_entropy_error(np.array(y01), np.array(t)))
print(cross_entropy_error(np.array(y02), np.array(t)))
