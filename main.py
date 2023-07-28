import uvicorn
import tensorflow as tf
from fastapi import FastAPI, File, UploadFile
import numpy as np
import uvicorn
from matplotlib import image
from matplotlib import pyplot as plt
from tensorflow.keras.utils import img_to_array, array_to_img

from model.components import predict, read_imagefile


app = FastAPI()


@app.get('/')
async def index():
    return {"Message": "Welcome to Neural Network"}


@app.post('/predict/image')
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = predict(image)

    return prediction


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
