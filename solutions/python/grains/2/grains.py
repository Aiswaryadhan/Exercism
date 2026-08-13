"""
Functions to check the number of grains in the chess board
"""
def square(number):
    """
    Determine the number of grains in the particular square of the chessboard

    Parameters:
        number (int): Number of the sqaure on chessboard

    Returns:
        int: number of grains in the particular square
        ValueError: When the square number provided is <= 0 or >64
    """

    if number<=0 or number>64:
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        return 1
    return 2 * square(number - 1)


def total():
    """
    Determine the total number of grains in the chessboard

    Returns:
        int: Total number of grains in the chessboard
    """
        
    total_grains = 0
    for number in range(1, 65):
        total_grains += square(number)
    return total_grains
