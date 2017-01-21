from card import Card
from deck import Deck

deck = Deck()
deck.shuffle()

player_hand = deck.deal(2)
dealer_hand = deck.deal(2)

while True:
  print("Your hand:")
  print(player_hand)

  print("Dealer hand:")
  print(dealer_hand)

  print("Hit? ")
  hit = raw_input()
  if hit == 'y':
    player_hand.append(deck.deal(1)[0])
  else:
    break

def calculate_score(hand):
  return sum(map(lambda x: x.score(), hand))

player_score = calculate_score(player_hand)
dealer_score = calculate_score(dealer_hand)

print("Your score: {0}".format(player_score))
print("Dealer score: {0}".format(dealer_score))

if abs(21 - player_score) < abs(21 - dealer_score):
  print("You won!")
else:
  print("You lost")


