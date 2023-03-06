from math import floor
import random

def print_matrix(matrix):
    print('\n'.join('\t'.join(map(str, row)) for row in matrix))

try:
    print("Введите число K, являющееся коэффициентом при умножении: ")
    k = 2#int(input())
    print("Введите число число N, большее 5, являющееся размером квадратной матрицы: ")
    n = 8#int(input())
    while n < 5:
        n = int(input("Вы ввели число, неподходящее по условию, введите число N, большее 5:\n"))

    print("Матрица А изначальная:")

    matrix_A = [[i for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            matrix_A[i][j] = random.randint(-10, 10)

    print_matrix(matrix_A)
    print()

    matrix_A_dump = [[elem for elem in raw] for raw in matrix_A]
    matrix_A_trans = [[0 for i in range(n)] for j in range(n)]

    print("Матрица A транспонированная:")

    for i in range(n):
        for j in range(n):
            matrix_A_trans[i][j] = matrix_A_dump[j][i]

    print_matrix(matrix_A_trans)
    print()

    print("Матрица F изначально равная матрице A:")

    matrix_F = [[elem for elem in raw] for raw in matrix_A]

    print_matrix(matrix_F)
    print()

    print("Элемент B матрицы F:")

    matrix_F_B = [[0 for i in range(floor(n/2))] for j in range(floor(n/2))]

    for i in range(floor(n/2)):
        for j in range(floor(n/2)):
            matrix_F_B[i][j] = matrix_F[i][j]

    print_matrix(matrix_F_B)
    print()

    zero_counter_1 = 0
    zero_counter_3 = 0
    n_B = floor(n/2)

    for i in range(n_B):
        for j in range(n_B):
            if ((i + j + 1) <= n_B) and (i >= j) and matrix_F_B[i][j] == 0:
                zero_counter_1 += 1

    for i in range(n_B):
        for j in range(n_B):
            if (i <= j) and ((i + j + 1) >= n_B) and matrix_F_B[i][j] == 0:
                zero_counter_3 += 1

    matrix_F_B_dump = [[elem for elem in raw] for raw in matrix_F_B]

    if zero_counter_1 > zero_counter_3:
        for i in range(n_B):
            for j in range(n_B):
                if (i < j) and ((i + j + 1) < n_B):
                    matrix_F_B[i][j] = matrix_F_B_dump[n_B - i - 1][j]
                    matrix_F_B[n_B - i - 1][j] = matrix_F_B_dump[i][j]

    print("Матрица F, сформированная:")

    matrix_F_dump = [[elem for elem in raw] for raw in matrix_F]

    if zero_counter_1 > zero_counter_3:
        for i in range(floor(n/2)):
            for j in range(floor(n/2)):
                if (i < j) and ((i + j + 1) < floor(n/2)):
                    matrix_F[i][j] = matrix_F_dump[floor(n/2) - i - 1][j]
                    matrix_F[floor(n/2) - i - 1][j] = matrix_F_dump[i][j]
    else:
        for i in range(floor(n/2)):
            for j in range(floor(n/2)):
                matrix_F[i][j] = matrix_F_dump[floor(n/2) + i][floor(n/2) + j]
                matrix_F[floor(n/2) + i][floor(n/2) + j] = matrix_F_dump[i][j]

    print_matrix(matrix_F)
    print()

    print("Результат умножения матрицы A на транспонированную матрицу A:")

    matrix_A_multiplied = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix_A_multiplied[i][j] += matrix_A[i][k] * matrix_A_trans[k][j]

    print_matrix(matrix_A_multiplied)
    print()

    print("Результат умножения матрицы F на коэффициент K:")

    matrix_F_multiplied = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            matrix_F_multiplied[i][j] = k * matrix_F[i][j]

    print_matrix(matrix_F_multiplied)
    print()

    print("Результат разности между результатом умножения матрицы A и результатом умножения матрицы F:")

    matrix_C_result = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            matrix_C_result[i][j] = matrix_A_multiplied[i][j] - matrix_F_multiplied[i][j]

    print_matrix(matrix_C_result)
    print()

except ValueError:
    print("\nВведенный символ не является числом.")