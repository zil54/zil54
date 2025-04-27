import tkinter as tk
import random

# Initialize main application window
window = tk.Tk()
window.title("Two Player Card Game")
window.geometry("800x600")

# Helper function to generate a deck of cards
def get_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [f"{rank} of {suit}" for suit in suits for rank in ranks]

deck = get_deck()
random.shuffle(deck)

# Function to load card images
def load_card_images():
    card_images = {}
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    ranks = ['4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    for suit in suits:
        for rank in ranks:
            card_name = f"{rank}_of_{suit}"
            card_images[card_name] = tk.PhotoImage(file=f"cards/{card_name}.png")
    return card_images

# Load card images
card_images = load_card_images()

# Players' hands
player1_cards = []
player2_cards = []

# Functions to draw cards for each player
def draw_card(player):
    global deck, player1_cards, player2_cards

    if deck:
        card = deck.pop()
        card_name = card.split()[0].lower() + "_of_" + card.split()[2].lower()
        card_image = card_images[card_name]

        if player == "Player 1":
            player1_cards.append(card)
            player1_label.config(text="Player 1's Cards: " + ', '.join(player1_cards))
            card_label1.config(image=card_image)
            card_label1.image = card_image
        elif player == "Player 2":
            player2_cards.append(card)
            player2_label.config(text="Player 2's Cards: " + ', '.join(player2_cards))
            card_label2.config(image=card_image)
            card_label2.image = card_image

# Create UI elements
player1_label = tk.Label(window, text="Player 1's Cards:", font=('Helvetica', 14))
player1_label.pack(pady=5)
card_label1 = tk.Label(window)
card_label1.pack()

player2_label = tk.Label(window, text="Player 2's Cards:", font=('Helvetica', 14))
player2_label.pack(pady=5)
card_label2 = tk.Label(window)
card_label2.pack()

draw1_button = tk.Button(window, text="Draw for Player 1", command=lambda: draw_card("Player 1"))
draw1_button.pack(pady=10)

draw2_button = tk.Button(window, text="Draw for Player 2", command=lambda: draw_card("Player 2"))
draw2_button.pack(pady=10)

# Run the application
window.mainloop()



player2_label = tk.Label(window, text="Player 2's Cards: ", font=('Helvetica', 14))
player2_label.pack(pady=10)

draw1_button = tk.Button(window, text="Draw for Player 1", command=lambda: draw_card("Player 1"))
draw1_button.pack(pady=10)

draw2_button = tk.Button(window, text="Draw for Player 2", command=lambda: draw_card("Player 2"))
draw2_button.pack(pady=10)

# Run the application
window.mainloop()
