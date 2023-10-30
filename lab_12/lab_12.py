# Вычислить сумму знакопеременного ряда |х^n|/n!, где х-матрица ранга к (к и матрица задаются случайным образом), n -
# номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой. У
# алгоритма д.б. линейная сложность. Операция умножения –поэлементная. Знак первого слагаемого +.

import random
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

        if abs(curr_term) < 1 / (10 ** t):
            break

    return result

print("Введите число t, являющееся коэффициентом при умножении: ")
t = int(input())
while t > 300 or t < 1:  # ошибка в случае введения слишком малой точности
    t = int(input("Вы ввели число, неподходящее по условию, введите число t, большее или равное 1:\n"))

k = random.randint(1, 10)
x = np.random.randint(0, 10, (k, k))

print(x)
print()

getcontext().prec = t + 100

result = s_sum(x, t)
print(f"Сумма ряда с точностью {t} знаков после запятой: {result:.{t}f}".rstrip('0'))

