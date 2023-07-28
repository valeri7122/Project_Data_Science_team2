import numpy as np

from io import BytesIO
from PIL import Image
from keras.layers import Flatten, Dense, Dropout
from keras.models import Sequential
from keras.applications.vgg16 import VGG16


model = None
filepath = "model/weights.h5"
class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']


def load_model():
    conv_base = VGG16(weights='imagenet', include_top=False, input_shape=(32, 32, 3))
    conv_base.trainable = False

    model = Sequential()
    model.add(conv_base)
    model.add(Flatten())
    model.add(Dense(256, activation='relu', name='hidden_1'))
    model.add(Dense(10, activation='softmax', name='predictions'))
    if filepath:
        model.load_weights(filepath)
    return model


def predict(image: Image.Image):
    global model
    if model is None:
        model = load_model()

    image = np.asarray(image.resize((32, 32)))[..., :3]
    image = np.expand_dims(image, 0)
    image = image / 255.0

    result = model.predict(image)
    response = class_names[np.array(result).argmax()]

    return f"Class: {response}"


def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image