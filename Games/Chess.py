import pygame

# Constants
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8
WHITE = (238, 238, 210)
GREEN = (118, 150, 86)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# Load piece images
piece_images = {
    "bp": pygame.image.load("chess/black_pawn.png"),
    "wp": pygame.image.load("chess/white_pawn.png"),
    "bn": pygame.image.load("chess/black_knight.png"),
    "wn": pygame.image.load("chess/white_knight.png"),
    "bb": pygame.image.load("chess/black_bishop.png"),
    "wb": pygame.image.load("chess/white_bishop.png"),
    "br": pygame.image.load("chess/black_rook.png"),
    "wr": pygame.image.load("chess/white_rook.png"),
    "bk": pygame.image.load("chess/black_king.png"),
    "wk": pygame.image.load("chess/white_king.png"),
    "bq": pygame.image.load("chess/black_queen.png"),
    "wq": pygame.image.load("chess/white_queen.png"),
}

class Board:
    """Chessboard with piece rendering and legal move validation."""
    def __init__(self):
        self.grid = [
            ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
            ["bp"] * 8,
            [""] * 8, [""] * 8, [""] * 8, [""] * 8,
            ["wp"] * 8,
            ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
        ]
        self.selected_piece = None
        self.selected_pos = None

    def draw(self):
        """Draw the board and pieces."""
        for row in range(8):
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else GREEN
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                piece = self.grid[row][col]
                if piece and (row, col) != self.selected_pos:
                    screen.blit(piece_images[piece], (col * SQUARE_SIZE + 10, row * SQUARE_SIZE + 10))

        if self.selected_piece:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            screen.blit(piece_images[self.selected_piece], (mouse_x - SQUARE_SIZE//2, mouse_y - SQUARE_SIZE//2))

    def handle_mouse_down(self, x, y):
        """Select a piece when clicked."""
        row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
        if self.grid[row][col]:  # Only select if a piece is present
            self.selected_piece = self.grid[row][col]
            self.selected_pos = (row, col)
            self.grid[row][col] = ""  # Temporarily clear piece for dragging

    def handle_mouse_up(self, x, y):
        """Drop piece at new position if legal."""
        if self.selected_piece:
            row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
            if self.is_legal_move(self.selected_pos[0], self.selected_pos[1], row, col):
                self.grid[row][col] = self.selected_piece  # Place piece
            else:
                self.grid[self.selected_pos[0]][self.selected_pos[1]] = self.selected_piece  # Revert move

            self.selected_piece = None
            self.selected_pos = None  # Reset selection

    def is_legal_move(self, start_row, start_col, end_row, end_col):
        """Validate moves based on piece type."""
        piece = self.selected_piece
        if not piece:
            return False

        # Pawn movement rules
        if "p" in piece:
            direction = 1 if "w" in piece else -1  # White moves up, black moves down
            if start_col == end_col and (end_row == start_row + direction):  # Regular move
                return True
            elif abs(start_col - end_col) == 1 and end_row == start_row + direction and self.grid[end_row][end_col]:  # Capture
                return True

        # Rook movement rules
        elif "r" in piece:
            if start_row == end_row or start_col == end_col:  # Vertical or horizontal moves
                return self.is_clear_path(start_row, start_col, end_row, end_col)

        # Knight movement rules
        elif "n" in piece:
            if abs(end_row - start_row) * abs(end_col - start_col) == 2:  # "L" shape movement
                return True

        # Bishop movement rules
        elif "b" in piece:
            if abs(start_row - end_row) == abs(start_col - end_col):  # Diagonal movement
                return self.is_clear_path(start_row, start_col, end_row, end_col)

        # Queen movement rules
        elif "q" in piece:
            if start_row == end_row or start_col == end_col or abs(start_row - end_row) == abs(start_col - end_col):  # Rook + Bishop moves
                return self.is_clear_path(start_row, start_col, end_row, end_col)

        # King movement rules
        elif "k" in piece:
            if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:  # Moves one square in any direction
                return True

        return False

    def is_clear_path(self, start_row, start_col, end_row, end_col):
        """Check if path is clear for Rook, Bishop, Queen moves."""
        row_step = 1 if end_row > start_row else -1 if end_row < start_row else 0
        col_step = 1 if end_col > start_col else -1 if end_col < start_col else 0

        r, c = start_row + row_step, start_col + col_step
        while (r, c) != (end_row, end_col):
            if self.grid[r][c]:  # Path blocked
                return False
            r += row_step
            c += col_step

        return True

class ChessGame:
    """Main game manager."""
    def __init__(self):
        self.board = Board()
        self.running = True

    def run(self):
        """Main game loop."""
        while self.running:
            screen.fill((0, 0, 0))
            self.board.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.board.handle_mouse_down(*event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.board.handle_mouse_up(*event.pos)

            pygame.display.flip()

# Run the game
game = ChessGame()
game.run()
pygame.quit()