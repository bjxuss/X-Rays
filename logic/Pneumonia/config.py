import numpy as np # linear algebra
import cv2 # import cv2

import matplotlib.pyplot as plt

import tensorflow as tf


IMG_SIZE = 224  # redimensionar imagen

# load model and predict some some external photo


def prepare(filepath):
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

def get_model():
    model = tf.keras.models.load_model("data\Pneumonia\Modelos Entrenados\cnn_model3_50_epoch.h5") # load model
    return model


