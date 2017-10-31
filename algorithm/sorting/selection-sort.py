cards = [2, 7, 4, 1, 5, 3]
sorted_cards = []

length = len(cards)
for i in range(length):
    for j in range(i+1, length):
        if cards[i] > cards[j]:
            (cards[i], cards[j]) = (cards[j], cards[i])

print cards
