# -*- coding: utf-8 -*-
from picamera import PiCamera
from time import sleep

camera = PiCamera()


camera.rotation = 180	# Kääntää kuvan 180 astetta, koska kamera on väärin päin

# Kuvan ottaminen
camera.start_preview()
sleep(5)	# Sleeep tarvitaan, jotta kamera tasaa kirkkauden ennen kuvan ottamista.
camera.capture('/home/pi/koodi/kuva.jpg')
camera.stop_preview()

# Videon ottaminen

camera.resolution = (600, 480)	# Asetetaan matalampi resoluutio
camera.start_recording('/home/pi/koodi/video.h264')
sleep(15)
camera.stop_recording()
