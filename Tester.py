from Card import Card
from Deck import Deck
from Hand import Hand

''' Unit Tests '''

# TEST 1: Print some cards to test override function
def test_print():

    print('\nTesting overload printing function -----------------------')
    card1 = Card('Spades', 2)
    print(card1)
    card2 = Card('Hearts', 10)
    print(card2)
    card3 = Card('Clubs', 12)
    print(card3)

    # Output:
    # Testing override printing function -----------------------
    #  ___ 
    # |2  |
    # | ♠ |
    # |__2|
    #  ___ 
    # |10 |
    # | ♥ |
    # |_10|
    #  ___ 
    # |Q  |
    # | ♣ |
    # |__Q|

# TEST 2: Print the whole deck
#         Make sure no card is missing when set up the deck and shuffle
def test_print_deck():
    deck = Deck()
    for card in deck.get_deck():
        print(card)

    print(deck.check_enough_cards())

# TEST 3: Test replace cards # About reference
def test_replace(how_many):
    
    card1 = Card('Spades', 2)
    card2 = Card('Hearts', 3)
    card3 = Card('Clubs', 4)
    card4 = Card('Diamonds', 5)
    card5 = Card('Spades', 6)

    deck = [card1, card2, card3, card4, card5]
    top = 2
    
    hand = deck[0:2]  
    print('DECK')
    for card in deck:
        print(card)

    print('HAND')
    for card in hand:
        print(card)

    for index in how_many:
        print(f'Index: {index}')
        print(deck[index])
        deck.append(Card(deck[index].get_suit(), deck[index].get_value()))
        deck[index].copy_card(deck[top])
        deck.pop(top)
        print(f'After pop: {len(deck)}')

    print('DECK')
    for card in deck:
        print(card)

    print('HAND')
    for card in hand:
        print(card)

# TEST 4: Test replace method in Deck
def test_replace_method():
    hand = Hand()
    hand.get_deck().print_deck()
    user_input = input('Enter indices: ').split()
    indices = [int(index) for index in user_input]
    hand.get_deck().replace_cards(indices)
    # print()
    # print()
    # hand.get_deck().print_deck()

    print('\n\n')
    hand.print_hand()

# TEST 5: Another test for replace method in Deck
def test_deck(indices):
    deck = Deck()
    deck.print_deck()
    print('\n\n\n')
    for index in indices:
        current = deck.get_deck()[index]
        card_top = deck.get_deck()[Deck.TOP]
        deck.get_deck().append(Card(current.get_suit(), current.get_value()))
        current.copy_card(card_top)
        deck.get_deck().pop(Deck.TOP)

    deck.print_deck()

def test_pair():
    cards = [1, 1, 1, 1, 3]
    valtup = {}
    for i in cards:
        if i in valtup:
            valtup[i] += 1
        else:
            valtup[i] = 1

    print(valtup)
    print(len(valtup))
    print(valtup.values())
    print(valtup.values() == (4, 1))


# TEST HANDS:
def test_flush():
    card1 = Card('Hearts', 10)
    card2 = Card('Hearts', 1)
    card3 = Card('Hearts', 11)
    card4 = Card('Hearts', 13)
    card5 = Card('Hearts', 12)
    temp = [card1, card2, card3, card4, card5]
    hand = Hand()
    hand.hand = temp
    hand.print_hand()
    print()
    print(hand.royal_flush())

def test_straight():
    card1 = Card('Hearts', 3)
    card2 = Card('Hearts', 1)
    card3 = Card('Hearts', 2)
    card4 = Card('Hearts', 1)
    card5 = Card('Hearts', 2)
    temp = [card1, card2, card3, card4, card5]
    hand = Hand()
    hand.hand = temp
    hand.print_hand()
    print()
    print(hand.one_pair())

def test_check_hand():
    card1 = Card('Hearts', 3)
    card2 = Card('Hearts', 6)
    card3 = Card('Hearts', 5)
    card4 = Card('Hearts', 2)
    card5 = Card('Clubs', 1)
    temp = [card1, card2, card3, card4, card5]
    hand = Hand()
    hand.hand = temp
    hand.print_hand()
    print()
    hand.check_hand()
    print(hand.get_type())



