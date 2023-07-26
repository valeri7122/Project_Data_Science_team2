import tensorflow as tf
from fastapi import FastAPI, File, UploadFile
import numpy as np
import uvicorn



#MODEL = tf.keras.models.load_model('model/')

app = FastAPI()



@app.get('/')
async def index():
    return {"Message": "Welcome to Neural Network"}

@app.post('/predict/')
async def predict(file: UploadFile = File()):

    file = file
    #prediction = MODEL.predict([...])

    return {"prediction": 'prediction'}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)