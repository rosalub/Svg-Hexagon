# Importing Image from PIL package 
from PIL import Image
 
def get_color(img_path, origins) : 
    """
    Take an image and a list of coordinates and return 
    the color of the associated pixels  

    Args :
    - img_path : (str) path of the image file
    - origins : (list) tuples associated to coordinates 

    Returns :
    - pixels : (list) list of the color of each pixels 
    """
    # creating an image object
    im = Image.open(rf'{img_path}')
    px = im.load()
    pixels = []
    for coordinate in origins : 
        # using getpixel method
        pixels.append(im.getpixel(coordinate))
    return pixels

