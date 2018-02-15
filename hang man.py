# port string
import random

# a general guide for hangman
# 1. make a word bank - 10 items
# 2. pick a random item from the list
# 3. add a guess to the list of letters guessed
# 4. reveal letters already guessed
# 5. create a win condition


word_bank = ["oof", "earth", "hi", "great", "cake", "dog", "pluto", "turtle",
             "flute", "slow"]
word = random.choice(word_bank)



letters_guessed = []

guesses_left = 10

correct_word = word

guess = " "

correct_letters = list(word)

while guesses_left > 0 and guess != quit:
    output= []
    current_guess = input("guess a letter:")

    letters_guessed.append(current_guess)

    print("".join(letters_guessed))

    if current_guess != correct_letters:
        guesses_left -=1
        for letter in word:
            if letter.lower() in letters_guessed:
                output.append(letter)
            else:
                output.append("*")
        print("".join(list(output)))
    if output == list(word):
        print("".join(list(word)))
        print("you win")
        quit()


