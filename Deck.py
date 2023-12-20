import random
from Card import Card

class Deck:

    TOP = 5     # Index of the card on top of the deck

    def __init__(self):
        self.deck = []     # List of 52 Cards
        self.set_up_deck()
        self.shuffle()


    # SET UP
    def set_up_deck(self):  
        ''' Set up the deck'''
        for value in range(1, 14):
            for suit in Card.suit:
                self.deck.append(Card(suit, value))

    def shuffle(self):      
        ''' Shuffle the deck '''
        for i in range (52):
            random_value = random.randrange(52)
            self.deck[i], self.deck[random_value] = self.deck[random_value], self.deck[i]

    # MUTATOR
    def replace_cards(self, indices):   
        ''' Take out cards and replace new ones '''
        ''' indices: a list contains indices need replacing '''

        for index in indices:
            current = self.deck[index - 1]
            card_top = self.deck[Deck.TOP]
            self.deck.append(Card(current.suit, current.value))
            current.copy_card(card_top)
            self.deck.pop(Deck.TOP)
    
    def print_deck(self):
        for card in self.deck:
            print(card)


