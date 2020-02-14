import os
import sys

sys.path.append(os.pardir)
import numpy as np
import pickle
from common.functions import sigmoid, softmax
from data_mnist.mnist import load_mnist
from PIL import Image


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

# print(x_train.shape)
# print(t_train.shape)
# print(x_test.shape)
# print(t_test.shape)


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


img = x_train[35]
label = t_train[35]
print(img.shape)
img = img.reshape(28, 28)
print(img.shape)

img_show(img)
