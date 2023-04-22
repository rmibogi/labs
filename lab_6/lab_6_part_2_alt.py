# Задание состоит из двух частей.
# 1 часть – написать программу в соответствии со своим вариантом задания.
# 2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум
# одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.
# Гр. ИСТд-11
# Вариант 1.Пароль состоит из К символов. Первые Т символов – латинские буквы, остальные - латинские буквы или цифры.
# Обязательно наличие как минимум одной цифры. Все символы должны быть разные. Составьте все возможные пароли.

from math import sqrt

def max_distance_password(passwords):
    max_distance = 0
    max_distance_passwords = None
    for i in range(len(passwords)):
        p1 = list(map(ord, passwords[i]))
        for j in range(i+1, len(passwords)):
            p2 = list(map(ord, passwords[j]))
            euclidean = 0
            for coord in range(len(p1)):
                euclidean += (p1[coord] - p2[coord]) ** 2
            euclidean = sqrt(euclidean)
            if euclidean > max_distance:
                max_distance = euclidean
                max_distance_passwords = (passwords[i], passwords[j])
    return max_distance_passwords

def generate_passwords(K, T, password="", num_digits=0, first_letter=True, passwords=[]):
    global count
    if len(password) == K:
        if num_digits >= 2:
            passwords.append(password)
            count += 1
        return
    if len(password) < T:
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c not in password:
                if first_letter:
                    generate_passwords(K, T, password + c.upper(), num_digits, False, passwords)
                else:
                    generate_passwords(K, T, password + c, num_digits, False, passwords)
    else:
        for c in "abcdefghijklmnopqrstuvwxyz0123456789":
            if c not in password:
                if c.isdigit():
                    generate_passwords(K, T, password + c, num_digits + 1, False, passwords)
                if first_letter:
                    generate_passwords(K, T, password + c.upper(), num_digits, False, passwords)
                else:
                    generate_passwords(K, T, password + c, num_digits, first_letter, passwords)

count = 0

K = int(input("Введите число K >= 1, количество символов из которых состоит пароль: \n"))
while K <= 0:
    K = int(input("Ошибка: введите натуральное число K: "))

T = int(input("Введите натуральное число T < K - 1, количество первых символов, которые будут латинскими буквами: \n"))
while T < 0 or T >= K - 1:
    T = int(input("Ошибка: введите натуральное число T, удовлетворяющее условию T < K - 1: "))

print("\nНайденные варианты паролей. Если первый символ буква, она должна быть заглавной, остальные буквы всегда строчными. Первые Т символов – латинские буквы, остальные - латинские буквы или цифры. \nОбязательно наличие как минимум двух цифр. Все символы должны быть разные:")
passwords = []
generate_passwords(K, T, passwords=passwords)
print(*passwords)

max_distance_passwords = max_distance_password(passwords)
print(f"\nНаибольшее геометрическое расстояние между точками {max_distance_password[0]} и {max_distance_password[1]} и оно равно {max_distance_passwords}")

print("\nКоличество найденных паролей:", count)