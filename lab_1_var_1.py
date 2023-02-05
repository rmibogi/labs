# Натуральные числа. Заменять четные цифры, стоящие на нечетных местах словами (цифры от 0 до 9 на слова «ноль», «один», …, «девять»).

number_to_words = {'1' : 'один', 2 : 'два', 3 : 'три', 4 : 'четыре', 5 : 'пять', 6 : 'шесть', 7 : 'семь', 8 : 'восемь', 9 : 'девять', 0 : 'ноль'}

max_buffer_len = 100    # максимальный размер рабочего буфера
buffer_len = 1          # размер буфера чтения

work_buffer = ""        # рабочий буфер
number_flag = False     # флаг числа
odd_position_flag = True # флаг нечетной позиции
work_buffer_len = buffer_len # длина рабочего буфера

try:
    with open("test.txt", "r") as file:                         # открываем файл
        print("\n------Результат работы программы-----\n")
        buffer = file.read(buffer_len)                          # читаем первый блок
        if not buffer:                                          # если файл пустой
            print("\nФайл test.txt в директории проекта пустой. \nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
        while buffer:                                           # пока файл не пустой
#           print(buffer)
#           print(odd_position_flag)
            if not((buffer >= 'a' and buffer <= 'z') or (buffer >= 'A' and buffer <= 'Z') or (buffer >= 'а' and buffer <= 'я') or (buffer >= 'А' and buffer <= 'Я')):
                if buffer>='0' and buffer <='9' and odd_position_flag and int(buffer) % 2 == 0:     #обрабатываем текущий блок
                    number_flag = True
                    work_buffer += number_to_words[int(buffer)]
                else:
                    work_buffer += buffer
                    if buffer>='0' and buffer <='9':
                        number_flag = True
    
            odd_position_flag = not(odd_position_flag)
#            print(work_buffer, buffer, number_flag)
            
            if buffer.find('.') >= 0 or buffer.find('!') >= 0 or buffer.find('?') >= 0 or buffer.find(',') >= 0 or buffer.find(' ') >= 0:   # если символ, разделяющий числа
                odd_position_flag = True
                if number_flag:             # если число
                    print(work_buffer)      # печатаем число и готовим новый цикл
                    number_flag = False
                work_buffer = ""
                work_buffer_len = 0
            buffer = file.read(buffer_len)  # читаем очередной блок
            work_buffer_len += buffer_len
            if work_buffer_len >= max_buffer_len and buffer.find('.') < 0 and buffer.find('!') < 0 and buffer.find('?') < 0:
                print("\nФайл test.txt не содержит знаков окончания предложения и максимальный размер буфера превышен.\nОткорректируйте файл text.txt в директории проекта или переименуйте существующий *.txt файл.")
                buffer = ""
        print(work_buffer)
                
except FileNotFoundError:
    print("\nФайл test.txt в директории не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
    
