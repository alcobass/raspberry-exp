#!/usr/bin/python
# -*- coding: utf-8 -*-

from signal_generator import SignalGenerator
#import sys
import codecs
#reload(sys)
#sys.setdefaultencoding('utf8')

#print sys.getdefaultencoding()
gen = SignalGenerator(600)
fo = codecs.open("message.txt", "rU", 'utf-8')
str = fo.read()

fo.close()

while 1 == 1:
    gen.signalString(str);

#print MorseTranslator.textToMorse('123')


