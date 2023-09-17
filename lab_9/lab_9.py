from tkinter import *
import re
from tkinter import ttk
from tkinter.ttk import Progressbar

ceasar_key = 3

font_style = ('Arial', 14, 'bold')
font_style_desc = ('Arial', 12, 'bold')


def dismiss(window):
    window.grab_release()
    window.destroy()

def show_tooltip(tooltip_text):
    global tooltip
    tooltip = Toplevel(root)
    tooltip.overrideredirect(True)
    style = ttk.Style()
    style.configure("Tooltip.TLabel", background="lightyellow", relief="solid", borderwidth=1)
    description = ttk.Label(tooltip, text=tooltip_text, style="Tooltip.TLabel")
    description.pack()
    tooltip.update_idletasks()
    tooltip.geometry(f"+{root.winfo_pointerx()}+{root.winfo_pointery()}")

def custom_showmessage(name, error, button=''):
    error_window = Toplevel(root, relief=SUNKEN)
    error_window.geometry("400x100+730+420")
    error_window.resizable(False, False)
    error_window.title(name)
    error_window.protocol("WM_DELETE_WINDOW", lambda: dismiss(error_window))
    error_window.columnconfigure(index=1, weight=1)
    error_window.rowconfigure(index=1, weight=2)
    error_window.rowconfigure(index=2, weight=3)
    Label(error_window, text=error, font=font_style_desc).grid(row=1, column=1)
    if button != '':
        close_button = Button(error_window, text=button, font=font_style_desc, command=lambda: dismiss(error_window))
        close_button.grid(row=2, column=1)
    if button == 'Продолжить':
        close_button = Button(error_window, text=button, font=font_style_desc, command=lambda: (dismiss(error_window), dismiss(root)))
        close_button.grid(row=2, column=1)
    error_window.grab_set()


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
        custom_showmessage('Регистрация', 'Пожалуйста, заполните все поля.', 'Повторить ввод')
        return

    with open('user_data.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            stored_username, _ = line.strip().split('•')
            if username == stored_username:
                custom_showmessage('Регистрация', 'Пользователь с таким именем уже существует.', 'Повторить ввод')
                return

    strength = get_password_strength(password)

    if strength == 'Низкая':
        custom_showmessage('Регистрация', 'Пароль слишком слабый!', 'Повторить ввод')
    else:
        encrypted_password = encrypt_password(password)
        with open('user_data.txt', 'a') as file:
            file.write(f'{username}•{encrypted_password}\n')
        custom_showmessage('Регистрация', 'Регистрация прошла успешно!', 'Продолжить')


def login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        custom_showmessage('Вход', 'Пожалуйста, заполните все поля.', 'Повторить ввод')
        return

    with open('user_data.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            stored_username, stored_encrypted_password = line.strip().split('•')
            stored_password = decrypt_password(stored_encrypted_password)
            if username == stored_username and password == stored_password:
                custom_showmessage('Вход', 'Вход выполнен успешно!', 'Продолжить')
                return

    custom_showmessage('Вход', 'Неверное имя пользователя или пароль.', 'Повторить ввод')


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
    if re.search(r'[а-я]|[А-Я]', password):
        return 'Низкая'

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


root = Tk()
root.title('Регистрация и вход')
root.geometry("640x480+600+300")
root.resizable(False, False)

label_username = Label(root, text='Имя пользователя', font=font_style)
label_password = Label(root, text='Пароль', font=font_style)
entry_username = Entry(root, font=font_style)
entry_password = Entry(root, show='*', font=font_style)
button_register = Button(root, text='Зарегистрироваться', width=19, command=register, font=font_style)
button_login = Button(root, text='Войти', width=7, command=login, font=font_style)

label_username.place(x=205, y=20)
entry_username.place(x=208, y=50)
label_password.place(x=205, y=80)
entry_password.place(x=208, y=110)
button_register.place(x=205, y=260)
button_login.place(x=205, y=210)

password_strength_label = Label(root, text='', fg='black', font=font_style_desc)
password_strength_label.place(x=205, y=180)

password_strength_bar = Progressbar(root, length=225, mode='determinate')
password_strength_bar.place(x=208, y=150)

show_password_var = BooleanVar()
show_password_var.set(False)
show_password_checkbox = Checkbutton(root, variable=show_password_var, command=toggle_password_visibility)
show_password_checkbox.place(x=440, y=110)

entry_password.bind("<Enter>", lambda event: show_tooltip("Пароль должен состоять\nиз латинских букв и цифр,\nминимум 8 символов."))
entry_password.bind("<Leave>", lambda event: dismiss(tooltip))
show_password_checkbox.bind("<Enter>", lambda event: show_tooltip("Показать пароль"))
show_password_checkbox.bind("<Leave>", lambda event: dismiss(tooltip))
entry_password.bind('<KeyRelease>', update_password_strength)

mainloop()
