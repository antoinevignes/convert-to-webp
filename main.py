from PIL import Image
import os

source_dir = os.path.join(os.path.dirname(__file__), "img")


def convert(filepath):
    webp_dir = os.path.join(source_dir, "webp")
    if not (os.path.exists(webp_dir)):
        os.makedirs(webp_dir)

    name = os.path.basename(filepath)
    output_path = os.path.join(webp_dir, os.path.splitext(name)[0] + ".webp")

    img = Image.open(filepath)
    img.save(output_path)


with os.scandir(source_dir) as entries:
    for entry in entries:
        if entry.name != ".DS_Store":
            input_path = os.path.join(source_dir, entry.name)
            if os.path.isfile(input_path):
                convert(input_path)
