"""
Function to find the number of steps it takes to reach 1 
according to the rules of the Collatz Conjecture
"""

def steps(number):
    """
    Determine the number of steps to reach 1

    Parameters:
        number (int): The number to find the steps to reach 1
    
    Return:
        int: Number of steps taken to reach 1
    """
    steps_taken = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while number > 1:
        number = number/2 if number%2 == 0 else number*3+1 
        steps_taken += 1
    return steps_taken