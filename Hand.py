from Card import Card
from Deck import Deck

class Hand:

    # Hand string
    NO_PAIR = 'No Pair'
    ONE_PAIR = 'One Pair'                   # 2 cards have same value
    TWO_PAIRS = 'Two Pairs'                 # 2 pairs of cards that have the same value
    THREE_OF_A_KIND = 'Three of a kind'     # 3 cards have the same value
    STRAIGHT = 'Straight'                   # 5 cards with consecutive values    # Ace could be: [A 2 3 4 5] or [10 J Q K A]
    FLUSH = 'Flush'                         # 5 cards have same suit
    FULL_HOUSE = 'Full House'               # Three of a kind + One pair
    FOUR_OF_A_KIND = 'Four of a kind'       # 4 cards have same value
    STRAIGHT_FLUSH = 'Straight Flush'       # Straight + Flush (5 cards same suit and have consecutive values)
    ROYAL_FLUSH = 'Royal Flush'             # [10 J Q K A] same suit

    # CTOR
    def __init__(self):
        self.deck = Deck()
        self.hand = self.deck.deck[0:5]     # List of 5 Card(s)
        self.type = ''


    # PRINT
    def print_hand(self):
        for card in self.hand:
            print(card)


    # CHECK

    def check_hand(self):
        if self.royal_flush():
            self.type = Hand.ROYAL_FLUSH
        elif self.straight_flush():
            self.type = Hand.STRAIGHT_FLUSH
        elif self.four_of_a_kind():
            self.type = Hand.FOUR_OF_A_KIND
        elif self.full_house():
            self.type = Hand.FULL_HOUSE
        elif self.flush():
            self.type = Hand.FLUSH
        elif self.straight():
            self.type = Hand.STRAIGHT
        elif self.three_of_a_kind():
            self.type = Hand.THREE_OF_A_KIND
        elif self.two_pairs():
            self.type = Hand.TWO_PAIRS
        elif self.one_pair():
            self.type = Hand.ONE_PAIR
        else:
            self.type = Hand.NO_PAIR

    def one_pair(self):
        one_pair = False
        values = self.value_list()
        count = self.count_value(values)
        if 2 in count.values() and len(count) != 3:
            one_pair = True
        return one_pair

    def two_pairs(self):
        two_pairs = False
        values = self.value_list()
        count = self.count_value(values)
        if 2 in count.values() and len(count) == 3:
            two_pairs = True
        return two_pairs

    def three_of_a_kind(self):  # Tested
        three_of_a_kind = False
        values = self.value_list()
        count = self.count_value(values)
        if 3 in count.values():
            three_of_a_kind = True
        return three_of_a_kind

    # [A 2 3 4 5] or [10 J Q K A]
    def straight(self):    
        straight = True

        if self.special(): # [10 J Q K A]
            return straight
        
        values = self.value_list()
        
        for i in range(len(values) - 1):
            if values[i] != values[i + 1] - 1:
                straight = False
                break
        
        return straight
        
    def flush(self):   
        flush = True
        for i in range(len(self.hand) - 1):
            if self.hand[i].suit != self.hand[i+1].suit:
                flush = False
                break
        return flush

    def full_house(self):   
        full_house = False
        values = self.value_list()
        count = self.count_value(values)
        if 3 in count.values() and 2 in count.values():
            full_house = True
        return full_house

    def four_of_a_kind(self):  
        four_of_a_kind = False
        values = self.value_list()
        count = self.count_value(values)
        if 4 in count.values():
            four_of_a_kind = True
        return four_of_a_kind
    
    def straight_flush(self):   
        return self.straight() and self.flush()

    def royal_flush(self):  
        return self.special() and self.flush()
    

    # Support Methods

    def special(self):  # Tested
        sample = [1, 10, 11, 12, 13] # [10 J Q K A]
        values = self.value_list()
        return values == sample

    def value_list(self):
        values = []
        for card in self.hand:
            values.append(card.value)
        values.sort()
        return values
    
    def count_value(self, values):
        count = {}
        for i in values:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        return count
        