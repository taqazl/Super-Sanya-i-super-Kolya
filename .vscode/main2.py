import random

def chooseword():
    words = ["apple", "banana", "orange", "grape", "pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += ""
    return displayedword

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")

        displayed = display_word(word, guessed_letters)
        print(displayed)

        if "" not in displayed:
            print("Congratulations! You guessed the word:", word)
            break

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", word)

if name == "main":
    hangman()