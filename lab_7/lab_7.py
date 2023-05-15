# Написать объектно-ориентированную реализацию, в программе должны быть реализованы минимум один класс, три атрибута, два метода.
#
# Пароль состоит из К символов. Первые Т символов – заглавные латинские буквы из набора "ABCDWXYZ", остальные -
# латинские буквы или цифры из набора "abcdwxyz0123456789". Обязательно наличие как минимум двух цифр.
# Все символы должны быть разные. Составьте все возможные пароли.


from math import sqrt


def euclidean(password_1, password_2):
    p1 = list(map(ord, password_1))
    p2 = list(map(ord, password_2))
    euclidean_result = 0
    for coord in range(len(p1)):
        euclidean_result += (p1[coord] - p2[coord]) ** 2
    euclidean_result = sqrt(euclidean_result)
    return euclidean_result


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
        self._generate_password('')
        self.filter_passwords(self.passwords, self.min_dist)

    def _generate_password(self, prefix):
        if len(prefix) == self.length:
            if self._is_valid_password(prefix):
                self.passwords.append(prefix)
            return

        if len(prefix) < self.t:
            for char in 'ABCDWXYZ':
                if char not in prefix:
                    self._generate_password(prefix + char)
        else:
            for char in 'abcdwxyz0123456789':
                if char not in prefix:
                    self._generate_password(prefix + char)

    def _is_valid_password(self, password):
        digit_count = sum(char.isdigit() for char in password)
        if digit_count < self.digits_count:
            return False

        return True

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


K = int(input("Введите число K >= 2, количество символов из которых состоит пароль: \n"))
while K < 2 or K > 26:
    K = int(input("Ошибка: введите натуральное число K <= 26: "))

T = int(input(
    "Введите натуральное число T < K - 1 <= 8, количество первых символов, которые будут заглавными латинскими буквами: \n"))
while T < 0 or T >= K - 1 or T > 8:
    T = int(input("Ошибка: введите натуральное число T, удовлетворяющее условию T < K - 1 <= 8: "))

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
