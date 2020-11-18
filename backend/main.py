from image_processing import process_image

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/process_image/{item_id}", response_class=HTMLResponse)
async def process_image(request: Request, item_id: str):
    # process_image(request.image)
    return {"item_id": item_id, "request": request}
