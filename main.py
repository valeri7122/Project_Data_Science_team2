import uvicorn
import tensorflow as tf
from fastapi import FastAPI, File, UploadFile
import numpy as np
import uvicorn
from matplotlib import image
from matplotlib import pyplot as plt
from tensorflow.keras.utils import img_to_array, array_to_img



#MODEL = tf.keras.models.load_model('model/')


app = FastAPI()



@app.get('/')
async def index():
    return {"Message": "Welcome to Neural Network"}

@app.post('/predict/')
async def predict(file: UploadFile = File()):

    with open(file.filename, "wb") as f:
        f.write(await file.read())

    img = image.imread(file.filename)
    img_reduced = array_to_img(img, scale=False).resize((32,32))
    img_reduced_transformed = (img_to_array(img_reduced).astype('float32')/255)

    plt.imshow(img_reduced_transformed)
    plt.show()
    
    #prediction = MODEL.predict([...])

    return {"prediction": 'prediction'}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
