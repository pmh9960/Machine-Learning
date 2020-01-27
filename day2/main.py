import numpy as np
import matplotlib.pyplot as plt
from make_graph import graphf

x = np.arange(-1, 2, 0.1)
y = x*x + 1

graphf(x, y, "y=3x+2")