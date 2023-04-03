import time
import matplotlib.pyplot as plt

def recursive_f(n):
    if n < 2:
        return 1
    else:
        return 2 * recursive_f(n-1) + recursive_f(n-3)

def iterative_f(n):
    if n < 2:
        return 1
    f0, f1, f2 = 1, 1, 3
    for i in range(3, n + 1):
        fn = 2 * f2 + f0
        f0, f1, f2 = f1, f2, fn
    return fn if n > 2 else f2

try:
    print("Введите число n, являющееся входным числом для функции F(x<2) = 1; F(n) = 2F(n-1) + F(n-3): ")
    n = int(input())
    while n < 1:  # ошибка в случае введения слишком малого порядка матрицы
        n = int(input("\nВы ввели не натуральное число, функция определенна лишь в области натуральных чисел. Введите натуральное число:\n"))

    if n > 100000:
        print("\nРабота программы может занять существенное время, ожидайте...")

    start = time.time()
    result = iterative_f(n)
    end = time.time()
    print("\nРезультат работы итерационного подхода:", result, "\nВремя работы:", end - start)

    if 40 < n < 100000:
        print("\nРабота рекурсивного подхода может занять существенное время, ожидайте...")

    start = time.time()
    result = recursive_f(n)
    end = time.time()
    print("\nРезультат работы рекурсивного подхода:", result, "\nВремя работы:", end - start)

    print("\nПрограмма формирует сравнительную таблицу и графики времени вычисления рекурсивным и итерационным подходом для n чисел, ожидайте...\n")

    recursive_times = []
    recursive_values = []
    iterative_times = []
    iterative_values = []
    n_values = list(range(1, n + 1))

    for n in n_values:
        start = time.time()
        recursive_values.append(recursive_f(n))
        end = time.time()
        recursive_times.append(end - start)

        start = time.time()
        iterative_values.append(iterative_f(n))
        end = time.time()
        iterative_times.append(end - start)

    table_data = []
    for i, n in enumerate(n_values):
        table_data.append([n, recursive_times[i], iterative_times[i], recursive_values[i], iterative_values[i]])

    print('{:<7}|{:<22}|{:<22}|{:<22}|{:<22}'.format('n', 'Время рекурсии (с)', 'Время итерации (с)', 'Значение рекурсии', 'Значение итерации'))
    print('-' * 110)
    for data in table_data:
        print('{:<7}|{:<22}|{:<22}|{:<22}|{:<22}'.format(data[0], data[1], data[2], data[3], data[4]))

    plt.plot(n_values, recursive_times, label='Рекурсия')
    plt.plot(n_values, iterative_times, label='Итерация')
    plt.xlabel('n')
    plt.ylabel('Время (с)')
    plt.title('Сравнение рекурсивного и итерационного подхода')
    plt.legend()
    plt.show()

    print("\nРабота программы завершена.\n")

except ValueError:
    print("\nВы ввели не натуральное число, функция определенна лишь в области натуральных чисел. Перезапустите программу и введите натуральное число.")

except RecursionError:
    print("\nВы превысили относительную максимальную глубину рекурсии. Перезапустите программу и введите меньшее число, если хотите получать результат работы рекурсивного подхода и сравнительную таблицу.")
