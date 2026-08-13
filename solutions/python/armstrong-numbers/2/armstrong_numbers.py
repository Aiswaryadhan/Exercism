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
    num = number
    digit_sum = 0
    while num > 0:
        num_digit = num % 10
        digit_sum += num_digit**number_length
        num = num//10
    return digit_sum == number
