import tkinter as tk
import random
from abc import ABC, abstractmethod

class IGame(ABC):
    """Game interface enforcing key methods."""
    @abstractmethod
    def check_winner(self):
        pass

    @abstractmethod
    def check_draw(self):
        pass

    @abstractmethod
    def reset_board(self, message):
        pass

class Player(ABC):
    """Abstract player class."""
    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def make_move(self, game, row, col):
        pass

class HumanPlayer(Player):
    """Human player who clicks buttons."""
    def make_move(self, game, row, col):
        if game.buttons[row][col]["text"] == "":
            game.buttons[row][col]["text"] = self.symbol
            game.process_turn()

class ComputerPlayer(Player):
    """AI player using Minimax algorithm."""
    def make_move(self, game):
        best_move = game.find_best_move()
        if best_move:
            row, col = best_move
            game.buttons[row][col]["text"] = self.symbol
            game.process_turn()

class TicTacToe(tk.Tk, IGame):
    """Main game class implementing the interface."""
    alternate_starting_player = "O"

    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.configure(bg='#ff6347')

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

        self.current_player = TicTacToe.alternate_starting_player
        self.human = HumanPlayer("O")
        self.computer = ComputerPlayer("X")

        self.status_label = tk.Label(self, text=f"Player {self.current_player}'s turn", font=('normal', 20))
        self.status_label.grid(row=3, column=0, columnspan=3)

        if self.current_player == "X":
            self.computer.make_move(self)

    def create_board(self):
        """Create the UI buttons for Tic-Tac-Toe."""
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self, text="", font=('normal', 40), width=5, height=2,
                                                   command=lambda r=row, c=col: self.human.make_move(self, r, c),
                                                   bg="dark blue", fg="white")
                self.buttons[row][col].grid(row=row, column=col)

    def find_best_move(self):
        """Find best AI move using Minimax while prioritizing winning/blocking moves."""
        best_score = float('-inf')
        best_move = None
        alpha, beta = float('-inf'), float('inf')

        possible_moves = [(row, col) for row in range(3) for col in range(3) if self.buttons[row][col]["text"] == ""]

        # Prioritize winning moves first
        for row, col in possible_moves:
            self.buttons[row][col]["text"] = "X"
            if self.check_winner():  # Instant win
                self.buttons[row][col]["text"] = ""  # Undo temporary move
                return (row, col)  # Make the winning move immediately
            self.buttons[row][col]["text"] = ""  # Undo move

        # Evaluate Minimax for best decision
        for row, col in possible_moves:
            self.buttons[row][col]["text"] = "X"
            score = self.minimax(0, alpha, beta, False)
            self.buttons[row][col]["text"] = ""

            if score > best_score:
                best_score = score
                best_move = (row, col)

            alpha = max(alpha, best_score)
            if beta <= alpha:
                break

        return best_move

    def minimax(self, depth, alpha, beta, is_maximizing):
        """Minimax algorithm with alpha-beta pruning."""
        if self.check_winner():
            return 1 if self.current_player == "X" else -1
        if self.check_draw():
            return 0
        if depth >= 5:
            return 0

        original_player = self.current_player
        best_score = float('-inf') if is_maximizing else float('inf')

        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]["text"] == "":
                    self.buttons[row][col]["text"] = "X" if is_maximizing else "O"
                    self.current_player = "X" if is_maximizing else "O"
                    score = self.minimax(depth + 1, alpha, beta, not is_maximizing)
                    self.buttons[row][col]["text"] = ""
                    self.current_player = original_player

                    if is_maximizing:
                        best_score = max(best_score, score)
                        alpha = max(alpha, best_score)
                    else:
                        best_score = min(best_score, score)
                        beta = min(beta, best_score)

                    if beta <= alpha:
                        break

        return best_score

    def check_winner(self):
        """Check if X or O has won."""
        players = ["X", "O"]  # Check both players instead of only self.current_player

        for player in players:
            for row in range(3):
                if all(self.buttons[row][col]["text"] == player for col in range(3)):
                    return True
            for col in range(3):
                if all(self.buttons[row][col]["text"] == player for row in range(3)):
                    return True
            if all(self.buttons[i][i]["text"] == player for i in range(3)):
                return True
            if all(self.buttons[i][2 - i]["text"] == player for i in range(3)):
                return True

        return False

    def check_draw(self):
        """Check if the game is a draw."""
        return all(self.buttons[row][col]["text"] != "" for row in range(3) for col in range(3))

    def reset_board(self, message):
        """Display result and reset board."""
        self.status_label.config(text=message)
        self.update_idletasks()
        self.after(2000, self.start_new_game)

    def start_new_game(self):
        """Begin a new round with alternating start player."""
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""

        TicTacToe.alternate_starting_player = "X" if TicTacToe.alternate_starting_player == "O" else "O"
        self.current_player = TicTacToe.alternate_starting_player
        self.status_label.config(text=f"New game: Player {self.current_player}'s turn")

        if self.current_player == "X":
            self.computer.make_move(self)

    def process_turn(self):
        """Handle move completion and turn switching."""
        if self.check_winner():
            self.reset_board(f"Player {self.current_player} wins!")
        elif self.check_draw():
            self.reset_board("It's a draw!")
        else:
            self.current_player = "X" if self.current_player == "O" else "O"
            self.status_label.config(text=f"Player {self.current_player}'s turn")
            if self.current_player == "X":
                self.computer.make_move(self)

if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop()