import random
import os

os.system('clear')
resume_game = 'y'

deck_of_cards = {
    'Hearts': {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 11]
    },
    'Diamonds': {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 11]
    },
    'Clubs': {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 11]
    },
    'Spades': {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 11]
    }
}

def random_card():
    random_suit = random.choice(list(deck_of_cards.keys()))
    random_rank = random.choice(list(deck_of_cards[random_suit].keys()))
    card_value = deck_of_cards[random_suit][random_rank]
    
    if card_value == [1, 11]:
        card_value = 11

    return [random_suit, random_rank, card_value]

def initial_cards():
    global user_score
    global dealer_score
    for list in deck:
        while len(list) < 2:
            assigned_card = random_card()
            list.append(assigned_card)
    
    # Calculate scores
    user_score = int(deck[0][0][2]) + int(deck[0][1][2])
    dealer_first_card_score = int(deck[1][0][2])
    dealer_score = dealer_first_card_score + int(deck[1][1][2])
    
    # Show initial cards and scores
    print(f"🎉 Welcome to Blackjack! 🎉")
    print(f"----------------------------\n")
    print(f"Your initial cards: {deck[0][0][1]} of {deck[0][0][0]} and {deck[0][1][1]} of {deck[0][1][0]} (Initial Score: {user_score}).\n")
    print(f"Dealer first card: {deck[1][0][1]} of {deck[1][0][0]}. Dealer's second card is hidden. (Initial Score: {dealer_first_card_score}).\n")


def choose_card(chosen_person, num):
    global user_score
    global dealer_score
    new_card = random_card()
    
    if new_card[2] == 11:
        if chosen_person == "you":
            if new_card[2] + user_score > 21:
                new_card[2] = 1
        elif chosen_person == "The dealer":
            if new_card[2] + dealer_score > 21:
                new_card[2] = 1

    deck[num].append(new_card)
    
    if chosen_person == "you":
        user_score += int(new_card[2])
        print(f"You drew {new_card[1]} of {new_card[0]}. Your new total score is {user_score}.\n")
    else:
        dealer_score += int(new_card[2])
        print(f"Dealer draws a third card: {new_card[1]} of {new_card[0]}. Dealer's new total score is {dealer_score}.\n")

while resume_game == 'y':
    deck = [[],[]]
    user_score = 0 
    dealer_score = 0
    initial_cards()
    
    while True:
        if user_score >= 21:
            break

        pick_card = input("Would you like to draw another card? Type 'y' to draw or 'n' to pass: \n").lower()
        
        if pick_card == 'y':
            choose_card("you", 0)

            if user_score > 21:
                print(f"You busted with a score of {user_score}! Game over.\n")
                break

        elif pick_card == 'n':
            print(f"Dealer's second card is revealed: {deck[1][1][1]} of {deck[1][1][0]}. (Total Score: {dealer_score})\n")
            
            # Dealer actions
            while dealer_score < 17:
                choose_card("The dealer", 1)
                
            if dealer_score > 21:
                print(f"The dealer busted with a score of {dealer_score}. You win!\n")
            else:
                print(f"Dealer's final score: {dealer_score}\n")
                
            break  

        else:
            print("Invalid input. Please type 'y' or 'n'.\n")

    if user_score <= 21 and dealer_score <= 21:
        if user_score > dealer_score:
            print(f"You win! Your score of {user_score} beat the dealer's {dealer_score}.\n")
        elif user_score < dealer_score:
            print(f"You lose. Your score of {user_score} was lower than the dealer's {dealer_score}.\n")
        else:
            print("It's a draw!\n")

    resume_game = input("Would you like to play again? (y/n): ").lower()
    if resume_game == 'y':
        os.system('clear')
    else:
        print("Thanks for playing! Goodbye!")
        break
