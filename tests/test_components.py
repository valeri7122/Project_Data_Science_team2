import pytest
import keras.engine.sequential
import model.components as model_components

from PIL import Image, JpegImagePlugin
from io import BytesIO



@pytest.fixture()
def file():
    """
    The file function returns a file object that can be used to test the
        model.components.ImageInput class.
    
    :return: A file-like object, which is an object that acts like a file
    """
    file_data = BytesIO()
    image = Image.new('RGB', size=(100, 100), color=(255, 0, 0))
    image.save(file_data, 'jpeg')
    file_data.seek(0)

    return file_data


def test_load_model():
    """
    The test_load_model function tests the load_model function in model/components.py
        The test_load_model function checks that the result of calling load_model is an instance of keras.engine.sequential.Sequential
    
    
    :return: An instance of the sequential class
    """
    result = model_components.load_model()
    assert isinstance(result, keras.engine.sequential.Sequential)


def test_read_imagefile(file):
    """
    The test_read_imagefile function tests the read_imagefile function in model/components.py
        The test_read_imagefile function takes a file as an argument and reads it using the read_imagefile
        function from model/components.py, then asserts that the result is of type JpegImagePlugin.JpegImageFile
    
    :param file: Read the file that is passed in
    :return: A jpegimageplugin
    """
    result = model_components.read_imagefile(file.read())
    assert isinstance(result, JpegImagePlugin.JpegImageFile)


def test_predict(file):
    """
    The test_predict function tests the predict function in model/components.py
        The test_predict function takes a file as an argument and reads it into memory.
        It then passes that image to the predict function, which returns a string of 
        predicted labels for that image. The test_predict asserts that this returned value is indeed a string.
    
    :param file: Read the image file and convert it to a numpy array
    :return: A string
    """
    image = model_components.read_imagefile(file.read())
    result = model_components.predict(image)
    assert isinstance(result, str)
