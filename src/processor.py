import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model('model.h5')
class Processor():
    def __init__(self) -> None:
        pass