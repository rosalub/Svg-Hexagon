"""Testing the tesselate.py functions"""

from hexagon_shaping.tesselate import hexadots, hexatess

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
        