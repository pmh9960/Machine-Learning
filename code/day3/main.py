"""
import numpy as np
from MLPerceptron import XOR

X = [0, 0, 0, 0, 0, 1]
print(XOR(X))
X = [0, 1, 0, 0, 0, 1]
print(XOR(X))
X = [1, 0, 0, 0, 0, 1]
print(XOR(X))
X = [1, 1, 0, 0, 0, 1]
print(XOR(X))
"""
"""
import numpy as np
import matplotlib.pylab as plt
from functions import step, sigmoid, ReLU

x = np.arange(-5, 5, 0.1)
y1 = step(x)
y2 = sigmoid(x)
y3 = ReLU(x)
plt.plot(x,y1, color = "blue")
plt.plot(x,y2, color = "red")
plt.plot(x,y3, color = "green")
plt.ylim(-0.1,3)
plt.show()
"""
"""
import numpy as np
x = np.array([0.5, 0.8, -1.2])
W1 = np.array([
    [2,2,-1],
    [2,2,0],
    [0,-1,-1]
])
W2 = np.array([
    [2,2,-1],
    [-1,0,0],
    [2,-1,2]
])
W3 = np.array([
    [2,-1,0],
    [-1,-1,0],
    [2,0,0]
])
y = np.dot(W3,np.dot(W2,np.dot(W1,x)))
print(y)
"""
import numpy as np
import matplotlib.pyplot as plt
from functions import softmax
X = np.array([1, 2, 3])
softmax_X = softmax(X)
plt.pie(softmax_X, labels=softmax_X)
plt.show()