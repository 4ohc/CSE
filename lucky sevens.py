import random

money_left = 15

while money_left > 0:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("Dice 2 is %d" % dice2)

    print("Dice 1 is %d" % dice1)

    if dice1 + dice2 == 7:
        money_left += 4
    else:
        money_left -= 1
    print(money_left)





