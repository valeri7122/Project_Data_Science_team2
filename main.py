from fastapi import FastAPI, File, UploadFile
from model.components import predict, read_imagefile
import uvicorn
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index():

    return FileResponse("static/index.html")


@app.post('/predict/image')
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = predict(image)
    pred = f"""
	    <html>
            <head>
                <title>Image prediction</title>
            </head>
	        <body bgcolor=blue>
        		<br/><br/>
        		<input type="button" onclick="history.back();" value="Повернутись на головну сторінку"/>
        		<br/><br/><br/><br/><br/><br/><br/><br/>
        		<h1 align="center"><font size="10" color=yellow face="Arial">{prediction}</font></h1>
            </body>
        </html>
        """

    return HTMLResponse(content=pred, status_code=200)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
