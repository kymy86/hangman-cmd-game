#!/usr/bin/python3

from wordsloader import WordsLoader
from hangmanpic import pics
from hangmanengine import HangEngine


def run_game():
    loader = WordsLoader()
    pic = pics()
    your_name = input("Enter your name:     ")
    print("{}, welcome in the Magic Hangman game.\n".format(your_name))
    loader.build_word_dict()
    word = loader.get_word_from_list()
    print(word)
    run = True
    attempt = 0
    hangengine = HangEngine(word)

    while run is True:
        print("{}".format(pic[attempt]))
        print("{}".format(" ".join(hangengine.guessing_word)))
        guess_letter = input("Guess your letter ==> ")
        run = hangengine.hangman_engine(attempt, len(pic)-1, guess_letter)
        if hangengine.status == 2:
            print("{}".format(" ".join(hangengine.guessing_word)))
        elif hangengine.status == 3:
            print("{}".format(" ".join(hangengine.guessing_word)))
            attempt += 1

    if hangengine.status == -1:
        print("{}".format(pic[len(pic)-1]))
        print("{} you lost. The word was {}".format(your_name, word))
    else:
        print("Wooow {}! You guessed the word {} ".format(your_name, word))

if __name__ == '__main__':
    run_game()
