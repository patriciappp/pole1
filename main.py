import random

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "*"
    return displayed_word

def main():
    words = ["apple", "banana", "orange", "strawberry", "grape", "watermelon"]
    word = random.choice(words)
    attempts = int(input("Введите количество попыток: "))
    guessed_letters = []

    while attempts > 0:
        print(display_word(word, guessed_letters))
        guess = input("Введите букву или слово: ").lower()

        if len(guess) == 1:  # ввід - літера
            if guess in guessed_letters:
                print("Вы уже вводили эту букву.")
            elif guess in word:
                guessed_letters.append(guess)
                if set(word) == set(guessed_letters):
                    print(word)
                    print("Поздравляю, вы угадали слово!")
                    break
            else:
                print("Такой буквы нет.")
                attempts -= 1
        else:  # ввід - слово
            if guess == word:
                print(word)
                print("Похдравляю, вы угадали слово!")
                break
            else:
                print("Попробуйте еще раз.")
                attempts -= 1

    if attempts == 0:
        print("Вы проиграли. Слово было:", word)

if __name__ == "__main__":
    main()
