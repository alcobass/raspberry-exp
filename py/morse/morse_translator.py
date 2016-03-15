from morse_constants import MorseConstants

class MorseTranslator:

    @staticmethod
    def textToMorse(inputText):
        constants = MorseConstants()
        res = []
        for a in inputText:
            res.append(constants.DICT[a])
        return res

    def __init__():
        print 123

    
