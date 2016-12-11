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



if __name__ == '__main__':
    run_game()
