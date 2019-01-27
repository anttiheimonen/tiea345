# -*- coding: utf-8 -*-
# Ohjelma ottaa yhden kuvan ja tallentaa sen /home/pi/koodi/tunninkuva.jpg
from picamera import PiCamera
from time import sleep

camera = PiCamera()
tallennussijainti = '/home/pi/Pictures/tunninkuva.jpg'	# Kuvan tallennussijainti

camera.rotation = 180	# Kääntää kuvan 180 astetta, koska kamera on väärin päin

# Kuvan ottaminen
camera.start_preview()
sleep(5)	# Sleep tarvitaan, jotta kamera tasaa kirkkauden ennen kuvan ottamista.
camera.capture(tallennussijainti)
camera.stop_preview()
