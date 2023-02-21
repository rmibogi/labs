# Написать программу, которая читая файл, распознает, преобразует и выводит на экран числа по определенному правилу. Числа распознаются по законам грамматики русского языка.
# Преобразование делать по возможности через словарь. Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. Распознование делать через регулярные выражения.
# В вариантах, где есть параметр К, К заменяется на любое число.
# Натуральные числа. Заменять четные цифры, стоящие на нечетных местах словами (цифры от 0 до 9 на слова «ноль», «один», …, «девять»).

import re

number_to_words = {2 : 'два', 4 : 'четыре', 6 : 'шесть', 8 : 'восемь', 0 : 'ноль'}
number_counter = 0

try:
    file = open("text.txt", "r")    # открываем файл
    while True:
        a = file.readline().split()     # читаем строку
        if not a:
            print("\nФайл text.txt в директории проекта закончился.")
            break
        for j in a:
            res = re.findall(r'\b\d+\b', j) # находим все натуральные числа с учетом грамматики
            if len(res) == 1:
#                print(res, len(res[0]), "|", j, len(j))
                counter = 0         # счетчик для вывода
                number_counter += 1
                for i in res[0]:         # вывод
                    counter += 1
                    if int(i) % 2 == 0 and counter % 2 != 0:
                        print(number_to_words[int(i)], end='')
                    else:
                        print(i, end='')
                print()

    if number_counter == 0:     # если чисел, подходящих условию нет
        print()
        print('В файле нет чисел, удовлетворяющих условию. Добавьте числа в файл или переименуйте существующий *.txt файл.')
                     
except FileNotFoundError:
    print()
    print("\nФайл test.txt в директории не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
    
