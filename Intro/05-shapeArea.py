def shapeArea(n):
    area = 1
    multiplier = 1
    for i in range(n - 1):
        area += 4 * multiplier
        multiplier += 1
    return area
