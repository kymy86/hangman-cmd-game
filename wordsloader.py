#!/usr/bin/python3
import logging
import urllib.request
from pathlib import Path
import shutil
from tempfile import NamedTemporaryFile
import re
import random

class WordsLoader:
    """
    Retrieve and build the dictionary of Hangman game
    """

    _DICTNAME = 'hangwords.txt'
    _WORDSURL = 'https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569'
    built = False

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    def build_word_dict(self):
        """If words file exist, use it, otherwise retrive from remote source """
        dict_name = Path(self._DICTNAME)
        if dict_name.is_file():
            logging.info("# File already exists. Nothing to do")
            self.built = True
        else:
            self.scraping_words_with_progress()
            self.validate_dictionary()
            self.built = True

    @DeprecationWarning
    def scraping_words_file(self):
        """ Retrive words file from remote source"""
        try:
            with urllib.request.urlopen(self._WORDSURL) as response, open(self._DICTNAME, 'wb') as dict_file:
                shutil.copyfileobj(response, dict_file)
        except urllib.error.HTTPError:
            logging.warning("# I can't download the dictionary file'")

    def scraping_words_with_progress(self):
        """ Retrieve words file from remote source displaying a progress bar"""
        try:
            dict_file = urllib.request.urlopen(self._WORDSURL)
            meta = dict_file.info()
            print("Content-Length: {} bytes".format(meta['Content-Length']))
            file_total_bytes = int(meta['Content-Length'])
            data_blocks = []
            total = 0

            while True:
                block = dict_file.read(1024)
                data_blocks.append(block)
                total += len(block)
                progress = ((60*total)//file_total_bytes)
                current_size = int(total/file_total_bytes*100)
                print("[{}{}] {}%".format('#' * progress, ' ' * (60-progress), current_size), end="\r")
                if not len(block):
                    break
            data = b''.join(data_blocks)
            dict_file.close()
            with open(self._DICTNAME, "wb") as file:
                file.write(data)
        except urllib.error.HTTPError:
            logging.warning("# I can't download the dictionary file'")

    def validate_dictionary(self):
        """
        Remove from the words list the words shorter than 3 characters,
        the abbreviations and the special chars
        """
        tempfile = NamedTemporaryFile(delete=False)
        regexp = re.compile(b"^[a-z][^']{4}$")
        words_filename = open(self._DICTNAME, 'rb')
        for i in words_filename:
            match = regexp.match(i)
            if match is not None:
                tempfile.write(i)
        words_filename.close()
        shutil.move(tempfile.name, self._DICTNAME)

    def get_words_from_list(self):
        if self.built:
            dict_file = open(self._DICTNAME, 'r')
            lines = dict_file.readlines()
            dict_file.close()
            index = random.randrange(0, len(lines))
            return lines[index].strip()


