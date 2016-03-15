# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time as time
from morse_translator import MorseTranslator
from morse_constants import MorseConstants


class SignalGenerator():
    SIGNAL_CHANNEL = 2
    constants = MorseConstants()
    
    def __init__(self, pps):
        self.PPS = pps
        self.singleDelay = 60 / float(pps)

        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.SIGNAL_CHANNEL, GPIO.OUT)
#	GPIO.setup(ch, GPIO.HIGH);
#	time.sleep(0.2);

    def __signalMessage__(self,strList):
        for letter in strList:
            # print letter
            # letter-pause 
            if letter == MorseConstants.WORD_PAUSE:
                GPIO.setup(self.SIGNAL_CHANNEL, GPIO.LOW)
                time.sleep(self.singleDelay * self.constants.MULTIPLIER_WORD_PAUSE)
            else :
                GPIO.setup(self.SIGNAL_CHANNEL, GPIO.LOW)
                time.sleep(self.singleDelay * self.constants.MULTIPLIER_LETTER_PAUSE)
                
                # walk through letter
                for sIndex in range(len(letter)):

                    # for non-first letter add symbol-pause
                    if sIndex > 0:
                        GPIO.setup(self.SIGNAL_CHANNEL, GPIO.LOW)
                        time.sleep(self.singleDelay * self.constants.MULTIPLIER_SYMBOL_PAUSE)
                    sym = letter[sIndex]
                    # Point signal
                    if sym == '.':
                        GPIO.setup(self.SIGNAL_CHANNEL, GPIO.HIGH)
                        time.sleep(self.singleDelay * self.constants.MULTIPLIER_POINT)
                    # Dash symbol
                    if sym == '-':
                        GPIO.setup(self.SIGNAL_CHANNEL, GPIO.HIGH)
                        time.sleep(self.singleDelay * self.constants.MULTIPLIER_DASH)
                        
            


    def signalString(self,st):
        morseMessage = MorseTranslator.textToMorse(st)
        print morseMessage
        self.__signalMessage__(morseMessage)


        
