class Card:
    
    # Dictionaries for printing purpose
    suit = {'Spades': '♠', 'Diamonds': '♦', 'Hearts': '♥', 'Clubs': '♣'} 
    value = {11: 'J', 12: 'Q', 13: 'K', 1: 'A'}

    ''' Represent a single card '''

    # CTOR
    def __init__(self, suit='Spades', value=1):
        self.suit = suit        
        self.value = value

    def copy_card(self, card):
        self.suit = card.suit
        self.value = card.value

    # PRINT
    def __str__(self):      # Tested
        # Special case: Value = 10
        if self.value == 10:
            return (f' ___ \n'                      # The top edge of the card   ___
                f'|{self.value} |\n'                # First row of the card     |10 |  (Has width = 5 spaces)
                f'| {Card.suit[self.suit]} |\n'     # Second row of the card    | ♦ |  (Has suit in the center)
                f'|_{self.value}|')                 # Last row // Bottom edge   |_10|  
                                                    # (Only had 1 underscore because "10" already occupy 2 spaces)
        
        # Value is 1 or 10 or 11 or 12 or 13 -> Need to convert to Symbol
        elif self.value in Card.value:
            return (f' ___ \n'                      # Top edge of the card       ___
                f'|{Card.value[self.value]}  |\n'   # First row                 |K  |
                f'| {Card.suit[self.suit]} |\n'     # Second row                | ♣ |
                f'|__{Card.value[self.value]}|')    # Last row // Bottom edge   |__K|

        # Other 1-digit value
        else:
            return (f' ___ \n'                      # Top edge of the card       ___
                f'|{self.value}  |\n'               # First row                 |2  |
                f'| {Card.suit[self.suit]} |\n'     # Second row                | ♠ |
                f'|__{self.value}|')                # Last row // Bottom edge   |__2|
        


                






