from Card import Card
from Deck import Deck
from Hand import Hand


def print_menu():
    print('''
     __MENU____________________________________________________________ 
    |                                                                  |
    |  r - Show the rule                                               |
    |  n - Play a new game (deck is shuffled again and give new hand)  |
    |  q - Quit                                                        |
    |__________________________________________________________________|         
    ''')

def display_rule():
    print('''
    The deck has 52 cards, 13 of each suit (Spades, Clubs, Hearts, Diamonds)
    The deck is shuffled at the beginning of the game
    The 5 cards on top of the deck will be given to you as a hand of cards
    You can choose to replace none OR some OR all of their cards once  # Typing index: 1 2 3 4 5, separated by space
    Then your hand will be scored\n                    
    No pair:         5 cards that don\'t match any the hands below
    One pair:        2 cards have same value
    Two pairs:       2 pairs of cards that have the same value
    Three of a kind: 3 cards have the same value
    Straight:        5 cards with consecutive values    # Ace could be: [A 2 3 4 5] or [10 J Q K A]
    Flush:           5 cards have same suit
    Full house:      Three of a kind + One pair          
    Four of a kind:  4 cards have same value
    Straight Flush:  Straight + Flush (5 cards same suit and have consecutive values)
    Royal Flush:     [10 J Q K A] same suit
    ''')

def replace_cards(hand):
    ''' Replace cards from the top of the deck '''
    user_input = input('Enter positions of cards you wanna replace: ').split()
    if user_input:
        indices = [int(index) for index in user_input]
        hand.deck.replace_cards(indices)    

def new_game():
    ''' Creates a new game with new shuffled deck and new hand '''
    print('\nNEW GAME\n')
    hand = Hand()
    print('Here is your hand')
    hand.print_hand()
    print()
    replace_cards(hand)
    hand.check_hand()
    print('\nYour new hand\n')
    hand.print_hand()
    print(f'\nYour hand is {hand.type} \n')

if __name__ == '__main__':
    print('\n\nWelcome to VIDEO POKER game\n')
    print('You can choose each of these options\n')
    print_menu()
    option = input('Your option: ')
    while option != 'q':
        token = 0
        if option == 'r':
            display_rule()
        elif option == 'n':
            new_game()
        else:
            print('Wrong input')

        print_menu()
        option = input('Your option: ')   

    
