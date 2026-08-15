import re
def is_valid(isbn):
    sum_digits = 0
    if "-" in isbn:
        regex_pattern = re.compile(r'^\d-\d{3}-\d{5}-[\dXx]$')
        print(regex_pattern.match(isbn)==True)
        if not regex_pattern.match(isbn):
            return False
        isbn = isbn.replace("-", "")

    if not len(isbn) == 10:
        return False
            
    for i in range(1, len(isbn)+1):
        char = isbn[-1]
        if char == "X":
            val_char = 10
        elif not char.isdigit():
            return False
        else:
            val_char = int(char)
        isbn = isbn[:-1]
        sum_digits += val_char*i
    
    if sum_digits % 11== 0:
        return True
    return False
