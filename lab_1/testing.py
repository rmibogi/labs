number_to_words = {'1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь',
                   '8': 'восемь', '9': 'девять', '0': 'ноль'}
numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}  # использование множества вместо генерации списка
symbols = {'.', '!', '?', ',', ' '}

max_buffer_len = 100
buffer_len = 1

work_buffer = ""
number_flag = False
trash_flag = False
odd_position_flag = True
work_buffer_len = buffer_len

try:
    with open("text.txt", "r") as file:
        print("\n------Результат работы программы-----\n")
        buffer = file.read(buffer_len)
        if not buffer:
            print(
                "\nФайл test.txt в директории проекта пустой. \nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
        while buffer:
            if buffer in numbers and odd_position_flag and int(
                    buffer) % 2 == 0:  # проверка на вхождение в множество и использование прямого сравнения
                number_flag = True
                work_buffer += number_to_words[buffer]
            else:
                work_buffer += buffer
                if buffer in numbers:
                    number_flag = True
                elif buffer not in symbols:
                    trash_flag = True
            odd_position_flag = not odd_position_flag

            if any(s in buffer for s in
                   symbols) and work_buffer_len > 1:  # использование any для поиска символов в строке
                odd_position_flag = True
                if number_flag and not trash_flag:
                    work_buffer = work_buffer[:-1]
                    print(work_buffer)
                    number_flag = False
                trash_flag = False
                work_buffer = ""
                work_buffer_len = 0
            elif any(s in buffer for s in
                     symbols) and work_buffer_len > 0:  # использование any для поиска символов в строке
                odd_position_flag = True
                trash_flag = False
                work_buffer = ""
                work_buffer_len = 0
            buffer = file.read(buffer_len)
            work_buffer_len += buffer_len
            if work_buffer_len >= max_buffer_len and not any(s in buffer for s in symbols):
                print(
                    "\nФайл test.txt не содержит знаков, разделяющих числа, и максимальный размер буфера превышен.\nОткорректируйте файл text.txt в директории проекта или переименуйте существующий *.txt файл.")
                buffer = ""
        if not trash_flag:
            print(work_buffer)

except FileNotFoundError:
    print(
        "\nФайл test.txt в директории не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")