# -*- coding: utf-8 -*-

from morse_constants import MorseConstants

class MorseTranslator:

    @staticmethod
    def textToMorse(inputText):
        constants = MorseConstants()
        res = []
        for a in inputText:
            if a == ' ':
                res.append(constants.WORD_PAUSE)
            else :
                if a.upper() in constants.DICT:
                    print a
                    res.append(constants.DICT[a.upper()])
        return res

    def __init__():
        print 123

    
