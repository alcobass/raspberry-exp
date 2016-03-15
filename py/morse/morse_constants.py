# -*- coding: utf-8 -*-

#import unicodecsv
import codecs

class MorseConstants:
    DICT_FILE_NAME = 'morse-dict.csv'
    WORD_PAUSE = 'wp'

    MULTIPLIER_POINT = 1
    MULTIPLIER_DASH = 3
    MULTIPLIER_SYMBOL_PAUSE = 1
    MULTIPLIER_LETTER_PAUSE = 3
    MULTIPLIER_WORD_PAUSE = 6
    
    DICT = {}

    def __init__(self):
        #        reader = csv.reader(codecs.open(self.DICT_FILE_NAME,'rU','utf-8'))
        #reader = unicodecvs.reader(self.DICT_FILE_NAME, encoding='utf-8')
        fo = codecs.open(self.DICT_FILE_NAME,'rU','utf-8')
        #print reader
        self.DICT = {}
        for row in fo:
            #print row
            fList = row.split(',', 1)
            if len(fList) < 2:
                continue
            k = fList[0]
            v = fList[1]
            self.DICT[k] = v
        #print self.DICT

