import keras
import numpy as np

from io import BytesIO
from PIL import Image


model = None
filepath = "model/weights.h5"
class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']


def load_model():
    model = keras.models.load_model(filepath)
    
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