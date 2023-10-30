"""Testing the python files in functions folder"""

from functions.tesselate import hexadots, hexatess
from functions.hexagon_color import get_color 

def test_hexadots():
    """Define the test function
    Args: None
    Returns: None"""
    assert hexadots(5, [(10,10)]) == [[(10, 5), (15, 8), (15, 12), (10, 15), (5, 12), (5, 8), (10, 5)]]
    with pytest.raises(ValueError):
        hexadots("This is a string", [(10,10)])

def test_hexatess():
    with pytest.raises(ValueError):
        hexatess("This is a string", "screenshot.jpg")
        hexatess(5, 10)

def test_get_color():
    assert get_color('screenshot.jpg', [(10, 5), (15, 8), (15, 12), (10, 15), (5, 12), (5, 8), (10, 5)]) == [(24, 195, 239), (25, 193, 240), (25, 193, 242), (25, 193, 240), (24, 195, 241), (23, 196, 238), (24, 195, 239)]
