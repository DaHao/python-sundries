"""
It's a exercise of python 'How to Think Like a Computer Scientist
Link: http://www.openbookproject.net/thinkcs/python/english2e/ch05.html
"""
def compare(a, b):
    """
        >>> compare(5, 4)
        1
        >>> compare(7, 7)
        0
        >>> compare(2, 3)
        -1
        >>> compare(42, 1)
        1
    """
    return 0 if a == b else ( 1 if a > b else -1)

def hypotenuse(a, b):
    """
        >>> hypotenuse(3,4)
        5.0
        >>> hypotenuse(12, 5)
        13.0
        >>> hypotenuse(7, 24)
        25.0
        >>> hypotenuse(9, 12)
        15.0
    """
    return (a**2 + b**2)**0.5

def slope(x1, y1, x2, y2):
    """
        >>> slope(5, 3, 4, 2)
        1.0
        >>> slope(1, 2, 3, 2)
        0.0
        >>> slope(1, 2, 3, 3)
        0.5
        >>> slope(2, 4, 1, 2)
        2.0
    """
    if not x1 - x2: return 0.0
    result = (y1 - y2) / (x1 - x2)
    return 0.0 if result == 0.0 else result 


if __name__ == '__main__':
    import doctest
    doctest.testmod()
