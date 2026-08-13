def leap_year(year):
    if year % 100:
        if year % 4:
            return False
        return True
    if year % 400:
        return False
    return True
