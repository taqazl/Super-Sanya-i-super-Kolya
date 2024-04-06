import random

class InvalidInputError(Exception):
    pass

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
        try:
            guess = input("Буква: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                raise InvalidInputError("Неправильный ввод! Пожалуйста, введите одну букву.")

            if guess in guessed_letters:
                raise InvalidInputError("Вы уже ввели эту букву!")

            guessed_letters.append(guess)

            if guess in word:
                print("Правильно!")
            else:
                attempts -= 1
                print(f"Неправильно, осталось попыток: {attempts}")

            displayed = display_word(word, guessed_letters)
            print(displayed)

            if "_" not in displayed:
                print("Поздравляю, вы угадали слово:", word)
                break

        except InvalidInputError as e:
            print(e)

    if attempts == 0:
        print("К сожалению, вы проиграли. Загаданное слово было:", word)

if __name__ == "__main__":
    hangman()
