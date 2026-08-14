def score(x, y):
    distance = x**2+y**2
    if distance <=1:
        return 10
    if distance <= 25:
        return 5
    if distance <=100:
        return 1
    return 0