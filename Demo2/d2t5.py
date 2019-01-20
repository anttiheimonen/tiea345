# -*- coding: utf-8 -*-
# Ohjelma matkii liikennevalojen toimintaa. Oletuksena näytetään autoilijoille vihreää valoa.
# Jalankulkija painaa painiketta, kun haluaa itselleen vihreät valot. Liiketunnistin odottaa, 
# ettei autoja tule, jonka jälkeen vaihtaa autoille punaiset valot ja kävelijälle vihreän.
# Lopuksi vielä näytetään kävelijälle punaista ja autoille taas vihreää valoa.

import RPi.GPIO as GPIO
import time	

GPIO.setmode(GPIO.BCM)		# Asetetaan GPIO kirjasto BCM tilaan
# Auton liikennevalojen pinnit:
LED_AUTO_PUNAINEN = 16
LED_AUTO_KELTAINEN = 20
LED_AUTO_VIHREA = 21

#Jalankulkijan liikennevalojen pinnit:
LED_JALANK_PUNAINEN = 5
LED_JALANK_VIHREA = 6
LED_ODOTTAAVAIHTUMISTA = 19

# Sisääntulojen pinnit:
PAINIKE = 26				# liikennevalon napille
LIIKETUN = 13				# liiketunnistukselle

# Pinnien alustus
GPIO.setup(LED_AUTO_PUNAINEN, GPIO.OUT)
GPIO.setup(LED_AUTO_KELTAINEN, GPIO.OUT)
GPIO.setup(LED_AUTO_VIHREA, GPIO.OUT)
GPIO.setup(LED_JALANK_PUNAINEN, GPIO.OUT)
GPIO.setup(LED_JALANK_VIHREA, GPIO.OUT)
GPIO.setup(LED_ODOTTAAVAIHTUMISTA, GPIO.OUT)

GPIO.setup(PAINIKE, GPIO.IN)
GPIO.setup(LIIKETUN, GPIO.IN)


# Liikennevalojen asetus alkuarvoihin:
GPIO.output(LED_AUTO_PUNAINEN, 0)
GPIO.output(LED_AUTO_KELTAINEN, 0)
GPIO.output(LED_AUTO_VIHREA, 1)

GPIO.output(LED_JALANK_PUNAINEN, 1)
GPIO.output(LED_JALANK_VIHREA, 0)
GPIO.output(LED_ODOTTAAVAIHTUMISTA, 0)

vaihtopyydetty = 0

# Ohjelma pyörii silmukassa, kunnes käyttäjä painaa ctrl + c
print("Paina CTRL + c lopettaaksesi")
try:
	while True:
		time.sleep(0.1)
		if (GPIO.input (PAINIKE)):					# Painikkeen tilan tarkastus
			print("Jalankulkija tulossa")			
			GPIO.output(LED_ODOTTAAVAIHTUMISTA, 1)	# led-syttyy jalankulkijan pyynnön merkiksi.
			while GPIO.input (LIIKETUN) == 1:		# Odotetaan silmukassa, kunnes liikkeentunnistin 
													# ei huomaa enää liikennettä.
				print("autoja ajaa")
				# Jos liikennettä näkyy, niin odotetaan kaksi sekuntia, ennen uutta tarkastusta.
				# Lisäksi valontunnistimessa on oma ajastin, jonka aikana liikennettä ei saa olla
				# näkynyt, ennen kun sensori ilmoittaa, ettei liikettä ole.
				time.sleep(2)					
			
			# Muutetaan liikenne valot samalla tavalla kuin oikeassa elämässäkin:
			# Sytyttää autoille keltaisen valon
			GPIO.output(LED_AUTO_KELTAINEN, 1)
			GPIO.output(LED_AUTO_VIHREA, 0)
			time.sleep(2)
			
			# Sytyttää autoille punaisen valon
			GPIO.output(LED_AUTO_PUNAINEN, 1)
			GPIO.output(LED_AUTO_KELTAINEN, 0)
			time.sleep(2)
			
			# Jalankulkijoille vihreä valo ja napin led pois päältä
			GPIO.output(LED_JALANK_PUNAINEN, 0)
			GPIO.output(LED_JALANK_VIHREA, 1)
			GPIO.output(LED_ODOTTAAVAIHTUMISTA, 0)
			time.sleep(3)
			
			# Jalankulkijoille punainen valo 
			GPIO.output(LED_JALANK_PUNAINEN, 1)
			GPIO.output(LED_JALANK_VIHREA, 0)
			time.sleep(2)
			
			# Sytyttää autoille keltaisen (punainen palaa jo)
			GPIO.output(LED_AUTO_KELTAINEN, 1)
			time.sleep(1)
			
			# Sytyttää autoille vihreän
			GPIO.output(LED_AUTO_PUNAINEN, 0)
			GPIO.output(LED_AUTO_KELTAINEN, 0)
			GPIO.output(LED_AUTO_VIHREA, 1)

except KeyboardInterrupt:
	pass
		
GPIO.cleanup()				# Asettaa pinnit oletustilaan
print("GPIO-kirjaston siivous tehty")