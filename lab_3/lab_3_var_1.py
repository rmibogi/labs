# С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E
# заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное.

# Формируется матрица F следующим образом: если количество нулей в В в области 1 больше, чем в области 3, то поменять в ней
# симметрично области 2 и 4 местами, иначе В и Е поменять местами несимметрично. При этом матрица А не меняется. После чего
# вычисляется выражение: A * AT – K * F. Выводятся по мере формирования А, F и все матричные операции последовательно.

#                       2
#   B   C           1       3
#   D   E               4

from math import ceil, floor
import random

def print_matrix(matrix):                  # функция вывода матрицы
    matrix1 = list(map(list, zip(*matrix)))
    for i in range(len(matrix1)):
        k = len(max(list(map(str, matrix1[i])), key=len))
        matrix1[i] = [f'{elem:{k}d}' for elem in matrix1[i]]
    matrix1 = list(map(list, zip(*matrix1)))
    for row in matrix1:
        print(*row)
    print()

try:
    print("Введите число K, являющееся коэффициентом при умножении: ")
    k = int(input())
    print("Введите число число N, большее или равное 5, являющееся порядком квадратной матрицы: ")
    n = int(input())
    print()
    while n < 5:        # ошибка в случае введения слишком малого порядка матрицы
        n = int(input("Вы ввели число, неподходящее по условию, введите число N, большее или равное 5:\n"))

    print("Матрица А изначальная:")

    matrix_A = [[random.randint(-10, 10) for i in range(n)] for j in range(n)]    # создаем матрицу размером nxn, заполненную случайными числами

    #matrix_A = [[i+j*n for i in range(n)] for j in range(n)]        # задание матрицы для тестирования

    print_matrix(matrix_A)          # вывод матрицы A

    matrix_A_dump = [[elem for elem in raw] for raw in matrix_A]        # резервная копия матрицы A для дальнейших операций
    matrix_A_trans = [[0 for i in range(n)] for j in range(n)]          # заготовка под транспонированную матрицу A

    print("Матрица A транспонированная:")

    for i in range(n):              # произведение транспонирования матрицы A
        for j in range(n):
            matrix_A_trans[i][j] = matrix_A_dump[j][i]

    print_matrix(matrix_A_trans)        # вывод транспонированной матрицы A

    print("Матрица F изначально равная матрице A:")

    matrix_F = [[elem for elem in raw] for raw in matrix_A]         # создание матрицы F, на данный момент равной матрице A

    print_matrix(matrix_F)          # вывод матрицы F

    print("Элемент B матрицы F:")

    matrix_F_B = [[0 for i in range(ceil(n/2))] for j in range(ceil(n/2))]      # заготовка под отдельную подматрицу B матрицы F

    for i in range(ceil(n/2)):      # копирование элементов подматрицы B матрицы F в отдельную матрицу B
        for j in range(ceil(n/2)):
            matrix_F_B[i][j] = matrix_F[i][j]

    print_matrix(matrix_F_B)        # вывод элемента B матрицы F

    zero_counter_1 = 0      # счетчик нулей в области 1 подматрицы B матрицы F
    zero_counter_3 = 0      # счетчик нулей в области 3 подматрицы B матрицы F
    n_B = ceil(n/2)         # порядок подматрицы B

    for i in range(n_B):
        for j in range(n_B):
            if ((i + j + 1) <= n_B) and (i >= j) and matrix_F_B[i][j] == 0:     # считаем нули в области 1, используя формулы главной и побочной диагонали
                zero_counter_1 += 1

    for i in range(n_B):
        for j in range(n_B):
            if (i <= j) and ((i + j + 1) >= n_B) and matrix_F_B[i][j] == 0:     # считаем нули в области 3, используя формулы главной и побочной диагонали
                zero_counter_3 += 1

    print("Количество нулей в области 1 в подматрице B:", zero_counter_1, "\nКоличество нулей в области 3 в подматрице B:", zero_counter_3)

    matrix_F_dump = [[elem for elem in raw] for raw in matrix_F]        # резервная копия матрицы F для дальнейших операций

    if zero_counter_1 > zero_counter_3:         # проверка условия, если нулей в области 1 больше, чем в области 3, меняем симметрично области 2 и 4 местами
        print("\nКоличество нулей в области 1 больше, чем в области 3, меняем области 2 и 4 симметрично местами.\n")
        for i in range(ceil(n/2)):
            for j in range(ceil(n/2)):
                if (i < j) and ((i + j + 1) < ceil(n/2)):
                    matrix_F[i][j] = matrix_F_dump[ceil(n/2) - i - 1][j]
                    matrix_F[ceil(n/2) - i - 1][j] = matrix_F_dump[i][j]
    else:                                                                       # иначе, меняем B и E местами несимметрично, если порядок изначальной матрицы нечетный центральный элемент также меняем
        print("\nКоличество нулей в области 1 меньше или равно количеству нулей в области 3, меняем области B и E местами несимметрично.\nЕсли порядок матрицы нечетный, центральный элемент также меняется.\n")
        for i in range(ceil(n/2)):
            for j in range(ceil(n/2)):
                matrix_F[i][j] = matrix_F_dump[floor(n/2) + i][floor(n/2) + j]
                matrix_F[floor(n/2) + i][floor(n/2) + j] = matrix_F_dump[i][j]

    print("Матрица F, сформированная:")

    print_matrix(matrix_F)          # выводим уже сформированную матрицу F

    print("Результат умножения матрицы A на транспонированную матрицу A:")

    matrix_A_multiplied = [[0 for i in range(n)] for j in range(n)]      # заготовка под результат умножения матрицы A на транспонированную матрицу A

    for i in range(n):              # производим умножение двух матриц друг на друга
        for j in range(n):
            for l in range(n):
                matrix_A_multiplied[i][j] += matrix_A[i][l] * matrix_A_trans[l][j]

    print_matrix(matrix_A_multiplied)          # выводим результат умножения

    print("Результат умножения матрицы F на коэффициент K:")

    matrix_F_multiplied = [[0 for i in range(n)] for j in range(n)]      # заготовка под результат умножения матрицы F на коэффициент K

    for i in range(n):          # производим умножение матрицы на коэффициент
        for j in range(n):
            matrix_F_multiplied[i][j] = k * matrix_F[i][j]

    print_matrix(matrix_F_multiplied)          # выводим результат умножения

    print("Конечный результат разности между результатом умножения матрицы A*AT и результатом умножения матрицы F*K:")

    matrix_C_result = [[0 for i in range(n)] for j in range(n)]      # заготовка под конечный результат разности двух последних вычисленных слагаемых

    for i in range(n):              # производим разность между двумя матрицами
        for j in range(n):
            matrix_C_result[i][j] = matrix_A_multiplied[i][j] - matrix_F_multiplied[i][j]

    print_matrix(matrix_C_result)          # выводим конечный результат работы программы

    print("Работа программы завершена.")

except ValueError:                                      # ошибка на случай введения не числа в качестве порядка или коэффициента
    print("\nВведенный символ не является числом. Перезапустите программу и введите число.")