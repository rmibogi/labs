# Написать объектно-ориентированную реализацию, в программе должны быть реализованы минимум один класс, три атрибута, два метода.
# Пароль состоит из К символов. Если первый символ буква, она должна быть заглавной, остальные буквы всегда строчными.
# Первые Т символов – латинские буквы, остальные - латинские буквы или цифры. Обязательно наличие как минимум двух цифр.
# Все символы должны быть разные. Составьте все возможные пароли.

from math import sqrt


def euclidean(password_1, password_2):
    p1 = list(map(ord, password_1))
    p2 = list(map(ord, password_2))
    euclidean = 0
    for coord in range(len(p1)):
        euclidean += (p1[coord] - p2[coord]) ** 2
    euclidean = sqrt(euclidean)
    return euclidean


class PasswordGenerator:
    def __init__(self, length, digits_count, t, min_dist):
        self.length = length
        self.digits_count = digits_count
        self.t = t
        self.passwords = []
        self.max_distance_passwords = []
        self.min_dist = min_dist

    def generate_passwords(self):
        self.passwords = []
        self._generate_password('', self.length, 0, set())

    def _generate_password(self, prefix, remaining_length, letter_count, used_letters):
        if remaining_length == 0:
            if self._is_valid_password(prefix):
                self.passwords.append(prefix)
            return

        if letter_count < self.t:
            # Generate uppercase letter for first T characters
            for char in 'ABCDWXYZ':
                if char not in used_letters:
                    self._generate_password(prefix + char, remaining_length - 1, letter_count + 1, used_letters.union({char}))
        else:
            # Generate lowercase letter or digit for remaining characters
            for char in 'abcdwxyz0123456789':
                if char not in used_letters:
                    self._generate_password(prefix + char, remaining_length - 1, letter_count, used_letters.union({char}))

    def _is_valid_password(self, password):
        if not password[:self.t].isalpha():
            return False

        lowercase_chars = password[self.t:].lower()
        if len(set(lowercase_chars)) != len(lowercase_chars):
            return False

        digit_count = sum(char.isdigit() for char in password)
        if digit_count < self.digits_count:
            return False

        return True

    def generate_passwords(self):
        self.passwords = []
        self._generate_password('', self.length, 0, set())
        self.filter_passwords(self.passwords, self.min_dist)

    def filter_passwords(self, passwords, min_dist_in):
        self.max_distance_passwords = []
        for i in range(len(passwords)):
            is_max_distance = True
            for j in range(len(self.max_distance_passwords)):
                if euclidean(passwords[i], self.max_distance_passwords[j]) <= min_dist_in:
                    is_max_distance = False
                    break
            if is_max_distance:
                self.max_distance_passwords.append(passwords[i])
        return self.max_distance_passwords


K = int(input("Введите число K >= 1, количество символов из которых состоит пароль: \n"))
while K <= 0:
    K = int(input("Ошибка: введите натуральное число K: "))

T = int(input("Введите натуральное число T < K - 1, количество первых символов, которые будут заглавными латинскими буквами: \n"))
while T < 0 or T >= K - 1:
    T = int(input("Ошибка: введите натуральное число T, удовлетворяющее условию T < K - 1: "))

P = int(input("Введите натуральное число P, минимальное геометрическое расстояние между двумя паролями: \n"))
while P < 0:
    P = int(input("Ошибка: введите натуральное число P: "))

print("\nНайденные варианты паролей (это может занять некоторое время):")

generator = PasswordGenerator(length=K, digits_count=2, t=T, min_dist=P)
generator.generate_passwords()

for password in generator.passwords:
    print(password, end=" ")
print()

print(f"\nПароли с геометрическим расстоянием больше {P}:")

if len(generator.max_distance_passwords) != 1:
    for password in generator.max_distance_passwords:
        print(password, end=" ")
else:
    print("Таких паролей нет.")