import cards
import random


def test_shuffle():
    deck = Deck()
    deck.shuffle_deck()
    for c in deck.return_deck():
        print(c.name_of_card())
def test_draw():
    deck = Deck()
    deck.shuffle_deck()
    for i in range(1):
        print(i)
        hand = deck.draw(num_of_cards = 5)
        for c in hand:
            print(c.name_of_card())

protocol = test_draw

class Deck:
  def __init__(self):
    self.cards = []
    suits = ['D','H','S','C']
    for suit in suits:
      for rank in range(2,15):
        self.cards.append(cards.Card(rank,suit))
  def return_deck(self):
    return self.cards
  def shuffle_deck(self):
    random.shuffle(self.cards) 
  def draw(self,num_of_cards):
    hand = []
    for i in range(num_of_cards):
        try:
            hand.append(self.cards.pop(0))
        except IndexError:
            print("end of deck")


    return hand


if __name__ == "__main__":
    protocol()