# -*- coding: utf-8 -*-
# Ohjelma sytyttää ledin ja sammuttaa ledin 10 kertaa sekunniksi kerrallaan.
# Ohjelma olettaa ledin olevan Rasperin BCM numeroinnin mukaisessa GPIO pinnissä 21.
import RPi.GPIO as GPIO
import time	

GPIO.setmode(GPIO.BCM)		# Asetetaan GPIO kirjasto BCM tilaan
LED_PIN = 21				# Ulostulo, jota käytetään virran syöttmiseen ledille
PAINIKE = 26				# Ulostulo, johon tulee signaali, kun painiketta painetaan.
LIIKE = 13					# Ulostulo, johon tulee signaali, kun painiketta painetaan.

GPIO.setup(LED_PIN, GPIO.OUT)	# Asetetaan ledin virtasyöte virranantotilaan
GPIO.setup(PAINIKE, GPIO.IN)	# Asetetaan ledin virtasyöte virranantotilaan
GPIO.setup(LIIKE, GPIO.IN)		# Asetetaan ledin virtasyöte virranantotilaan
tila = 0
edellinen_tila = 0

try:
	while True:
		time.sleep(1)
		GPIO.output(LED_PIN, GPIO.input (PAINIKE))
		tila = GPIO.input (LIIKE)
		if tila != edellinen_tila:
			print("Liikesensorin tila muuttunut: " , tila )
			edellinen_tila = tila
		else:
			print("Liikesensorin tila: " , tila )
			
except KeyboardInterrupt:
	pass
	
print("Loppu")

GPIO.cleanup()				# Asettaa pinnit oletustilaan