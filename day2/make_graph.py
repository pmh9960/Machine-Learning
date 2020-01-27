import numpy as np
import matplotlib.pyplot as plt

def graphf(x, y, label):
    x_axis = [0,] * len(x)
    y_axis = [0,] * len(y)

    plt.plot(x, y, label = label)
    plt.plot(x, y_axis, 'k')    # k = color = "black" (?)
    plt.plot(x_axis, y, 'k')

    plt.legend()
    plt.grid()
    plt.show()