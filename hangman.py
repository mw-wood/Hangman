from english_words import english_words_lower_set
import random

correct_word = random.choice(list(english_words_lower_set))
correct_letters = []
incorrect_letters = []

MAX_WRONG_GUESSES = 8
current_wrong_guesses = 0


def UserGuess():
    letter = str(input("Enter a letter: "))
    if letter == "":
        return UserGuess()

    letter = letter[0].lower()
    occurances = correct_word.count(letter)
    if occurances == 0:
        return 1

    if letter not in correct_letters:
        for x in range(occurances):
            correct_letters.append(letter)
    return 0


def PrintGuesses():
    for letter in correct_word:
        if letter in correct_letters:
            print(letter, end="")
        else:
            print("_", end="")

    print(f"\n\n{current_wrong_guesses}/8 Wrong Guesses")


def CheckForWin():
    if current_wrong_guesses >= MAX_WRONG_GUESSES:
        print(f"Unlucky! The correct word was: {correct_word}.")
        return False
    elif len(correct_letters) == len(correct_word):
        print("Congratulations!")
        return False
    else:
        return True


if __name__ == "__main__":
    while CheckForWin():
        current_wrong_guesses += UserGuess()
        PrintGuesses()
