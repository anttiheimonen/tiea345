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

# Ohjelma pyörii silmukassa, kunnes käyttäjä painaa ctrl + c
print("Paina CTRL + c lopettaaksesi")

try:
	while True:
		time.sleep(0.1)		# Tauko estää prosessorin 100 % käytön
		GPIO.output(LED_PIN, GPIO.input (PAINIKE))	# LED_PIN saa arvoksi napin inputin arvon
		tila = GPIO.input (LIIKE)					# Otetaan liikesensorin tila ylös
		if tila != edellinen_tila:					# Jos tila on muuttunut, niin kerrotaan siitä
			print "Liikesensorin tila muuttunut: " , tila
			edellinen_tila = tila
except KeyboardInterrupt:
	pass
	
print("Loppu")

GPIO.cleanup()				# Asettaa pinnit oletustilaan