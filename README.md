### Blackjack Game in Python - README

This project is a simple Python-based Blackjack game that allows users to play against a dealer in a simulated card game. The game involves standard Blackjack rules, with options to draw cards, check scores, and decide whether to continue playing or stop. The code is designed for terminal-based interaction and follows the basic structure of a card game simulation.

#### Key Features:
1. **Deck of Cards Simulation:**
   - The game uses a deck of cards, with suits (Hearts, Diamonds, Clubs, Spades) and ranks (2-10, Jack, Queen, King, Ace).
   - Aces are treated as either 1 or 11 depending on the player’s current score, avoiding busts over 21.

2. **Randomized Card Drawing:**
   - Cards are randomly selected using the `random` module, ensuring a unique game experience each time.
   - The game provides both player and dealer with initial cards and continues as the player decides whether to "hit" or "pass."

3. **Score Calculation:**
   - The game tracks and updates both the player’s and dealer’s scores in real-time.
   - Dealer follows standard Blackjack rules, drawing cards until reaching a score of at least 17.
   
4. **Win/Loss Determination:**
   - The game ends when either the player or the dealer exceeds 21 ("bust") or when the player chooses to stop drawing cards.
   - The final scores are compared, and the game determines whether the player wins, loses, or the game ends in a draw.

5. **Replayability:**
   - After each game, the player has the option to play again, with the screen cleared for a fresh start.

#### Characteristics of the Code:
- **Modular Functions**: Functions like `random_card()`, `initial_cards()`, and `choose_card()` make the code clean, reusable, and easy to maintain.
- **Game Logic**: The game handles the core Blackjack rules and provides clear feedback based on user input and dealer actions.
- **User Input Handling**: The program accepts simple 'y'/'n' inputs for drawing cards and restarting the game, ensuring a user-friendly interface.
- **Ace Handling**: Special logic ensures that Aces (value [1, 11]) adjust to prevent busting.

#### Requirements:
- Python 3.x
- `random` and `os` modules (part of the standard library)

#### How to Play:
1. Run the Python script.
2. The game starts with two cards dealt to both the player and the dealer.
3. Decide whether to draw another card by typing 'y' (yes) or 'n' (no).
4. The game continues until the player busts or chooses to stop, at which point the dealer will draw cards as per Blackjack rules.
5. Scores are compared to determine the winner.
6. Replay or exit as desired.

This Blackjack game provides a fun and simple way to experience Blackjack through code, with replayability and automated score management!
