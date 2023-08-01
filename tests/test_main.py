from fastapi.testclient import TestClient

from PIL import Image
from io import BytesIO

import main


client = TestClient(main.app)



def test_index():
    """
    The test_index function tests the index route.
    It does this by making a GET request to /, and then asserting that the response has status code 200 (OK) and that its content type is text/html; charset=utf-8.
    
    :return: The response of the index page
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"


def test_predict_api():
    """
    The test_predict_api function tests the predict API endpoint.
    It does so by creating a new image, saving it to memory, and then sending it to the server.
    The response is checked for a 200 status code and an HTML content type.
    
    :return: A 200 status code and a content-type of text/html; charset=utf-8
    """
    file_data = BytesIO()
    image = Image.new('RGB', size=(100, 100), color=(255, 0, 0))
    image.save(file_data, 'jpeg')
    file_data.seek(0)

    response = client.post('/predict/image', files={"file": ("test.jpg", file_data, "image/jpeg")})
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"