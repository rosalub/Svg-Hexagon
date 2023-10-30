"""Functions that cover the tesselation"""

import math 
from PIL import Image, ImageDraw 
import numpy as np

def hexadots(l,origins):
    """Given an origin, defines the point to design a hexagon.
    Args:
    - l: (int) length of the hexagon
    - origins: (list) list of x and y corresponding to the center of the hexagon
    Returns:
    - L: All the 6 coordinates needed to draw a hexagon
    """
    
    if type(l) is not int:
        raise ValueError("l must be an integer")

    L = list()
    res = list()
    for o in origins:
        x = o[0]
        y = o[1]
        half = int((l/2))
        res = [(x,y-l),(x+l,y-half),(x+l,y+half),(x,y+l),(x-l,y+half),(x-l,y-half),(x,y-l)]
        L.append(res)
        res = list()
    return L

def hexacoor(l, img):
    """
    Return coordinates of each points of the 
    hexagones of width l which will fill our image.
    Args:
    - l: (int) length of the hexagon
    - img: (str) path of the image
    Returns:
    - origins : (list) coordinates of each hexagone's origins
    - coord : (list) tuples of coordinates for the 
            points within lists for each hexagone
    """

    if type(l) is not int:
        raise ValueError("l must be an integer")
    if type(img) is not str:
        raise ValueError("Please put the path of the image")

    #Going throw all the origins given a length for every hexagon:
    image = Image.open(img)
    width, height = image.size
    xs = list()
    ys = list()
    k = 0
    for y in range(l,height, int(1.5*l)):
        if k % 2 == 0:
            k += 1
            for x in range(int(l), width, 2*l):
                xs.append(x)
                ys.append(y)
        else:
            k += 1
            for x in range(0, width, 2*l):
                xs.append(x)
                ys.append(y)
                
    # ------------------------------------------------------------  
    #Aggregating all our origins in a list of tuples
    origins = list(zip(xs,ys))
    
    # ------------------------------------------------------------
    #Deducing all the points that form a hexagon from our origins and draw them on the image:
    coord = hexadots(l,origins)
    return origins, coord


def hexatess(l, img):
    """Tesselates a given picture by hexagons
    Args:
    - l: (int) length of the hexagon
    - img: (str) path of the image
    Returns:
    - Void, display the image filled with hexagons
    """

    coord = hexacoor(l, img)
    with Image.open("screenshot.jpg") as im:
        draw = ImageDraw.Draw(im) 
        for i in coord:
            shape = i
            draw.line(shape, width = 0) 
    im.save("hexagon.png")
    im.show()
    
