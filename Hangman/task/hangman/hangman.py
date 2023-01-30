import random


def greeting():
    print("H A N G M A N")


def draw_word():
    return random.choice(words)


def input_letter(hidden, used_letters):
    while True:
        letter = input("\n" + hidden + "\nInput a letter: ")
        if len(letter) != 1:
            print("Please, input a single letter.")
            continue
        if letter in used_letters:
            print("You've already guessed this letter.")
            continue
        if letter.isupper() or not letter.isalpha():
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        return letter


def guess_letter():
    secret_word = draw_word()
    hidden_word = len(secret_word) * "-"
    lives = 8
    used_letters = []
    while lives > 0:
        user_letter = input_letter(hidden_word, used_letters)
        used_letters.append(user_letter)
        if user_letter not in secret_word:
            print("That letter doesn't appear in the word.")
            lives -= 1
        else:
            for i in range(0, len(hidden_word)):
                if secret_word[i] == user_letter:
                    hidden_word = hidden_word[:i] + user_letter + hidden_word[i + 1:]
            if "-" not in hidden_word:
                print(f"You guessed the word {hidden_word}!\nYou survived!")
                return 1

    else:
        print("\nYou lost!")
        return 0


def menu():
    wins = 0
    losts = 0
    while True:
        choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        if choice == "play":
            if guess_letter():
                wins += 1
            else:
                losts += 1
            continue
        if choice == "results":
            print(f"You won: {wins} times")
            print(f"You lost: {losts} times")
            continue
        if choice == "exit":
            exit()
        

words = "python", "java", "swift", "javascript"

greeting()
menu()
