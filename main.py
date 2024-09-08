from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

from datetime import datetime

from services import get_option_list, get_image_path


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/image", StaticFiles(directory="image"), name="image")
templates = Jinja2Templates(directory="templates")


# Serve favicon.ico
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")  # adjust the path if necessar


@app.get("/", response_class=HTMLResponse)
def read_root(
    request: Request,
):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/{option_string}", response_class=HTMLResponse)
async def pick(request: Request, option_string: str):

    date_seed = datetime.now().strftime("%Y-%m-%d")

    option_list = get_option_list(option_string, seed=date_seed)
    image_path = get_image_path(option_list[0])

    image = {
        "url": image_path,
        "thumbnail_url": image_path,
    }

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "option_list": option_list,
            "image": image,
            "seed": date_seed,
        },
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
        {"request": request, "option_list": option_list, "image": image, "seed": seed},
    )
