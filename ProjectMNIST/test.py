import os
import sys

sys.path.append(os.pardir)
import numpy as np
import pickle
from common.functions import sigmoid, softmax
from data_mnist.mnist import load_mnist
from PIL import Image

currentPath = os.getcwd()
os.chdir(currentPath + "\\ProjectMNIST")

# (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

# print(x_train.shape)
# print(t_train.shape)
# print(x_test.shape)
# print(t_test.shape)


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


# img = x_train[35]
# label = t_train[35]
# img = img.reshape(28, 28)
# img_show(img)


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(
        flatten=True, normalize=True, one_hot_label=False
    )
    return x_test, t_test


def init_network():
    with open("sample_weight.pkl", "rb") as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    return y


x, t = get_data()
network = init_network()
accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)
    if p == t[i]:
        accuracy_cnt += 1

print("Accuracy: " + str(float(accuracy_cnt / len(x))))
