#generate new model
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import numpy as np
import tensorflow as tf
from tensorflow import keras

def create_model():
    # Define the model architecture
    model = keras.Sequential([
        keras.layers.Dense(16, activation=tf.nn.relu, input_shape=(2,)),
        keras.layers.Dense(16, activation=tf.nn.relu),
        keras.layers.Dense(1)
    ])

    # Compile the model
    model.compile(optimizer=tf.optimizers.Adam(0.01), loss='mean_squared_error', metrics=['accuracy'])
    return model