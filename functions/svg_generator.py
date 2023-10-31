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

def hexa_svg(l, img):
    """
    Display the image in an hexagon svg.
    Args:
    - l: (int) length of the hexagons
    - img: (str) path of the image
    Returns:
    - Void, display an svg version of the image, 
    made with haxagones
    """
    origins, coordinates = hexacoor(l, img)
    
    # Get the coordinates of hexagones which will build the image
    hexa_coordinates = coordinates_str(coordinates)

    # Sample the color in the origins 
    colors = get_color(img, origins)
    
    # Creating the HTML file
    file_html = open("../svg_hexagon.html", "w")

    #creating the polygon part in the html writing 
    polygons = ''
    for i in range(len(colors)) : 
        # this will create all the lines of the polygon tag needed to illustrate all the picture with
        # our hexagones
        polygons +=  f'<polygon points="{hexa_coordinates[i]}" \r                fill="{"rgb" + str(colors[i])}"stroke-width="0"/>\n                '
    # Adding the input data to the HTML file
    file_html.write('''<html>
        <head>
            <title>SVG Hexagon </title>
        </head>
        <body>
            <svg height="1920" width="1080">
                {polygons}
            </svg>
        </body>
    </html>'''.format(polygons=polygons))
    # Saving the data into the HTML file
    file_html.close()
    
    
hexa_svg(5, '../screenshot.jpg')

