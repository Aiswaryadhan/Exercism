"""
Function to determine if the given number is amstrong or not
"""
def is_armstrong_number(number):
    """
    Determine if the given number is amstrong or not

    Parameters:
        number (int): Number to find if amstrong or not

    Return:
        bool: True if number is an amstrong number, False otherwise
    """

    number_length = len(str(number))
    digit_sum = 0
    for digit in str(number):
        digit_sum += int(digit) ** number_length
    return digit_sum == number