if __name__ == '__main__':

    card1 = Card('Spades', 3)
    card2 = Card('Hearts', 1)
    hand = [card1, card2]

    hand[0], hand[1] = hand[1], hand[0]
    for item in hand:
        print(item)






'''
#  ___ 
# |A  |
# | ♠ |
# |__A|
#  ___ 
# |A  |
# | ♦ |
# |__A|
#  ___ 
# |A  |
# | ♥ |
# |__A|
#  ___ 
# |A  |
# | ♣ |
# |__A|
#  ___ 
# |2  |
# | ♠ |
# |__2|
#  ___ 
# |2  |
# | ♦ |
# |__2|
#  ___ 
# |2  |
# | ♥ |
# |__2|
#  ___ 
# |2  |
# | ♣ |
# |__2|
#  ___ 
# |3  |
# | ♠ |
# |__3|
#  ___ 
# |3  |
# | ♦ |
# |__3|
#  ___ 
# |3  |
# | ♥ |
# |__3|
#  ___ 
# |3  |
# | ♣ |
# |__3|
#  ___ 
# |4  |
# | ♠ |
# |__4|
#  ___ 
# |4  |
# | ♦ |
# |__4|
#  ___ 
# |4  |
# | ♥ |
# |__4|
#  ___ 
# |4  |
# | ♣ |
# |__4|
#  ___ 
# |5  |
# | ♠ |
# |__5|
#  ___ 
# |5  |
# | ♦ |
# |__5|
#  ___ 
# |5  |
# | ♥ |
# |__5|
#  ___ 
# |5  |
# | ♣ |
# |__5|
#  ___ 
# |6  |
# | ♠ |
# |__6|
#  ___ 
# |6  |
# | ♦ |
# |__6|
#  ___ 
# |6  |
# | ♥ |
# |__6|
#  ___ 
# |6  |
# | ♣ |
# |__6|
#  ___ 
# |7  |
# | ♠ |
# |__7|
#  ___ 
# |7  |
# | ♦ |
# |__7|
#  ___ 
# |7  |
# | ♥ |
# |__7|
#  ___ 
# |7  |
# | ♣ |
# |__7|
#  ___ 
# |8  |
# | ♠ |
# |__8|
#  ___ 
# |8  |
# | ♦ |
# |__8|
#  ___ 
# |8  |
# | ♥ |
# |__8|
#  ___ 
# |8  |
# | ♣ |
# |__8|
#  ___ 
# |9  |
# | ♠ |
# |__9|
#  ___ 
# |9  |
# | ♦ |
# |__9|
#  ___ 
# |9  |
# | ♥ |
# |__9|
#  ___ 
# |9  |
# | ♣ |
# |__9|
#  ___ 
# |10 |
# | ♠ |
# |_10|
#  ___ 
# |10 |
# | ♦ |
# |_10|
#  ___ 
# |10 |
# | ♥ |
# |_10|
#  ___ 
# |10 |
# | ♣ |
# |_10|
#  ___ 
# |J  |
# | ♠ |
# |__J|
#  ___ 
# |J  |
# | ♦ |
# |__J|
#  ___ 
# |J  |
# | ♥ |
# |__J|
#  ___ 
# |J  |
# | ♣ |
# |__J|
#  ___ 
# |Q  |
# | ♠ |
# |__Q|
#  ___ 
# |Q  |
# | ♦ |
# |__Q|
#  ___ 
# |Q  |
# | ♥ |
# |__Q|
#  ___ 
# |Q  |
# | ♣ |
# |__Q|
#  ___ 
# |K  |
# | ♠ |
# |__K|
#  ___ 
# |K  |
# | ♦ |
# |__K|
#  ___ 
# |K  |
# | ♥ |
# |__K|
#  ___ 
# |K  |
# | ♣ |
# |__K|
'''