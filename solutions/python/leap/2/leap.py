def leap_year(year):
    """
    Determine if the year is a Leap year or not.

    Parameters:
        year (int) : The given year

    Returns:
        bool: The year given is leap year or not.
        1) The year that is evenly divisible by 4.
        2) Unless the year is evenly divisible by 100, in which case it's only a leap year if the year is also evenly divisible by 400.
    """
    if year % 100:
        if year % 4:
            return False
        return True
    if year % 400:
        return False
    return True
