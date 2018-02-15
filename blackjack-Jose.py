import random

money_left = 15

while money_left > 0:
    cards = random.randint(1, 11)
    if input("draw a card?: "):
        print(cards)
    if input != 21:
        input ("get another card?")
    if cards + cards ==21:
        money_left += 5
    if cards +cards != 21 :
        money_left -= 1
    print(money_left)