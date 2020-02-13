import os
import sys
import numpy as np
import pickle
from common.functions import sigmoid, softmax
from data_mnist.mnist import load_mnist
from PIL import Image
sys.path.append(os.pardir)
