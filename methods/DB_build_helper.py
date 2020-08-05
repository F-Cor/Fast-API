import itertools
import random

class Word_Items:
    '''
    Class for all the word related items in the game
    '''
    def __init__(self, all_words: list = [], word_list: list = [], letter_list: list = [], must_use: str = ''):
        self.all_words = all_words
        self.word_list = word_list
        self.letter_list = letter_list
        self.must_use = must_use
    
    def _pick_new_word(self):
        '''
        Function to pick random word from our list that has 
        7 unique characters
        '''
        possible_words = []

        for i in self.all_words:
            if len(set(i)) == 7:
                possible_words.append(i)

        return random.choice(possible_words)
    
    def _reset_class(self):
        '''
        Helper function to reset all class data
        (used in recursive function call to avoid building too much data)
        '''
        self.all_words = []
        self.word_list = []
        self.letter_list = []
        self.must_use = ''

    def get_all_words(self):
        '''
        Function to create a list from our word bank
        '''
        with open('methods\word_list.txt', 'r') as f:
            for line in f:
                if len(line) > 3:
                    self.all_words.append(line.replace('\n', ''))

    def get_letters(self):
        '''
        Function to set our list of possible letters
        and our must use letter
        '''
        new_word = self._pick_new_word()
        self.letter_list = list(set(new_word))
        self.must_use = random.choice(self.letter_list)

    def get_word_list(self):
        '''
        Function to create word_list based on letter_list and must_use
        '''
        self.word_list = []
        def _possible_words(character):
            x = {}
            for n in character:
                x[n] = x.get(n, 0) + 1
            return x
        
        for i in self.all_words:
            value = 1
            m = _possible_words(i)
            for k in m:
                if k not in self.letter_list:
                    value = 0
                elif self.letter_list.count(k) != m[k]:
                    value = 0
            if (value == 1) and (self.must_use in i) and (len(i) > 3):
                self.word_list.append(i)
    
    def update_db(self):
        '''
        Function to update the DB
        '''
        self._reset_class()
        self.get_all_words()
        self.get_letters()
        self.get_word_list()
        len_words = len(self.word_list)
        if len_words < 15 or len_words > 30:
            # print(self.word_list, len_words)
            # print('recursing')
            return self.update_db()
        else:
            return {"letter_list": self.letter_list,
                    "must_use": self.must_use,
                    "word_list": self.word_list,
                    "word_list_len": len_words}