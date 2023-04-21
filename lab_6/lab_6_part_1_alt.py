import itertools

K = int(input("Введите число K >= 1, количество символов из которых состоит пароль: \n"))
while K <= 0:
    K = int(input("Ошибка: введите натуральное число K: "))

T = int(input("Введите натуральное число T < K, количество первых символов, которые будут латинскими буквами: \n"))
while T < 0 or T >= K:
    T = int(input("Ошибка: введите натуральное число T, удовлетворяющее условию T < K: "))

count = 0
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'

combinations = itertools.product(letters + numbers, repeat=K)

print("\nНайденные варианты паролей:")

for combination in combinations:
    password = ''.join(combination)
    if len(set(password)) == K and any(c.isdigit() for c in password) and password[:T].isalpha():
        print(password, end=" ")
        count += 1

print("\nКоличество найденных паролей:", count)