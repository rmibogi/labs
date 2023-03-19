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

import random
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

try:
    print("Введите число K, являющееся коэффициентом при умножении: ")
    k = int(input())
    print("Введите число число N, большее 5, являющееся порядком квадратной матрицы: ")
    n = int(input())
    print()
    while n <= 5:  # ошибка в случае введения слишком малого порядка матрицы
        n = int(input("Вы ввели число, неподходящее по условию, введите число N, большее или равное 5:\n"))

    np.set_printoptions(linewidth=1000)

    # Создание и заполнение матрицы A
    A = np.random.randint(-10.0, 10.0, (n, n))
    print("Матрица A:\n", A)

    # Создание подматриц
    submatrix_length = n//2
    sub_matrix_B = np.array(A[:submatrix_length, :submatrix_length])
    sub_matrix_C = np.array(A[:submatrix_length, submatrix_length+n % 2:n])
    sub_matrix_E = np.array(A[submatrix_length+n % 2:n, submatrix_length+n % 2:n])

    # Создание матрицы F
    F = A.copy()
    print("Матрица F:\n", F)

    # Обработка матрицы B и E
    zero_counter_B = np.count_nonzero(sub_matrix_B == 0)  # счетчик нулей подматрицы B матрицы F
    zero_counter_E = np.count_nonzero(sub_matrix_E == 0)  # счетчик нулей подматрицы E матрицы F

    print("Подматрица B:\n", sub_matrix_B)
    print(zero_counter_B)
    print()
    print("Подматрица E:\n", sub_matrix_E)
    print(zero_counter_E)
    print()

    # Формируем матрицу F
    if zero_counter_B > zero_counter_E:
        F[:submatrix_length, submatrix_length+n % 2:n] = sub_matrix_B[:submatrix_length, ::-1]
        F[:submatrix_length, :submatrix_length] = sub_matrix_C[:submatrix_length, ::-1]
    else:
        F[:submatrix_length, :submatrix_length] = sub_matrix_E
        F[submatrix_length+n % 2:n, submatrix_length+n % 2:n] = sub_matrix_B

    print("Отформатированная матрица F:\n", F)

    try:
        if np.linalg.det(A) > sum(np.diagonal(F)):
            print("Результат выражения A*AT – K * F:\n", A*A.transpose() - F*k)
        else:
            G = np.tri(n)*A
            print("Результат выражения (A^(-1) +G-F^(-1))*K:\n", (np.linalg.inv(A) + G - np.linalg.inv(F)) * k)

    except np.linalg.LinAlgError:
        print("Одна из матриц является вырожденной (определитель равен 0), поэтому обратную матрицу найти невозможно.")

    print("Матрица, которая используется при построение графиков:\n", F)

    av = [np.mean(abs(F[i, ::])) for i in range(n)]
    av = int(sum(av))
    fig, axs = plt.subplots(2, 2, figsize=(11, 8))
    x = list(range(1, n+1))
    for j in range(n):
        y = list(F[j, ::])

        axs[0, 0].plot(x, y, ',-', label=f"{j} строка.")
        axs[0, 0].set(title="График с использованием функции plot:", xlabel='Номер элемента в строке', ylabel='Значение элемента')
        axs[0, 0].grid()

        axs[0, 1].bar(x, y, 0.4, label=f"{j} строка.")
        axs[0, 1].set(title="График с использованием функции bar:", xlabel='Номер элемента в строке', ylabel='Значение элемента')
        if n <= 10:
            axs[0, 1].legend(loc='lower right')
            axs[0, 1].legend(loc='lower right')

    explode = [0]*(n-1)
    explode.append(0.1)
    sizes = [round(np.mean(abs(F[i, ::])) * 100/av, 1) for i in range(n)]
    axs[1, 0].set_title("График с ипользованием функции pie:")
    axs[1, 0].pie(sizes, labels=list(range(1, n+1)), explode=explode, autopct='%1.1f%%', shadow=True)

    def heatmap(data, row_labels, col_labels, ax, cbar_kw={}, **kwargs):
        im = ax.imshow(data, **kwargs)
        cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
        ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
        ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)
        return im, cbar
    def annotate_heatmap(im, data = None, textcolors=("black","white"), threshold=0):
        if not isinstance(data, (list, np.ndarray)):
            data = im.get_array()
        kw = dict(horizontalalignment="center", verticalalignment="center")
        texts = []
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                kw.update(color=textcolors[int(data[i, j] > threshold)])
                text = im.axes.text(j, i, data[i, j], **kw)
                texts.append(text)
        return texts
    im, cbar = heatmap(F, list(range(n)), list(range(n)), ax=axs[1, 1], cmap="magma_r")
    texts = annotate_heatmap(im)
    axs[1, 1].set(title="Создание аннотированных тепловых карт:", xlabel="Номер столбца", ylabel="Номер строки")
    plt.suptitle("Использование библиотеки matplotlib")
    plt.tight_layout()
    plt.show()

    number_row = []
    for i in range(1, n+1):
        number_row += [i]*n
    number_item = list(range(1, n+1))*n
    df = pd.DataFrame({"Значения": A.flatten(), "Номер строки": number_row, "Номер элемента в строке": number_item})
    fig, axs = plt.subplots(2, 2, figsize=(11, 8))
    plt.subplot(2, 2, 1)
    plt.title("Использование функции lineplot")
    sns.lineplot(x="Номер элемента в строке", y="Значения", hue="Номер строки", data=df, palette="Set2")
    plt.subplot(222)
    plt.title("Использование функции boxplot")
    sns.boxplot(x="Номер строки", y="Значения", palette="Set2", data=df)
    plt.subplot(223)
    plt.title("Использование функции kdeplot")
    sns.kdeplot(data=df, x="Номер элемента в строке", y="Значения", hue="Номер строки", palette="Set2")
    plt.subplot(224)
    plt.title("Использование функции heatmap")
    sns.heatmap(data=A, annot=True, fmt="d", linewidths=.5)
    plt.suptitle("Использование библиотеки seaborn")
    plt.tight_layout()
    plt.show()

except ValueError:
    print("\nВведенный символ не является числом. Перезапустите программу и введите число.")