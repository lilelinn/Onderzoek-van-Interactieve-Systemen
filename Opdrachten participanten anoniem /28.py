# schrijf hier je code
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def description(self):
        return f"{self.suit} of {self.value}"


class Deck:
    def __init__(self):
        self._suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        self._values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self._cards = []

        for suit in self._suits:
            for value in self._values:
                self._cards.append(Card(suit,value))


if __name__ == "__main__":
    # schrijf je test hier
    # test door middel van de 'play button' rechtsboven
    
    # test class Card
    card = Card(suit='Spades', value='Ace')
    print(card.description())
    
    # test class Deck
    my_deck = Deck()
    print(f"Deck created with {len(my_deck._cards)}")
    for card in my_deck._cards:
        print(f"Card: {card.value} of {card.suit}")
    

