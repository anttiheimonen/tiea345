# -*- coding: utf-8 -*-
# Ohjelma sytyttää ledin ja sammuttaa ledin 10 kertaa sekunniksi kerrallaan.
# Ohjelma olettaa ledin olevan Rasperin BCM numeroinnin mukaisessa GPIO pinnissä 21.
import RPi.GPIO as GPIO
import time	

GPIO.setmode(GPIO.BCM)		# Asetetaan GPIO kirjasto BCM tilaan
led_pin=21					# Ulostulo, jota käytetään virran syöttmiseen ledille

GPIO.setup(led_pin, GPIO.OUT)	# Asetetaan ledin virtasyöte virranantotilaan

# Annetaan ledille virtaa sekunnin ajan ja katkaistaan virta sekunniksi:
for i in range(0, 10):		
	GPIO.output(led_pin, 1)
	time.sleep(1)
	GPIO.output(led_pin, 0)
	time.sleep(1)

GPIO.cleanup()				# Asettaa pinnit oletustilaan
