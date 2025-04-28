import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    alternating_starting_player = "O"

    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg='#ff6347')
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        self.current_player = random.choice(["X", "O"])
        self.status_label = tk.Label(self.root, text=f"Player {self.current_player}'s turn", font=('normal', 20))
        self.status_label.grid(row=3, column=0, columnspan=3)
        if self.current_player == "X":
            self.computer_move()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.root, text="", font=('normal', 40), width=5, height=2,
                                                   command=lambda r=row, c=col: self.on_click(r, c),bg="dark blue",fg="white")
                self.buttons[row][col].grid(row=row, column=col)

    def on_click(self, row, col):
        if self.buttons[row][col]["text"] == "" and self.current_player == "O":
            self.buttons[row][col]["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", "Player O wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "X"
                self.status_label.config(text="Player X's turn")
                self.computer_move()

    def computer_move(self):
        best_move = self.find_best_move()
        if best_move:
            row, col = best_move
            self.buttons[row][col]["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", "Player X (Computer) wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O"
                self.status_label.config(text="Player O's turn")

    def find_best_move(self):
        best_score = float('-inf')
        best_move = None
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]["text"] == "":
                    self.buttons[row][col]["text"] = "X"
                    score = self.minimax(0, False)
                    self.buttons[row][col]["text"] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        return best_move

    def minimax(self, depth, is_maximizing):
        if self.check_winner():
            return 1 if self.current_player == "X" else -1
        if self.check_draw():
            return 0

        original_player = self.current_player

        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if self.buttons[row][col]["text"] == "":
                        self.buttons[row][col]["text"] = "X"
                        self.current_player = "X"
                        score = self.minimax(depth + 1, False)
                        self.buttons[row][col]["text"] = ""
                        best_score = max(score, best_score)
            self.current_player = original_player
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if self.buttons[row][col]["text"] == "":
                        self.buttons[row][col]["text"] = "O"
                        self.current_player = "O"
                        score = self.minimax(depth + 1, True)
                        self.buttons[row][col]["text"] = ""
                        best_score = min(score, best_score)
            self.current_player = original_player
            return best_score

    def check_winner(self):
        for row in range(3):
            if all(self.buttons[row][col]["text"] == self.current_player for col in range(3)):
                return True
        for col in range(3):
            if all(self.buttons[row][col]["text"] == self.current_player for row in range(3)):
                return True
        if all(self.buttons[i][i]["text"] == self.current_player for i in range(3)):
            return True
        if all(self.buttons[i][2-i]["text"] == self.current_player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.buttons[row][col]["text"] != "" for row in range(3) for col in range(3))

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""
        self.current_player = random.choice(["X", "O"])
        self.status_label.config(text=f"Player {self.current_player}'s turn")
        if self.current_player == "X":
            self.computer_move()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
