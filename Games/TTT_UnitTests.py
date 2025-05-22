from TicTacToe import TicTacToe
import unittest


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        """Initialize a fresh game instance before each test."""
        self.game = TicTacToe()

    def test_empty_board_no_winner(self):
        """Verify that an empty board has no winner."""
        self.assertFalse(self.game.check_winner())

    def test_draw_condition(self):
        """Ensure the game correctly detects a draw scenario."""
        draw_board = [
            ["X", "O", "X"],
            ["X", "X", "O"],
            ["O", "X", "O"]
        ]
        self.set_board(draw_board)
        self.assertTrue(self.game.check_draw())

    def test_all_winning_conditions(self):
        """Test multiple win scenarios using parameterized tests."""
        winning_boards = [
            (["X", "X", "X"], ["O", "", "O"], ["", "", ""]),
            (["O", "", "O"], ["X", "X", "X"], ["", "", ""]),
            (["X", "", "O"], ["", "X", "O"], ["", "", "X"]),
            (["", "", "X"], ["", "X", "O"], ["X", "O", "X"])
        ]

        for board in winning_boards:
            with self.subTest(board=board):
                self.set_board(board)
                self.assertTrue(self.game.check_winner())

    def test_minimax_optimal_move(self):
        """Ensure Minimax correctly picks the best move."""
        board_state = [
            ["X", "O", "X"],
            ["O", "X", ""],
            ["", "", "O"]
        ]
        self.set_board(board_state)
        best_move = self.game.find_best_move()
        expected_moves = [(2, 0), (2, 1)]  # AI might pick either winning move
        self.assertIn(best_move, expected_moves)

    def test_no_invalid_moves(self):
        """Check that AI never makes illegal moves."""
        board_state = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["X", "O", "X"]
        ]
        self.set_board(board_state)
        best_move = self.game.find_best_move()
        self.assertIsNone(best_move)  # AI should return None as the board is full

    def set_board(self, board_state):
        """Helper method to configure the board for testing."""
        for row in range(3):
            for col in range(3):
                self.game.buttons[row][col]["text"] = board_state[row][col]

if __name__ == "__main__":
    unittest.main()