from random import shuffle
from card import Card

class Deck:
  def __init__(self):
    suits_and_values = sum([[(suit, val + 2) for val in range(13)] for suit in ['C', 'D', 'H', 'S']], [])
    self.cards = [Card(suit, value) for suit, value in suits_and_values]

  def deal(self, num):
    return [self.cards.pop() for _ in range(num)]

  def shuffle(self):
    shuffle(self.cards)