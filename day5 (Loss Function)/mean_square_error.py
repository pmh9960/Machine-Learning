import numpy as np

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]


def mean_square_error(y, t):
    return np.sum(((y - t) ** 2) / len(y))


print(mean_square_error(np.array(y), np.array(t)))
