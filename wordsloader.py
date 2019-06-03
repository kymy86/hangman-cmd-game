import logging
from urllib.request import Request
from urllib import request, error
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

    @property
    def dictname(self):
        return self._DICTNAME

    @property
    def wordsurl(self):
        return self._WORDSURL

    def build_word_dict(self):
        """If words file exist, use it, otherwise retrive from remote source """
        dict_name = Path(self._DICTNAME)
        if dict_name.is_file():
            #logging.info("# File already exists. Nothing to do")
            self.built = True
        else:
            self.scraping_words_with_progress()
            self.validate_dictionary()
            self.built = True

    @DeprecationWarning
    def scraping_words_file(self):
        """ Retrive words file from remote source"""
        try:
            with request.urlopen(self._WORDSURL) as response, open(self._DICTNAME, 'wb') as dict_file:
                shutil.copyfileobj(response, dict_file)
        except error.HTTPError:
            logging.warning("# I can't download the dictionary file'")

    def scraping_words_with_progress(self):
        """ Retrieve words file from remote source displaying a progress bar"""
        try:
            req = Request(self._WORDSURL)
            req.add_header('Accept-Encoding', "")
            dict_file = request.urlopen(req)
            meta = dict_file.info()
            print(meta)
            #print("Content-Length: {} bytes".format(meta['Content-Length']))
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
        except error.HTTPError:
            logging.warning("# I can't download the dictionary file")

    def validate_dictionary(self):
        """
        Remove from the words list the words shorter than 3 characters,
        the abbreviations and the special chars
        """
        tempfile = NamedTemporaryFile(delete=False)
        regexp = re.compile(b"^[a-z][^']{4}$")
        with open(self._DICTNAME, 'rb') as words_filename:
            for i in words_filename:
                if regexp.match(i) is not None:
                    tempfile.write(i)
        shutil.move(tempfile.name, self._DICTNAME)

    def get_word_from_list(self):
        """
        Return a random word by picking it from a
        the loaded list
        """
        if self.built:
            with open(self._DICTNAME, 'r') as dict_file:
                lines = dict_file.readlines()
            index = random.randrange(0, len(lines))
            return lines[index].strip()
        else:
            logging.warning("# Dictionary has not built yet")
