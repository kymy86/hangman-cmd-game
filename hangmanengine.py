"""
This class implement the hangman game
core logic
"""
#!/usr/bin/python3
import logging

class HangEngine:
    """
    Game Engine
    """
    status = 0

    def __init__(self, word):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        self.word = word
        self._word_length = len(self.word)
        self._word_list = list(word)
        self._guessing_word = ["_"] * self._word_length

    def hangman_engine(self, u_attempt, p_attempt, guess_letter):
        """
        Check if the letter exists, if user guesses the word or not
        """
        if u_attempt >= p_attempt:
            self.status = -1
            return False
        if guess_letter.lower() in self._word_list:
            self.__find_all_letters(guess_letter.lower())
            if "".join(self.guessing_word) == self.word:
                self.status = 1
                return False
            else:
                self.status = 2
                return True
        else:
            self.status = 3
            return True


    def __find_all_letters(self, guess_letter):
        for letter in self._word_list:
            if letter == guess_letter:
                guess_letter_index = self._word_list.index(guess_letter)
                self.guessing_word[guess_letter_index] = guess_letter
                self._word_list[guess_letter_index] = "_"

    @property
    def guessing_word(self):
        return self._guessing_word


            