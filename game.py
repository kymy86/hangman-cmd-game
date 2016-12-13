#!/usr/bin/python3

from wordsloader import WordsLoader
from hangmanpic import pics


def run_game():
    loader = WordsLoader()
    pic = pics()
    your_name = input("Enter your name\n")
    print("{}, welcome in the Magic Hangman game. Press enter to continue\n".format(your_name))
    loader.build_word_dict()
    print("\n")
    word = loader.get_words_from_list()
    print(word)

    attempt = 0
    success = False
    word_length = len(word)
    word_in_list = list(word)
    guessing_word = [None] * word_length
    for i in range(0, word_length):
        guessing_word[i] = "_"

    while attempt < len(pic)-1:

        print("{}".format(pic[attempt]))
        guess_letter = input("Guess your letter\n")
        if guess_letter.lower() in word_in_list:
            guess_letter_index = word_in_list.index(guess_letter.lower())
            guessing_word[guess_letter_index] = guess_letter.lower()
            word_in_list[guess_letter_index] = "_"
            print("{}".format(" ".join(guessing_word)))
            if "".join(guessing_word) == word:
                success = True
                break
            while True:
                answer = input("Would you like to guess the word? (Y/N)\n")
                if answer.upper() in ["Y", "N"]:
                    break
            if answer.upper() == "Y":
                guess_word = input("Guess the word\n")
                if guess_word == word:
                    success = True
                    break
                else:
                    print("{}".format(pic[attempt+1]))
        else:
            print("You're wrong\n")
            print("{}".format(" ".join(guessing_word)))
            attempt += 1

    if success:
        print("Congrats {}! You guessed the word!".format(your_name))
    else:
        print("{}".format(pic[len(pic)-1]))
        print("{} you lost. The words was {}".format(your_name, word))



if __name__ == '__main__':
    run_game()
