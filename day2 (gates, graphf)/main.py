import numpy as np
import matplotlib.pyplot as plt
from make_graph import graphf
import gates

x1 = 0
x2 = 0
print(gates.XOR(x1, x2))

x1 = 0
x2 = 1
print(gates.XOR(x1, x2))

x1 = 1
x2 = 0
print(gates.XOR(x1, x2))

x1 = 1
x2 = 1
print(gates.XOR(x1, x2))
