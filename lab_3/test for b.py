from math import floor
import random

def print_matrix(matrix):
    print('\n'.join('\t'.join(map(str, row)) for row in matrix))

zero_counter_1 = 0
zero_counter_3 = 0

n = 5

matrix_F = [[i for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        matrix_F[i][j] = random.randint(-10, 10)

print_matrix(matrix_F)
print()

for i in range(n):
    for j in range(n):
        if ((i+j+1) <= n) and (i >= j) and matrix_F[i][j] == 0:
            zero_counter_1 += 1

for i in range(n):
    for j in range(n):
        if (i <= j) and ((i + j + 1) >= n) and matrix_F[i][j] == 0:
            zero_counter_3 += 1

matrix_F_dump = [[elem for elem in raw] for raw in matrix_F]

print(zero_counter_1, zero_counter_3)

if zero_counter_1 > zero_counter_3:
    for i in range(floor(n)):
        for j in range(floor(n)):
            if (i < j) and ((i + j + 1) < n):
                matrix_F[i][j] = matrix_F_dump[floor(n) - i - 1][j]
                matrix_F[floor(n) - i - 1][j] = matrix_F_dump[i][j]

print_matrix(matrix_F)

k = 2

matrix_F_multiplied = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        matrix_F_multiplied[i][j] = k * matrix_F[i][j]

print_matrix(matrix_F_multiplied)
print()