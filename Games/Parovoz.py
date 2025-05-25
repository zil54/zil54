import pygame
import random
from abc import ABC, abstractmethod
# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 900, 700
CARD_WIDTH, CARD_HEIGHT = 75, 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Player Card Game")


class CardBase(ABC):
    """Abstract class representing a card."""
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.name = f"{rank}_of_{suit}"

    @abstractmethod
    def get_image(self):
        """Must be implemented by subclasses to return card image."""
        pass

class Card(CardBase):
    """Concrete card implementation with an image."""
    def __init__(self, rank, suit):
        super().__init__(rank, suit)
        self.image = pygame.transform.scale(pygame.image.load(f"cards/{self.name}.png"), (CARD_WIDTH, CARD_HEIGHT))

    def get_image(self):
        return self.image




class Deck:
    def __init__(self):
        self.cards = self.generate_deck()
        random.shuffle(self.cards)

    def generate_deck(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        return [Card(rank, suit) for suit in suits for rank in ranks]

    def draw_card(self):
        return self.cards.pop() if self.cards else None

class PlayerBase(ABC):
    """Abstract class for player behavior."""
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.play_area = []

    @abstractmethod
    def draw_card(self, deck):
        pass

class Player(PlayerBase):
    """Concrete Player implementation."""
    def __init__(self, name, y_position, play_area_y):
        super().__init__(name)
        self.y_position = y_position
        self.play_area_y = play_area_y

    def draw_card(self, deck):
        if len(self.cards) < 6:
            card = deck.draw_card()
            if card:
                x_position = 50 + len(self.cards) * (CARD_WIDTH + 10)
                self.cards.append((card, (x_position, self.y_position)))


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player1 = Player("Player 1", HEIGHT - 250, HEIGHT - 400)
        self.player2 = Player("Player 2", 100, 250)
        self.dragging_card = None
        self.dragging_position = (0, 0)
        self.deal_initial_cards()
        self.last_played_suit = None  # Tracks last played suit
        self.last_played_rank = None  # Tracks last played rank

    def deal_initial_cards(self):
        for _ in range(6):
            self.player1.draw_card(self.deck)
            self.player2.draw_card(self.deck)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for card_tuple in self.player1.cards + self.player2.cards:
                    card, position = card_tuple
                    x, y = position
                    if x <= mouse_x <= x + CARD_WIDTH and y <= mouse_y <= y + CARD_HEIGHT:
                        self.dragging_card = card_tuple
                        self.dragging_position = (mouse_x - CARD_WIDTH // 2, mouse_y - CARD_HEIGHT // 2)
            elif event.type == pygame.MOUSEMOTION:
                if self.dragging_card:
                    self.dragging_position = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.dragging_card:
                    mouse_x, mouse_y = event.pos

                    # Check if card is dropped into Player 1's play area
                    if HEIGHT - 450 <= mouse_y <= HEIGHT - 350:
                        self.player1.play_area.append((self.dragging_card[0], self.dragging_position))
                        self.player1.cards.remove(self.dragging_card)

                    # Check if card is dropped into Player 2's play area
                    elif 200 <= mouse_y <= 300:
                        self.player2.play_area.append((self.dragging_card[0], self.dragging_position))
                        self.player2.cards.remove(self.dragging_card)

                    self.dragging_card = None
        return True

    def render(self):
        screen.fill((34, 139, 34))

        # Draw play areas
        pygame.draw.rect(screen, (0, 100, 0), (50, HEIGHT - 450, WIDTH - 100, 100))
        pygame.draw.rect(screen, (0, 100, 0), (50, 200, WIDTH - 100, 100))

        # Draw player cards
        for player in [self.player1, self.player2]:
            for card_tuple in player.cards:
                card, position = card_tuple
                screen.blit(card.image, position)

        # Draw cards in play areas
        for card_tuple in self.player1.play_area:
            card, position = card_tuple
            screen.blit(card.image, position)

        for card_tuple in self.player2.play_area:
            card, position = card_tuple
            screen.blit(card.image, position)

        # Draw remaining deck
        if self.deck.cards:
            back_card_image = pygame.transform.scale(pygame.image.load("cards/card_back.png"),
                                                     (CARD_WIDTH, CARD_HEIGHT))
            screen.blit(back_card_image, (WIDTH - 150, HEIGHT // 2))
            font = pygame.font.Font(None, 36)
            text_surface = font.render(str(len(self.deck.cards)), True, (255, 255, 255))
            screen.blit(text_surface, (WIDTH - 100, HEIGHT // 2 + CARD_HEIGHT + 10))

        # Handle dragging
        if self.dragging_card:
            screen.blit(self.dragging_card[0].image, self.dragging_position)

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.render()

        pygame.quit()

# Run the game
game = Game()
game.run()