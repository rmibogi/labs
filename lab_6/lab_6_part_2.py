# Задание состоит из двух частей.
# 1 часть – написать программу в соответствии со своим вариантом задания.
# 2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум
# одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.
# Гр. ИСТд-11
# Вариант 1.Пароль состоит из К символов. Первые Т символов – латинские буквы, остальные - латинские буквы или цифры.
# Обязательно наличие как минимум одной цифры. Все символы должны быть разные. Составьте все возможные пароли.

def generate_passwords(K, T, password="", num_digits=0):
    global count
    if len(password) == K:
        if num_digits >= 2:
            print(password, end=" ")
            count += 1
        return
    if len(password) < T:
        for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if c not in password:
                generate_passwords(K, T, password + c, num_digits)
    else:
        for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            if c not in password:
                if c.isdigit():
                    generate_passwords(K, T, password + c, num_digits + 1)
                else:
                    generate_passwords(K, T, password + c, num_digits)

count = 0

K = int(input("Введите число K >= 1, количество символов из которых состоит пароль: \n"))
while K <= 0:
    K = int(input("Ошибка: введите натуральное число K: "))

T = int(input("Введите натуральное число T < K - 1, количество первых символов, которые будут латинскими буквами: \n"))
while T < 0 or T >= K - 1:
    T = int(input("Ошибка: введите натуральное число T, удовлетворяющее условию T < K - 1: "))

print("\nНайденные варианты паролей. Первые Т символов – латинские буквы, остальные - латинские буквы или цифры. \nОбязательно наличие как минимум двух цифр. Все символы должны быть разные:")
generate_passwords(K, T)

print("\nКоличество найденных паролей:", count)

