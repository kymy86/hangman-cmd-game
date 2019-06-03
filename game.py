"""
Game of hangmang writte in Python
"""
from wordsloader import WordsLoader
from hangmanpic import pics
from hangmanengine import HangEngine


def run_game():
    """
    Run hangman game
    """
    loader = WordsLoader()
    pic = pics()
    your_name = input("Enter your name:     ")
    print(f"{your_name}, welcome in the Magic Hangman game.\n")
    loader.build_word_dict()
    word = loader.get_word_from_list()
    run = True
    attempt = 0
    hangengine = HangEngine(word)

    while run is True:
        print(f"{pic[attempt]}")
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
        print(f"{your_name} you lost. The word was {word}")
    else:
        print(f"Wooow {your_name}! You guessed the word {word} ")

if __name__ == '__main__':
    run_game()
