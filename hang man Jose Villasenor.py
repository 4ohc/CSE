
import random
word_bank = ["oof", "earth", "hi", "great", "cake", "dog", "pluto", "turtle",
             "flute", "slow", "death", "fake", "fate"]
word = random.choice(word_bank)

letters_guessed = []

guesses_left = 8

correct_word = word

guess = "quit"

correct_letters = list(word)

while guesses_left > 0 and guess != quit:

    output = []

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