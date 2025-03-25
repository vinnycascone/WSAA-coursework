import requests

# Step 1: Shuffling a new deck
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(shuffle_url).json()
deck_id = response["deck_id"]

# Step 2: Drawing 5 cards
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
draw_response = requests.get(draw_url).json()
cards = draw_response["cards"]

# Step 3: Printing the drawn cards
card_values = []
card_suits = []

print("\nYou drew:")
for card in cards:
    value = card["value"]
    suit = card["suit"]
    print(f"{value} of {suit}")
    card_values.append(value)
    card_suits.append(suit)

# Step 4: Converting card values to numerical values for easier checking
value_map = {
    "ACE": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "JACK": 11, "QUEEN": 12, "KING": 13
}
numeric_values = sorted([value_map[v] for v in card_values if v in value_map])

# Step 5: Checking for pairs, triples, straight, and flush
from collections import Counter

value_counts = Counter(card_values)
suit_counts = Counter(card_suits)

has_pair = any(count == 2 for count in value_counts.values())
has_triple = any(count == 3 for count in value_counts.values())
is_straight = numeric_values == list(range(min(numeric_values), min(numeric_values) + 5))
is_flush = any(count == 5 for count in suit_counts.values())

# Step 6: Congratulate the user
if is_flush:
    print("\n🎉 Congratulations! You got a Flush (All cards of the same suit)!")
elif is_straight:
    print("\n🎉 Congratulations! You got a Straight (Five consecutive numbers)!")
elif has_triple:
    print("\n🎉 Congratulations! You got a Triple (Three cards of the same rank)!")
elif has_pair:
    print("\n🎉 Congratulations! You got a Pair (Two cards of the same rank)!")
else:
    print("\nBetter luck next time!")

