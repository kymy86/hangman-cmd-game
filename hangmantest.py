import unittest
import os
from hangmanengine import HangEngine
from wordsloader import WordsLoader


class WordLoaderTest(unittest.TestCase):
    """
    Unit test for the word loader
    """

    @classmethod
    def setUpClass(cls):
        cls.wordLoader = WordsLoader()

    def test_file_exists(self):
        """
        The wordLoader should load if the file exists
        """
        try:
            os.remove(self.wordLoader.dictname)
        except OSError:
            pass
        self.wordLoader.build_word_dict()
        self.assertTrue(os.path.exists(self.wordLoader.dictname))

    def test_dict_valid(self):
        """
        All words in the dictionary must have at least 4 chars
        """
        self.wordLoader.build_word_dict()
        with open(self.wordLoader.dictname, 'r') as dict_file:
            lines = dict_file.readlines()
    
        for i in lines:
            self.assertGreaterEqual(len(i), 4)

class HangmanEngineTest(unittest.TestCase):
    """
    Unit test for the hangman engine
    """

    @classmethod
    def setUpClass(cls):
        cls.hangengine = HangEngine('test')

    def test_guess_letter_wrong(self):
        """
        Test when user enters a wrong letter
        """
        res = self.hangengine.hangman_engine(2, 5, 'b')
        self.assertTrue(res)
        self.assertEqual(self.hangengine.status, 3)

    def test_guess_letter_right(self):
        """
        Test when user enters the right letter
        """
        res = self.hangengine.hangman_engine(2, 5, 't')
        self.assertTrue(res)
        self.assertEqual(self.hangengine.status, 2)

    def test_guess_letter_full_attempts(self):
        """
        Test if user uses all the attempts available
        """
        res = self.hangengine.hangman_engine(2, 2, 'e')
        self.assertFalse(res)
        self.assertEqual(self.hangengine.status, -1)

    def test_guess_word(self):
        """
        Test when user guesses the right word
        """
        res = self.hangengine.hangman_engine(2, 5, 't')
        self.assertTrue(res)
        res = self.hangengine.hangman_engine(2, 5, 'e')
        self.assertTrue(res)
        res = self.hangengine.hangman_engine(2, 5, 's')
        self.assertFalse(res)
        self.assertEqual("".join(self.hangengine.guessing_word), 'test')


if __name__ == '__main__':
    unittest.main()



