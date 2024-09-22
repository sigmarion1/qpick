from PIL import Image, ImageDraw, ImageFont
import random
from consts import emojis


def generate_image(text, image_path):

    # Image size
    width, height = 704, 352
    background_color = (255, 255, 255)  # White background

    # Text settings
    font_color = "white"
    shadow_color = "black"

    font_size = 109

    # Create a blank image
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Use a truetype font
    # On Windows, you might need to provide the full path to a font file
    # On other operating systems, you can specify the font name directly if it's installed
    # For example, on many Linux systems, you can use 'DejaVuSans.ttf'
    # font = ImageFont.truetype("DejaVuSans.ttf", font_size)
    # font = ImageFont.load_default(font_size)
    font = ImageFont.truetype("font/SpoqaHanSansNeo-Regular.ttf", font_size)

    _, _, w, h = draw.textbbox((0, 0), text, font=font)

    x = (width - w) / 2
    y = (height - h) / 2

    draw.text(
        (x, y),
        text,
        font=font,
        fill=font_color,
        stroke_width=3,
        stroke_fill=shadow_color,
    )

    # image_name = datetime.now().strftime("%Y%m%d%H%M%S") + text + ".png"
    # image_path = path.join("image", image_name)

    # Save the image
    image.save(image_path)

    # Provide the path for download
    return image_path


def add_emoji(text, image_path):
    image = Image.open(image_path)

    font_size = 109
    font = ImageFont.truetype("NotoColorEmoji.ttf", size=font_size)

    width, height = 704, 352

    draw = ImageDraw.Draw(image)

    # Randomly select an emoji
    emoji = random.choice(emojis)

    # Random position
    x = random.randint(-100, width)
    y = random.randint(-100, height)

    # Draw the emoji on the image
    draw.text((x, y), emoji, font=font, embedded_color=True)

    # Text settings
    font_color = "white"
    shadow_color = "black"

    font = ImageFont.truetype("MaruBuri-Regular.ttf", font_size)

    _, _, w, h = draw.textbbox((0, 0), text, font=font)

    x = (width - w) / 2
    y = (height - h) / 2

    draw.text(
        (x, y),
        text,
        font=font,
        fill=font_color,
        stroke_width=3,
        stroke_fill=shadow_color,
    )

    image.save(image_path)
