# С клавиатуры вводится два числа K и N. Квадратная матрица
# А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E
# заполняется случайным образом целыми числами в интервале
# [-10,10]. Для отладки использовать не случайное заполнение,
# а целенаправленное.

# Формируется матрица F следующим образом: скопировать в нее
# А и если количество нулей в В больше, чем в Е, то поменять в
# ней местами В и С симметрично, иначе В и Е поменять местами
# несимметрично. При этом матрица А не меняется. После чего
# если определитель матрицы А больше суммы диагональных
# элементов матрицы F, то вычисляется выражение: A*AT – K * F,
# иначе вычисляется выражение (A-1 +G-F-1)*K, где G-нижняя
# треугольная матрица, полученная из А. Выводятся по мере
# формирования А, F и все матричные операции последовательно.

#   B   C
#   D   E

import numpy as np

def print_matrix(matrix):                  # функция вывода матрицы
    matrix1 = list(map(list, zip(*matrix)))
    for i in range(len(matrix1)):
        k = len(max(list(map(str, matrix1[i])), key=len))
        matrix1[i] = [f'{elem:{k}d}' for elem in matrix1[i]]
    matrix1 = list(map(list, zip(*matrix1)))
    for row in matrix1:
        print(*row)
    print()

print("Введите число K, являющееся коэффициентом при умножении: ")
k = int(input())
print("Введите число число N, большее или равное 5, являющееся порядком квадратной матрицы: ")
n = int(input())
print()
while n < 5:  # ошибка в случае введения слишком малого порядка матрицы
    n = int(input("Вы ввели число, неподходящее по условию, введите число N, большее или равное 5:\n"))

np.set_printoptions(linewidth=1000)

# Создание и заполнение матрицы A
A = np.random.randint(-10.0, 10.0, (n, n))
print("Матрица A:")
print_matrix(A)

# Создание подматриц
submatrix_length = n//2
sub_matrix_B = np.array(A[:submatrix_length, :submatrix_length])
sub_matrix_C = np.array(A[:submatrix_length, submatrix_length+n % 2:n])
sub_matrix_E = np.array(A[submatrix_length+n % 2:n, submatrix_length+n % 2:n])

# Создание матрицы F
F = A.copy()
print("Матрица F:")
print_matrix(F)

# Обработка матрицы B и E
zero_counter_B = np.count_nonzero(sub_matrix_B == 0)  # счетчик нулей подматрицы B матрицы F
zero_counter_E = np.count_nonzero(sub_matrix_E == 0)  # счетчик нулей подматрицы E матрицы F

print("Подматрица B:")
print_matrix(sub_matrix_B)
print(zero_counter_B)
print()
print("Подматрица E:")
print_matrix(sub_matrix_E)
print(zero_counter_E)
print()

# Формируем матрицу F
if zero_counter_B > zero_counter_E:
    F[:submatrix_length, submatrix_length+n % 2:n] = sub_matrix_B[:submatrix_length, ::-1]
    F[:submatrix_length, :submatrix_length] = sub_matrix_C[:submatrix_length, ::-1]
else:
    F[:submatrix_length, :submatrix_length] = sub_matrix_E
    F[submatrix_length+n % 2:n, submatrix_length+n % 2:n] = sub_matrix_B

print("Отформатированная матрица F:")
print_matrix(F)
print()

try:
    if