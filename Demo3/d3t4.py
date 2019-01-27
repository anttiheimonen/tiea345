# -*- coding: utf-8 -*-
# Ohjelma ottaa kuvan, kun liiketunnistin havaitsee liikettä.
# Kuvan ottamisen jälkeen odotetaan, ettei tunnistin huomaa
# liikennettä, ennen kuin otetaan taas uusi kuva. Näin kuvia ei
# oteta jatkuvalla syötöllä hirveän iso määrää.
from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep

LIIKETUN = 18			# Liiketunnistimen pin

GPIO.setmode(GPIO.BCM)	# Asetetaan GPIO kirjasto BCM tilaan
camera = PiCamera()

GPIO.setup(LIIKETUN, GPIO.IN)

camera.rotation = 180	# Kääntää kuvan 180 astetta

# Alustetaan kamera
camera.start_preview()

# Ohjelma pyörii silmukassa, kunnes käyttäjä painaa ctrl + c
try:
	while True:
		if GPIO.input (LIIKETUN) == 1:	# Otetaan kuva, jos liikettä havaitaan
			camera.capture('/home/pi/koodi/d3t4.jpg')
			print("Kuva otettu")
		while GPIO.input (LIIKETUN) == 1:
			sleep(1)	# Odottaa, ettei liikettä ole enää, jottei kuvia oteta jatkuvasti
			print("Liikettä havaittu")
		sleep(1)

except KeyboardInterrupt:
	pass
	
camera.stop_preview()
GPIO.cleanup()				# Asettaa pinnit oletustilaan
print("Loppusiivous tehty")