import random
#jose
#generate random number
#take an input (number) from the user
#compare input to generated number
#add "higher" and "lower" statement
#add 5 guesses
number = random.randint(1, 50)
guess = -1
print (number)
guesses_left = 5
while "guess" != str (number) and guesses_left > 0:
    guess = input("guess a number: ")
    guesses_left -= 1
    if str(number) == guess :
        print ("you win")
    elif (str(number) >= guess) :
        print("guess higher")
    elif (str(number) <= guess) :
        print ("guess lower")