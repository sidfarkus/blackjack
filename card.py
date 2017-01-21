class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

  def score(self):
    return self.value if self.value < 10 else 10

  def __repr__(self):
    value_str = self.value if self.value <= 10 else "JQKA"[self.value - 11]
    return "{0}{1}".format(value_str, self.suit)