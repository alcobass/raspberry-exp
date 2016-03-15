#!/usr/bin/python

#http://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/#prettyPhoto
import RPi.GPIO as GPIO
import time as time
 
#GPIO.RPI_INFO
chl = []
a = 1
while a < 31:
  #print a
  a = a+1
  chl.append(a)

#ch = 27
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
print chl
 
bad = []
good = []
for ch in chl:
    try:
        GPIO.setup(ch, GPIO.OUT)
        good.append(ch)
    except:
        bad.append(ch)

print "Bad : " + str(bad)
print "Good: " + str(good)

GPIO.cleanup()
ch = 2

while 1: 
	print 111
	GPIO.setup(ch, GPIO.HIGH);
	time.sleep(0.2);
	print 000
	GPIO.setup(ch, GPIO.LOW);
	time.sleep(0.2);
