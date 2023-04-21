def generate_passwords(K, T, password="", num_digits=0, first_letter=True):
    global count
    if len(password) == K:
        if num_digits >= 2:
            print(password, end=" ")
            count += 1
        return
    if len(password) < T:
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c not in password:
                if first_letter:
                    generate_passwords(K, T, password + c.upper(), num_digits, False)
                else:
                    generate_passwords(K, T, password + c, num_digits, False)
    else:
        for c in "abcdefghijklmnopqrstuvwxyz0123456789":
            if c not in password:
                if c.isdigit():
                    generate_passwords(K, T, password + c, num_digits + 1, first_letter)
                else:
                    generate_passwords(K, T, password + c, num_digits, first_letter)

count = 0

K = int(input("Введите число K >= 1, количество символов из которых состоит пароль: \n"))
while K <= 0:
    K = int(input("Ошибка: введите натуральное число K: "))

T = int(input("Введите натуральное число T < K, количество первых символов, которые будут латинскими буквами: \n"))
while T < 0 or T >= K - 1:
    T = int(input("Ошибка: введите натуральное число T, удовлетворяющее условию T < K - 1: "))

print("\nНайденные варианты паролей:")
generate_passwords(K, T)

print("\nКоличество найденных паролей:", count)