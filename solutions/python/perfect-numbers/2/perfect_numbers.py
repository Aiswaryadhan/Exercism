import math

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    factors = find_factors(number)
    factors.remove(number)
    sum_factors = sum(factors)

    if number == sum_factors:
        return "perfect"
    if number < sum_factors:
        return "abundant"
    if number > sum_factors:
        return "deficient" 
    return None


def find_factors(number):
    factors = set()
    for num in range(1, math.isqrt(number)+1):
        if number % num == 0:
            factors.add(num)
            factors.add(number//num)
    return factors