#Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно
#и итерационно. Определить границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить
#в табличной и графической форме.

#F(x<2) = 1; F(n) = 2F(n-1) + F(n-3)

import time
import matplotlib.pyplot as plt

def recursive_f(n):         # рекурсивное решение
    if n < 2:
        return 1
    else:
        return 2 * recursive_f(n-1) + recursive_f(n-3)

def iterative_f(n):
    fn = [1] * (n + 1)
    for i in range(2, n + 1):
        fn[i] = 2 * fn[i-1] + fn[i-3]
    return fn[n]

try:
    print("Введите натуральное число n, являющееся входным для функции F(x<2) = 1; F(n) = 2F(n-1) + F(n-3),\nи на основе которого будет строиться сравнительная таблица: ")
    n = int(input())
    while n < 1:  # ошибка в случае введения не натурального числа
        n = int(input("\nВы ввели не натуральное число, функция определенна лишь в области натуральных чисел. Введите натуральное число:\n"))

    if n > 100000:
        print("\nРабота программы может занять существенное время, ожидайте...")

    start = time.time()         # счетчик времени и результат работы итерационного подхода
    result = iterative_f(n)
    end = time.time()
    print("\nРезультат работы итерационного подхода:", result, "\nВремя работы:", end - start)

    k = 1
    if n > 40:
        k = int(input(
            "\nЧисло n > 40, вы хотите получить результат работы рекурсивного подхода? Это может занять существенное время. (Да: 1 / Нет: 0):\n"))
    while k != 0 and k != 1:
        k = int(input("\nВы ввели не 1 и не 0. Введите 1, чтобы продолжить или 0, чтобы завершить программу:\n"))

    if k == 1:
        if 40 < n < 100000:
            print("\nРабота рекурсивного подхода может занять существенное время, ожидайте...")

        start = time.time()         # счетчик времени и результат работы рекурсивного подхода
        result = recursive_f(n)
        end = time.time()
        print("\nРезультат работы рекурсивного подхода:", result, "\nВремя работы:", end - start)

    if n > 40 and k != 0:
        k = int(input("\nЧисло n > 40, вы хотите сделать сравнительную таблицу? Это может занять существенное время. (Да: 1 / Нет: 0):\n"))
    while k != 0 and k != 1:
        k = int(input("\nВы ввели не 1 и не 0. Введите 1, чтобы продолжить или 0, чтобы завершить программу:\n"))

    if k == 1:
        print("\nПрограмма формирует сравнительную таблицу и графики времени вычисления рекурсивным и итерационным подходом для n чисел, ожидайте...\n")

        recursive_times = []                # создание списков для дальнейшего построения таблицы
        recursive_values = []
        iterative_times = []
        iterative_values = []
        n_values = list(range(1, n + 1))

        for n in n_values:                  # заполнение списков данными
            start = time.time()
            recursive_values.append(recursive_f(n))
            end = time.time()
            recursive_times.append(end - start)

            start = time.time()
            iterative_values.append(iterative_f(n))
            end = time.time()
            iterative_times.append(end - start)

        table_data = []             # создание и заполнение последующей таблицы
        for i, n in enumerate(n_values):
            table_data.append([n, recursive_times[i], iterative_times[i], recursive_values[i], iterative_values[i]])

        print('{:<7}|{:<22}|{:<22}|{:<22}|{:<22}'.format('n', 'Время рекурсии (с)', 'Время итерации (с)', 'Значение рекурсии', 'Значение итерации'))        # вывод таблицы
        print('-' * 110)
        for data in table_data:
            print('{:<7}|{:<22}|{:<22}|{:<22}|{:<22}'.format(data[0], data[1], data[2], data[3], data[4]))

        print("\nВсе дальнейшие выводы основаны на результатах, полученных на изначально тестируемом компьютере:"
              "\nРекурсивный подход перестает работать при n равном 999 и больше. Уже для n равного 42, рекурсивный подход\n"
              "начинает работать дольше секунды, а график времени его работы растет экспоненциально, что говорит о его неэффективности для вычисления данной\n"
              "реккурентной функции. В то же время итерационный подход сохраняет скорость работы меньше секунды, даже для n равного 180000,\n"
              "что говорит о его высокой эффективности и применимости даже для больших чисел.")

        plt.plot(n_values, recursive_times, label='Рекурсия')           # вывод графиков
        plt.plot(n_values, iterative_times, label='Итерация')
        plt.xlabel('n')
        plt.ylabel('Время (с)')
        plt.title('Сравнение рекурсивного и итерационного подхода')
        plt.legend()
        plt.show()

    print("\nРабота программы завершена.\n")

except ValueError:
    print("\nВы ввели число, не следуя условиям. Перезапустите программу и введите число, следуя инструкциям.")

except RecursionError:
    print("\nВы превысили относительную максимальную глубину рекурсии. Перезапустите программу и введите меньшее число, если хотите получать результат работы рекурсивного подхода и сравнительную таблицу.")