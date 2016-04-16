# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time as time
from subprocess import call
from morse_translator import MorseTranslator
from morse_constants import MorseConstants


class SignalGeneratorSound():
    SIGNAL_CHANNEL = 2
    constants = MorseConstants()
    
    def __init__(self, pps):
        self.PPS = pps
        self.singleDelay = 60 / float(pps)

    def __signalMessage__(self,strList):
        for letter in strList:
            # print letter
            # letter-pause 
            if letter == MorseConstants.WORD_PAUSE:
                time.sleep(self.singleDelay * self.constants.MULTIPLIER_WORD_PAUSE)
            else :
                time.sleep(self.singleDelay * self.constants.MULTIPLIER_LETTER_PAUSE)
                
                # walk through letter
                for sIndex in range(len(letter)):

                    # for non-first letter add symbol-pause
                    if sIndex > 0:
                        time.sleep(self.singleDelay * self.constants.MULTIPLIER_SYMBOL_PAUSE)
                    sym = letter[sIndex]
                    # Point signal
                    if sym == '.':
                        leng = self.singleDelay * self.constants.MULTIPLIER_POINT;
                        call(["./play_for_time.sh", str(leng)])
                    # Dash symbol
                    if sym == '-':
                        leng = self.singleDelay * self.constants.MULTIPLIER_DASH;
                        call(["./play_for_time.sh", str(leng)])
                        
            


    def signalString(self,st):
        morseMessage = MorseTranslator.textToMorse(st)
        print morseMessage
        self.__signalMessage__(morseMessage)


        
