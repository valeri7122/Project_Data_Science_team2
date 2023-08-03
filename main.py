from fastapi import FastAPI, File, UploadFile, HTTPException
from model.components import predict, read_imagefile
import uvicorn
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index():
    """
    The index function is a simple function that returns the index.html file
        from the static directory. This is used to serve up our web page.

    :return: A fileresponse object
    """
    return FileResponse("static/index.html")


@app.post('/predict/image', status_code=200)
async def predict_api(file: UploadFile = File(...)):
    """
    The predict_api function is a ReST API that takes an image file as input and returns the predicted class of the image.
    
    
    :param file: UploadFile: Get the uploaded file from the user
    :return: A string that is the predicted class
    """
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        raise HTTPException(
            status_code=404, detail="Image could not be downloaded"
        )
    file_read = await file.read()
    image = read_imagefile(file_read)
    prediction = predict(image)
    file_path = f"static/upload/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file_read)
    pred = response(file.filename, prediction)
    
    return HTMLResponse(content=pred, status_code=200)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
