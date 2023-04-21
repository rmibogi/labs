# Задание состоит из двух частей.
# 1 часть – написать программу в соответствии со своим вариантом задания.
# 2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум
# одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.
# Гр. ИСТд-11
# Вариант 1.Пароль состоит из К символов. Первые Т символов – латинские буквы, остальные - латинские буквы или цифры.
# Обязательно наличие как минимум одной цифры. Все символы должны быть разные. Составьте все возможные пароли.

def generate_passwords(K, T, password=""):
    if len(password) == K:
        if sum(c.isdigit() for c in password) >= 1:
            print(password, end= " ")
        return
    if len(password) < T:
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c not in password:
                generate_passwords(K, T, password + c)
    else:
        for c in "abcdefghijklmnopqrstuvwxyz0123456789":
            if c not in password:
                generate_passwords(K, T, password + c)

print("Введите натуральное число K, количество символов из которых состоит пароль: ")
K = int(input())
while K < 0:  # ошибка в случае введения не натурального числа
    K = int(input("\nВы ввели не натуральное число, функция определенна лишь в области натуральных чисел. Введите натуральное число:\n"))

print("Введите натуральное число T, количество первых символов, которые будут латинскими буквами: ")
T = int(input())
while T < 0:  # ошибка в случае введения не натурального числа
    T = int(input("\nВы ввели не натуральное число, функция определенна лишь в области натуральных чисел. Введите натуральное число:\n"))

print("\nНайденные варианты паролей:")
generate_passwords(K, T)

