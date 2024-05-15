from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from services import get_option_list, get_image_path


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/image", StaticFiles(directory="image"), name="image")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_root(
    request: Request,
):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/{option_string}", response_class=HTMLResponse)
async def pick(request: Request, option_string: str):

    option_list = get_option_list(option_string)
    image_path = get_image_path(option_list[0])

    image = {
        "url": image_path,
        "thumbnail_url": image_path,
    }

    return templates.TemplateResponse(
        "result.html",
        {"request": request, "option_list": option_list, "image": image},
    )


@app.get("/{option_string}/{seed}", response_class=HTMLResponse)
async def pick_by_seed(request: Request, option_string: str, seed: str):

    option_list = get_option_list(option_string, seed)
    image_path = get_image_path(option_list[0])

    image = {
        "url": image_path,
        "thumbnail_url": image_path,
    }

    return templates.TemplateResponse(
        "result.html",
        {"request": request, "option_list": option_list, "image": image},
    )
