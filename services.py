# services.py
import os
import random
from typing import List
from image_generator import (
    generate_image,
    add_emoji,
)  # Adjust the import according to your project structure


def get_option_list(option_string: str, seed: str | None = None) -> List[str]:
    option_list = option_string.split(",")

    option_list.sort()

    if seed:
        random.seed(seed)

    random.shuffle(option_list)

    return option_list


def get_image_path(option: str) -> str:

    # Define the images directory
    images_dir = "image"
    # Ensure the images directory exists
    os.makedirs(images_dir, exist_ok=True)

    # Define the image path
    image_path = os.path.join(images_dir, f"{option}.png")

    if os.path.exists(image_path):
        random.seed(None)
        random_number = random.randint(0, 10)
        # if random_number == 0:
        # add_emoji(option, image_path)
    else:
        generate_image(option, image_path)

    return image_path
