from tesselate import hexacoor, hexadots
from hexagon_color import get_color

def coordinates_str(coordinates):
    """
    Convert the lists of coordinates in an str list 
    to match with the arguments expected by the polygon method 
    of svg. 
    Args:
    - coordinates : list) tuples of coordinates for the 
            points within lists for each hexagone
    Return : 
    - coor : the converted list
    """

    coor = []
    for hexagon in coordinates : 
        coordinates_str = ""
        for i in range(6) : # no need to add the coordinates of the first point 
                                # to "close" the polygon
            coordinates_str += str(hexagon[i][0]) + " "
            coordinates_str += str(hexagon[i][1]) + ","
        coordinates_str = coordinates_str[:-1] 
        coor.append(coordinates_str)
    return coor

############################################### DRAFT 
def hexa_svg(l, img):
    """
    Display the image in an hexagon svg.
    Args:
    - l: (int) length of the hexagons
    - img: (str) path of the image
    Returns:
    - Void, display the image filled with hexagons
    """
    # Keep the list of origines (for color)
    # and the list of coordinates of the 6 points 
    # of each haxagone :
    origins, coordinates = hexacoor(l, img)

    # Sample the color in the origins 
    colors = get_color(img, origins)
    
    # Creating the HTML file
    file_html = open("svg_hexagon.html", "w")
    # Adding the input data to the HTML file
    file_html.write('''<html>
        <head>
            <title>SVG Hexagon </title>
        </head>
        <body>
            <svg height=l width=l
                <polygon points="50 3,100 28,100 75,50 100,
                3 75,3 25"
                stroke="black"
                fill="yellow" stroke-width="5" />
            </svg>
        </body>
    </html>''')
    # Saving the data into the HTML file
    file_html.close()