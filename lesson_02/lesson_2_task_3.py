import math


def square(side):
    area = side * side
    if area == float(area):
        return math.ceil(area)
    else:
        return area


side_len = 2.1
result = square(side_len)
print(f"Площадь квадрата со стороной {side_len} равна {result}")
