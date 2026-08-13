"""
Functions to determine the type of the triangle
"""

def is_triangle(funct):
    """
    Determine if the basic crieteria for triangles are met or not.

    Parameters:
        sides: The length of sides of the triangle
    
    Return:
        bool: If sides are satisfying the basic crieteria or not
    """

    def inner(sides):
        return sum(sides) > 2 * max(sides) and funct(sides)
    return inner


@is_triangle
def equilateral(sides):
    """
    Determine if the sides are of a equilateral triangle or not.

    Parameters:
        sides: The length of sides of the triangle
    
    Return:
        bool: If sides are of equal length or not
    """

    return len(set(sides)) == 1


@is_triangle
def isosceles(sides):
    """
    Determine if the sides are of a isosceles triangle or not.

    Parameters:
        sides: The length of sides of the triangle
    
    Return:
        bool: If atlease two sides are of same length or not
    """

    return len(set(sides)) < 3


@is_triangle
def scalene(sides):
    """
    Determine if the sides are of a scalene triangle or not.

    Parameters:
        sides: The length of sides of the triangle
    
    Return:
        bool: If sides are of different length or not
    """
    
    return len(set(sides)) == 3
