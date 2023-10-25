# Importing Image from PIL package 
from PIL import Image
 
def get_color(img_path, origins) : 
    # creating an image object
    im = Image.open(rf'{img_path}')
    px = im.load()
    pixels = []
    for coordinate in origins : 
        # using getpixel method
        pixels.append(im.getpixel(coordinate))
    return pixels

