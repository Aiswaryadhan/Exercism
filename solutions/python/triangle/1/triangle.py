"""
Functions to determine the type of the triangle
"""

def is_triangle(sides):
    """
    Determine if the basic crieteria for triangles are met or not.

    Parameters:
        sides: The length of sides of the triangle
    
    Return:
        bool: If sides are satisfying the basic crieteria or not
    """

    a, b, c = sides
    if 0 not in sides:
        if a + b >= c:
            if b + c >= a:
                if c + a >= b:
                    return True
    return False


def equilateral(sides):
    """
    Determine if the sides are of a equilateral triangle or not.

    Parameters:
        sides: The length of sides of the triangle
    
    Return:
        bool: If sides are of equal length or not
    """

    if is_triangle(sides):
        a, b, c = sides
        return a==b==c
    return False


def isosceles(sides):
    """
    Determine if the sides are of a isosceles triangle or not.

    Parameters:
        sides: The length of sides of the triangle
    
    Return:
        bool: If atlease two sides are of same length or not
    """

    if is_triangle(sides):
        a, b, c = sides
        return a==b or b==c or a==c
    return False


def scalene(sides):
    """
    Determine if the sides are of a scalene triangle or not.

    Parameters:
        sides: The length of sides of the triangle
    
    Return:
        bool: If sides are of different length or not
    """
    
    if is_triangle(sides):
        a, b, c = sides
        return a!=b and a!=c and b!=c
    return False

