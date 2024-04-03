from os import path
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


def generate_image(text):

    # Image size
    width, height = 704, 352
    background_color = (255, 255, 255)  # White background

    # Text settings
    font_color = (0, 0, 0)  # Black text
    font_size = 100

    # Create a blank image
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Use a truetype font
    # On Windows, you might need to provide the full path to a font file
    # On other operating systems, you can specify the font name directly if it's installed
    # For example, on many Linux systems, you can use 'DejaVuSans.ttf'
    # font = ImageFont.truetype("DejaVuSans.ttf", font_size)
    # font = ImageFont.load_default(font_size)
    font = ImageFont.truetype("MaruBuri-Regular.ttf", font_size)

    _, _, w, h = draw.textbbox((0, 0), text, font=font)
    draw.text(
        ((width - w) / 2, (height - h) / 2),
        text,
        font=font,
        fill=font_color,
    )

    image_name = datetime.now().strftime("%Y%m%d%H%M%S") + text + ".png"
    image_path = path.join("image", image_name)

    # Save the image
    image.save(image_path)

    # Provide the path for download
    return image_path
