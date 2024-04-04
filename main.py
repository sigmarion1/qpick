import os
from datetime import datetime
import random

from fastapi import FastAPI, Request, Depends, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from sqlalchemy.orm import Session
from PIL import Image

from image_generator import generate_image

# from models import Image as ImageModel
# from database import SessionLocal, engine, Base

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

    option_list = option_string.split(",")

    random.shuffle(option_list)

    image_path = generate_image(option_list[0])

    image = {
        "url": image_path,
        "thumbnail_url": image_path,
    }

    return templates.TemplateResponse(
        "result.html", {"request": request, "option_list": option_list, "image": image}
    )


@app.get("/{option_string}/{seed}", response_class=HTMLResponse)
async def pick_by_seed(request: Request, option_string: str, seed: str):

    option_list = option_string.split(",")

    random.seed(seed)

    random.shuffle(option_list)

    image_path = generate_image(option_list[0])

    image = {
        "url": image_path,
        "thumbnail_url": image_path,
    }

    return templates.TemplateResponse(
        "result.html", {"request": request, "option_list": option_list, "image": image}
    )


# @app.post("/{image_name}", response_class=HTMLResponse)
# async def upload_image(
#     request: Request,
#     original: UploadFile,
#     thumbnail: UploadFile,
#     image_name: str,
#     db: Session = Depends(get_db),
# ):
#     image_name = image_name.lower()

#     print(len(original), len(thumbnail))
#     # if not file:
#     #     return templates.TemplateResponse(
#     #         "error.html", {"request": request, "error_message": "no file"}
#     #     )

#     file = files[0]

#     ext = file.filename.split(".")[-1]

#     if ext not in ("jpg", "jpeg", "png", "bmp", "gif", "tiff", "webp"):
#         return templates.TemplateResponse(
#             "error.html",
#             {"request": request, "error_message": "unsupported image format"},
#         )

#     content = await file.read()
#     temp_file = os.path.join("temp", file.filename)

#     with open(
#         temp_file,
#         "wb",
#     ) as fp:
#         fp.write(content)  # 서버 로컬 스토리지에 이미지 저장 (쓰기)

#     image_dir = os.path.join("image", datetime.now().strftime("%Y_%m"))

#     if not os.path.exists(image_dir):
#         os.makedirs(image_dir)

#     image_file = os.path.join(image_dir, image_name + ".png")
#     thumbnail_file = os.path.join(image_dir, image_name + "_th.png")

#     image = Image.open(temp_file)
#     image.thumbnail((1024, 1024))
#     image.save(image_file)
#     image.thumbnail((800, 400))
#     image.save(thumbnail_file)

#     newImage = ImageModel(name=image_name, url=image_file, thumbnail_url=thumbnail_file)
#     db.add(newImage)
#     db.commit()

#     os.remove(temp_file)

#     return templates.TemplateResponse(
#         "image.html", {"request": request, "image": newImage}
#     )
