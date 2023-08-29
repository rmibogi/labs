# Написать объектно-ориентированную реализацию, в программе должны быть реализованы минимум один класс, три атрибута, два метода.
#
# Пароль состоит из К символов. Первые Т символов – заглавные латинские буквы из набора "ABCDWXYZ", остальные -
# латинские буквы или цифры из набора "abcdwxyz0123456789". Обязательно наличие как минимум двух цифр.
# Все символы должны быть разные. Составьте все возможные пароли.

# Требуется для своего варианта второй части л.р. №6 (усложненной программы) или ее объектно-ориентированной реализации (л.р. №7)
# разработать реализацию с использованием графического интерфейса. Допускается использовать любую графическую библиотеку питона.
# Рекомендуется использовать внутреннюю библиотеку питона  tkinter.

# В программе должны быть реализованы минимум одно окно ввода, одно окно вывода,
# текстовое поле, кнопка.

import tkinter as tk
from tkinter import messagebox
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
    def __init__(self, main):
        self.first_click = True

        self.main = main
        self.label_main = tk.Label(main,
                                   text="Пароль состоит из К символов. Первые Т символов – заглавные латинские буквы из набора ABCDWXYZ, "
                                        "\nостальные - латинские буквы или цифры из набора abcdwxyz0123456789. Обязательно наличие как минимум двух цифр. "
                                        "\nВсе символы должны быть разные. Составьте все возможные пароли.")

        self.label1 = tk.Label(main, text="Введите число K >= 2, количество символов из которых состоит пароль:")
        self.entry1 = tk.Entry(main, width=30, justify='center')

        self.label2 = tk.Label(main,
                               text="Введите натуральное число T < K - 1 <= 8, количество первых символов, которые будут заглавными латинскими буквами:")
        self.entry2 = tk.Entry(main, width=30, justify='center')

        self.label3 = tk.Label(main,
                               text="Введите натуральное число P, минимальное геометрическое расстояние между двумя паролями:")
        self.entry3 = tk.Entry(main, width=30, justify='center')

        self.button_main = tk.Button(main, text="Составить пароли", command=self.results)

        self.label_main.pack()
        self.label1.pack()
        self.entry1.pack()
        self.label2.pack()
        self.entry2.pack()
        self.label3.pack()
        self.entry3.pack()
        self.button_main.pack(expand=True)

    def results(self):
        try:
            self.conditions = True
            self.length = int(self.entry1.get())
            if self.length < 2 or self.length > 26:
                messagebox.showwarning(title="Ошибка", message="Ошибка: введите натуральное число 2 <= K <= 26.")
                self.conditions = False
            self.digits_count = 2
            self.first_letters_count = int(self.entry2.get())
            if self.first_letters_count < 0 or self.first_letters_count >= self.length - 1 or self.first_letters_count > 8:
                messagebox.showwarning(title="Ошибка", message="Ошибка: введите натуральное число T, удовлетворяющее условию T < K - 1 <= 8.")
                self.conditions = False
            self.passwords = []
            self.max_distance_passwords = []
            self.min_dist = int(self.entry3.get())
            if self.min_dist < 0:
                messagebox.showwarning(title="Ошибка", message="Ошибка: введите натуральное число P.")
                self.conditions = False

            if self.conditions == True:
                self.generate_passwords()
                self.filter_passwords()

                if self.first_click == True:
                    self.display_results()
                    self.first_click = False
                else:
                    self.results_window.destroy()
                    self.filtered_results_window.destroy()
                    self.display_results()

        except ValueError:
            messagebox.showwarning(title="Ошибка", message="Введено не число.")

    def generate_passwords(self):
        self._generate_password('')

    def _generate_password(self, prefix):
        if len(prefix) == self.length:
            if self._is_valid_password(prefix):
                self.passwords.append(prefix)
            return

        if len(prefix) < self.first_letters_count:
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

    def filter_passwords(self):
        for i in range(len(self.passwords)):
            is_max_distance = True
            for j in range(len(self.max_distance_passwords)):
                if euclidean(self.passwords[i], self.max_distance_passwords[j]) <= self.min_dist:
                    is_max_distance = False
                    break
            if is_max_distance:
                self.max_distance_passwords.append(self.passwords[i])

    def display_results(self):
        self.results_window = tk.Toplevel(self.main)
        self.results_window.geometry('480x320')
        self.results_window.title('Результаты')

        self.password_list = tk.Listbox(self.results_window)
        self.password_list.pack(side='left', fill='both', expand=1)

        for password in self.passwords:
            self.password_list.insert('end', password)

        self.scrollbar = tk.Scrollbar(self.results_window, command=self.password_list.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.password_list.config(yscrollcommand=self.scrollbar.set)

        self.filtered_results_window = tk.Toplevel(self.main)
        self.filtered_results_window.geometry('480x320')
        self.filtered_results_window.title('Фильтрованные результаты')

        self.filtered_list = tk.Listbox(self.filtered_results_window)
        self.filtered_list.pack(side='left', fill='both', expand=1)

        for password in self.max_distance_passwords:
            self.filtered_list.insert('end', password)

        self.scrollbar_filtered = tk.Scrollbar(self.filtered_results_window, command=self.filtered_list.yview)
        self.scrollbar_filtered.pack(side='right', fill='y')
        self.filtered_list.config(yscrollcommand=self.scrollbar_filtered.set)


root = tk.Tk()
root.title("Генератор паролей")
root.geometry("720x480")
root.resizable(False, False)

g = PasswordGenerator(root)

root.mainloop()