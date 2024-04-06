import random

def choose_word():
    words = ["apple", "banana", "orange", "pencil", "pineapple", "pamella"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Добрый День!")
    print("Давай")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("ББуква: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Другую.")
            continue

        if guess in guessed_letters:
            print("Нето.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            attempts -= 1
            print(f"Неправильно {attempts} Еще попыток.")
        
        displayed = display_word(word, guessed_letters)
        print(displayed)

        if "_" not in displayed:
            print("Ураааа:", word)
            break

    if attempts == 0:
        print("Не угадал:", word)

if __name__ == "__main__":
    hangman()
