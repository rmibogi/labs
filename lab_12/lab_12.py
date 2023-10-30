import numpy as np
import math
from decimal import Decimal, getcontext

def s_sum(x, t):
    n = 1
    curr_x = x
    factorial = 1
    result = 0
    sign = 1

    while True:
        curr_term = Decimal(np.linalg.det(curr_x) / factorial)
        result += sign * curr_term
        n += 1
        sign = -sign
        factorial *= n
        curr_x *= x

        print(curr_term, result)

        if abs(curr_term) < 1 / (10 ** t):
            break

    return result

k = 3
t = 6
x = np.random.randint(0, 10, (k, k))

print(x)
print()

getcontext().prec = t ** 10

result = s_sum(x, t)
print(f"Сумма ряда с точностью {t} знаков после запятой: {result:.{t}f}")
