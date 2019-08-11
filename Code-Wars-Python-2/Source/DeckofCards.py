def deck_of_cards():
    suits = ["hearts", "spades", "diamonds", "clubs"]
    ranks = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]

    return ["%s of %s" % (rank,suit) for suit in suits for rank in ranks]

print(deck_of_cards())