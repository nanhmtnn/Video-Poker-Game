# Video-Poker-Game
Video Poker Game by Python


''' Introduction 

    My game is Video Poker, where the user will be given 5 cards and their score will be based on 
    which hand they get. The game will start with a welcome message
    Then a menu of options will be show to them like this:

      __MENU____________________________________________________________ 
    |                                                                  |
    |  r - Show the rule                                               |
    |  c - Play a new game (deck is shuffled again and give new hand)  |
    |  q - Quit                                                        |
    |__________________________________________________________________|

    The rule of the game will be shown when the user presses 'r'
    The game starts when they press 'c'

    The 5 cards will be showns as below:
    Here is your hand
         ___ 
        |8  |
        | ♠ |
        |__8|
         ___ 
        |A  |
        | ♠ |
        |__A|
         ___ 
        |Q  |
        | ♦ |
        |__Q|
         ___ 
        |3  |
        | ♥ |
        |__3|
         ___ 
        |4  |
        | ♥ |
        |__4|

    Then they can choose which position(s) they want to replace. For example, if they want to replace
    the last 3 cards, they will input 3 4 5 (separated by whitespace)

'''

''' Overview of the program
    There are 4 classes in total:
        Card: represents a single card object, has value and suit for each card
        Deck: represents a whole deck with 52 cards, 13 of each suit
        Hand: represents a hand of 5 cards
        Poker: stimulates the video poker game based on the rule below
'''

''' Rule of Video Poker game

    The deck has 52 cards, 13 of each suit (Spades, Clubs, Hearts, Diamonds)
    The deck is shuffled at the beginning of the game
    The 5 cards on top of the deck will be given to the user as a hand of cards
    The user can choose to replace none OR some OR all of their cards once
    Then their hand will be scored

    No pair:         5 cards that don't match any the hands below 
    One pair:        2 cards have same value
    Two pairs:       2 pairs of cards that have the same value
    Three of a kind: 3 cards have the same value
    Straight:        5 cards with consecutive values    # Ace could be: [A 2 3 4 5] or [10 J Q K A]
    Flush:           5 cards have same suit
    Full house:      Three of a kind + One pair
    Four of a kind:  4 cards have same value
    Straight Flush:  Straight + Flush (5 cards same suit and have consecutive values)
    Royal Flush:     [10 J Q K A] same suit

'''
