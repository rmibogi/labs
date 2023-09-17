import tkinter as tk
from tkinter import messagebox
import re
from tkinter.ttk import Progressbar

ceasar_key = 3

font_style = ('Arial', 14, 'bold')
font_style_desc = ('Arial', 12, 'bold')


def encrypt_password(password):
    encrypted_password = ""
    for char in password:
        encrypted_char = chr(ord(char) + ceasar_key)
        encrypted_password += encrypted_char
    return encrypted_password


def decrypt_password(encrypted_password):
    decrypted_password = ""
    for char in encrypted_password:
        decrypted_char = chr(ord(char) - ceasar_key)
        decrypted_password += decrypted_char
    return decrypted_password


def register():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror('Регистрация', 'Пожалуйста, заполните все поля.')
        return

    with open('user_data.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            stored_username, _ = line.strip().split('•')
            if username == stored_username:
                messagebox.showerror('Регистрация', 'Пользователь с таким именем уже существует.')
                return

    strength = get_password_strength(password)

    if strength == 'Низкая':
        messagebox.showerror('Регистрация', 'Пароль слишком слабый!')
    else:
        encrypted_password = encrypt_password(password)
        with open('user_data.txt', 'a') as file:
            file.write(f'{username}•{encrypted_password}\n')
        messagebox.showinfo('Регистрация', 'Регистрация прошла успешно!')


def login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror('Вход', 'Пожалуйста, заполните все поля.')
        return

    with open('user_data.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            stored_username, stored_encrypted_password = line.strip().split('•')
            stored_password = decrypt_password(stored_encrypted_password)
            if username == stored_username and password == stored_password:
                messagebox.showinfo('Вход', 'Вход выполнен успешно!')
                return

    messagebox.showerror('Вход', 'Неверное имя пользователя или пароль.')


def update_password_strength(*args):
    password = entry_password.get()

    if password:
        strength = get_password_strength(password)

        if strength == 'Высокая':
            password_strength_label.config(text='Сложность пароля: Сильная', fg='green', font=font_style_desc)
            password_strength_bar['value'] = 100
        elif strength == 'Средняя':
            password_strength_label.config(text='Сложность пароля: Средняя', fg='orange', font=font_style_desc)
            password_strength_bar['value'] = 60
        else:
            password_strength_label.config(text='Сложность пароля: Низкая', fg='red', font=font_style_desc)
            password_strength_bar['value'] = 30
    else:
        password_strength_label.config(text='', fg='black', font=font_style)
        password_strength_bar['value'] = 0


def get_password_strength(password):
    if len(password) < 8:
        return 'Низкая'

    if not re.search(r'\d', password):
        return 'Низкая'

    if not re.search(r'[a-z]', password):
        return 'Низкая'

    if not re.search(r'[A-Z]', password):
        return 'Средняя'

    if not re.search(r'[!@#\$%^&*()_+{}\[\]:;<>,.?~\\-]', password):
        return 'Средняя'

    return 'Высокая'


def toggle_password_visibility():
    if show_password_var.get():
        entry_password.config(show='')
    else:
        entry_password.config(show='*')


root = tk.Tk()
root.title('Регистрация и вход')
root.geometry("640x480+600+300")
root.resizable(False, False)

label_username = tk.Label(root, text='Имя пользователя', font=font_style)
label_password = tk.Label(root, text='Пароль', font=font_style)
entry_username = tk.Entry(root, font=font_style)
entry_password = tk.Entry(root, show='*', font=font_style)
button_register = tk.Button(root, text='Зарегистрироваться', width=19, command=register, font=font_style)
button_login = tk.Button(root, text='Войти', width=7, command=login, font=font_style)

label_username.place(x=205, y=20)
entry_username.place(x=208, y=50)
label_password.place(x=205, y=80)
entry_password.place(x=208, y=110)
button_register.place(x=205, y=260)
button_login.place(x=205, y=210)

password_strength_label = tk.Label(root, text='', fg='black', font=font_style_desc)
password_strength_label.place(x=205, y=180)

password_strength_bar = Progressbar(root, length=225, mode='determinate')
password_strength_bar.place(x=208, y=150)

show_password_var = tk.BooleanVar()
show_password_var.set(False)
show_password_checkbox = tk.Checkbutton(root, variable=show_password_var,
                                        command=toggle_password_visibility, font=font_style_desc)
show_password_checkbox.place(x=440, y=110)

entry_password.bind('<KeyRelease>', update_password_strength)

root.mainloop()
