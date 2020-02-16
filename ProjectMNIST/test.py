import os
import sys

sys.path.append(os.pardir)
import numpy as np
import pickle  # pickle 사용법 https://wayhome25.github.io/cs/2017/04/04/cs-04/
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


# W1, W2, W3 = network["W1"], network["W2"], network["W3"]
# print(x.shape, W1.shape, W2.shape, W3.shape, y.shape)
# (10000, 784) (784, 50) (50, 100) (100, 10) (10,)

"""
# 배치(Batch) 처리

IO에 상대적으로 많은 시간 소요
'메모리가 허용하는 한' 많은 데이터를 '한 번에' 읽어오기.

메모리에 따라서, 데이터에 따라서
N개를 M번 반복하는 것이 가장 빠름.

"""


x, t = get_data()
network = init_network()
batch_size = 100
accuracy_cnt = 0

for i in range(0, len(x), batch_size):
    x_batch = x[i : i + batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    # axis=0 : 열 별로 살펴봄
    # axis=1 : 행 별로 살펴봄
    accuracy_cnt += np.sum(p == t[i : i + batch_size])

print("Accuracy: " + str(float(accuracy_cnt / len(x))))

