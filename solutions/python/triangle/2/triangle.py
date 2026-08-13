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

    side_1, side_2, side_3 = sides
    if 0 not in sides:
        if side_1 + side_2 >= side_3:
            if side_2 + side_3 >= side_1:
                if side_3 + side_1 >= side_2:
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
        side_1, side_2, side_3 = sides
        return side_1==side_2==side_3
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
        side_1, side_2, side_3 = sides
        return side_1==side_2 or side_2==side_3 or side_1==side_3
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
        side_1, side_2, side_3 = sides
        return side_1!=side_2 and side_1!=side_3 and side_2!=side_3
    return False
