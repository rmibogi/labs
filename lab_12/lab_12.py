# Вычислить сумму знакопеременного ряда |х^n|/n!, где х-матрица ранга к (к и матрица задаются случайным образом), n - номер слагаемого.
# Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой. У алгоритма д.б. линейная сложность.
# Операция умножения –поэлементная. Знак первого слагаемого  +.

# Импорт необходимых библиотек
import random
import numpy as np
from decimal import Decimal, getcontext


# Определение функции для вычисления суммы знакопеременного ряда
def s_sum(x, t):
    # Задаем базовые параметры
    n = 1  # Номер слагаемого
    curr_x = x  # Текущая матрица
    factorial = 1  # Накопляемый факториал
    res = 0  # Переменная результата
    sign = 1  # Переменная для смены знака

    # Начинаем бесконечный цикл для вычисления ряда
    while True:
        curr_term = Decimal(np.linalg.det(curr_x) / factorial)  # Вычисляем текущий член ряда, преобразовывая его в
        # decimal, что позволяет сохранять числа после запятой, даже при больших значениях самого числа
        res += sign * curr_term  # Прибавляем его к результату с учетом знака для текущего слагаемого

        # Проверяем, достигли ли заданной точности t
        if abs(curr_term) < 1 / (10 ** t):
            break

        # Меняем параметры для следующего слагаемого
        n += 1
        sign = -sign
        factorial *= n
        curr_x *= x

    return res

try:
    # Ввод значения t (количества знаков после запятой)
    print("Введите число t, являющееся количеством знаков после запятой (точностью):")
    t = int(input())
    while t > 300 or t < 1:  # ошибка в случае введения слишком малой точности
        t = int(input("Вы ввели число, неподходящее по условию, введите число t, большее или равное 1:\n"))

    print()

    # Генерация случайного значения k и матрицы x
    k = random.randint(1, 10)
    x = np.random.randint(0, 10, (k, k))

    # Вывод матрицы x
    print("Сгенерированная матрица:")
    print(x)
    print()

    # Установка технической точности вычислений с учетом заданной
    getcontext().prec = t + 100

    # Вызов функции s_sum для вычисления суммы ряда с заданной точностью t
    result = s_sum(x, t)

    # Вывод результата с заданной точностью
    print(f"Сумма ряда с точностью {t} знаков после запятой: {result:.{t}f}".rstrip('0').rstrip('.'))

# Ошибка на случай введения не числа в качестве точности
except ValueError:
    print("\nВведенный символ не является числом. Перезапустите программу и введите число.")