# Крестики-нолики на tkinter с компьютером.

import tkinter as tk
import random


def dismiss(window):
    window.grab_release()
    window.destroy()


def game_over_popup(result):
    global popup
    popup = tk.Toplevel(root)
    popup.title("Игра окончена")
    popup.geometry("+600+300")
    popup.resizable(False, False)

    message = tk.Label(popup, text=result, font=("normal", 16))
    message.pack(padx=20, pady=20)

    popup.protocol("WM_DELETE_WINDOW", lambda: start_new_game())
    restart_button = tk.Button(popup, text="Начать новую игру", font=("normal", 16), command=lambda: (start_new_game(), dismiss(popup)))
    restart_button.pack(padx=20, pady=20)

    popup.grab_set()


def select_options():
    options_window = tk.Toplevel(root)
    options_window.title("Настройки игры")
    options_window.geometry("+600+300")
    options_window.resizable(False, False)

    def start_game():
        global difficulty, game_mode
        difficulty = difficulty_var.get()
        game_mode = mode_var.get()
        options_window.grab_release()
        options_window.destroy()
        start_new_game()

    difficulty_label = tk.Label(options_window, text="Выберите сложность:", font=("normal", 16))
    difficulty_label.grid(row=0, column=0, padx=10, pady=10)
    difficulty_var = tk.StringVar(options_window)
    difficulty_var.set(difficulty)
    difficulty_menu = tk.OptionMenu(options_window, difficulty_var, "легкая", "сложная")
    difficulty_menu.config(font=("normal", 12))
    difficulty_menu.grid(row=0, column=1, padx=10, pady=10)

    mode_label = tk.Label(options_window, text="Выберите режим игры:", font=("normal", 16))
    mode_label.grid(row=1, column=0, padx=10, pady=10)
    mode_var = tk.StringVar(options_window)
    mode_var.set(game_mode)
    mode_menu = tk.OptionMenu(options_window, mode_var, "игрок против компьютера", "игрок против игрока")
    mode_menu.config(font=("normal", 12))
    mode_menu.grid(row=1, column=1, padx=10, pady=10)

    start_button = tk.Button(options_window, text="Начать игру", font=("normal", 16), command=start_game)
    start_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    options_window.grab_set()


def check_win(board_copy, player):
    for i in range(0, 8, 3):
        if board_copy[i] == board_copy[i + 1] == board_copy[i + 2] == player:
            return True
    for i in range(3):
        if board_copy[i] == board_copy[i + 3] == board_copy[i + 6] == player:
            return True
    if board_copy[0] == board_copy[4] == board_copy[8] == player or board_copy[2] == board_copy[4] == board_copy[6] == player:
        return True
    return False


def evaluate(board_copy):
    if check_win(board_copy, "X"):
        return -1
    elif check_win(board_copy, "O"):
        return 1
    elif " " not in board_copy:
        return 0
    else:
        return None


def minimax(board_copy, depth, is_max):
    score = evaluate(board_copy)

    if score is not None:
        return score

    if is_max:
        best_score = -float("inf")
        for i in range(9):
            if board_copy[i] == " ":
                board_copy[i] = "O"
                score = minimax(board_copy, depth + 1, False)
                board_copy[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board_copy[i] == " ":
                board_copy[i] = "X"
                score = minimax(board_copy, depth + 1, True)
                board_copy[i] = " "
                best_score = min(score, best_score)
        return best_score


def computer_move():
    global player_turn, game_over
    if not player_turn and not game_over:
        if difficulty == "легкая":
            empty_cells = [i for i in range(9) if board[i] == " "]
            if empty_cells:
                move = random.choice(empty_cells)
                board[move] = "O"
                buttons[move].config(text="O")
        else:
            best_score = -float("inf")
            best_move = None
            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    score = minimax(board, 0, False)
                    board[i] = " "
                    if score > best_score:
                        best_score = score
                        best_move = i
            if best_move is not None:
                board[best_move] = "O"
                buttons[best_move].config(text="O")
        player_turn = not player_turn
        if check_win(board, "O"):
            game_over_popup("Компьютер победил!")
        elif " " not in board:
            game_over_popup("Ничья!")


def player_move(position):
    global player_turn, game_over
    if board[position] == " " and not game_over:
        if player_turn:
            board[position] = "X"
        else:
            board[position] = "O"
        buttons[position].config(text=board[position])
        player_turn = not player_turn
        if check_win(board, "X"):
            game_over_popup("Игрок X победил!")
        elif check_win(board, "O"):
            game_over_popup("Игрок O победил!")
        elif " " not in board:
            game_over_popup("Ничья!")
        else:
            if game_mode == "игрок против компьютера":
                computer_move()


def start_new_game():
    global player_turn, game_over, board
    player_turn = True
    game_over = False
    board = [" " for i in range(9)]
    for b in buttons:
        b.config(text=" ")
    if game_mode == "игрок против компьютера" and not player_turn:
        computer_move()


root = tk.Tk()
root.title("Крестики-нолики")
root.geometry("630x720+500+50")

player_turn = True
game_over = False
board = [" " for i in range(9)]
difficulty = "легкая"
game_mode = "игрок против компьютера"

buttons = []
for i in range(9):
    row = i // 3
    col = i % 3
    button = tk.Button(root, text=" ", font=("normal", 52), width=5, height=2,
                       command=lambda position=i: player_move(position))
    button.grid(row=row, column=col)
    buttons.append(button)

options_button = tk.Button(root, text="Настройки", font=("normal", 16), command=select_options)
options_button.grid(row=4, column=0, columnspan=3, pady=20)

root.mainloop()
