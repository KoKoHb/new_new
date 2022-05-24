# Write a function that accepts two parameters (sum and multiply) and find two numbers [x, y],
# where x + y = sum and x * y = multiply.
# Example:
# sum = 12 and multiply = 32
# In this case, x equals 4 and y equals 8.
# x = 4
# y = 8
# Because
# x + y = 4 + 8 = 12 = sum
# x * y = 4 * 8 = 32 = multiply
# The result should be [4, 8].
# Note:
# 0 <= x <= 1000
# 0 <= y <= 1000
# If there is no solution, your function should return null (or None in python).
# You should return an array (list in python) containing the two values [x, y]
# and it should be sorted in ascending order.
# One last thing: x and y are integers (no decimals).

def sum_and_multiply_my(sum, multiply):
    s = []
    for i in range(sum + 1):
        for j in range(i, sum + 1):
            if j + i == sum and j * i == multiply:
                s.append(i)
                s.append(j)
                break
    if len(s) < 2:
        return None
    t = []
    t.append(min(s))
    t.append(max(s))
    return t


def sum_and_multiply(sum, multiply):
    for x in range(sum + 1):
        if x * (sum - x) == multiply:
            return [x, sum - x]


print(sum_and_multiply(50, 0))
