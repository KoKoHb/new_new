from math import *
def is_square(n):
    if n < 0 or sqrt(n) % 1 != 0:
        return False
    else:
        return True

print(is_square(5))