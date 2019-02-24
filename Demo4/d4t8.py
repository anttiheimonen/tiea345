# -*- coding: utf-8 -*-
# Ohjelma ottaa kuvan Raspin kameralla ja tunnistaa siitä kasvot. Kasvojen tunnistuksen
# jälkeen kuva tallennetaan levylle.
import io
import numpy as np
import cv2 as cv
from picamera import PiCamera
from time import sleep

stream = io.BytesIO()

camera = PiCamera()

camera.rotation = 180	# Kääntää kuvan 180 astetta, koska kamera on väärin päin

# Ladataan koulutettu kasvojen tunnistin:
face_cascade = cv.CascadeClassifier('/home/pi/opencv-3.1.0/data/haarcascades_cuda/haarcascade_frontalface_default.xml')

# Kameran asetukset
camera.resolution = (320, 240)

# Kuvan ottaminen
camera.start_preview()
sleep(1)	# Sleep antaa kameralle aikaa tasata valoisuutta ennen kuvan ottoa.
camera.capture(stream, format='jpeg')
camera.stop_preview()

# Otetaan kuva Numpyn taulukkoon
buff = np.fromstring(stream.getvalue(), dtype=np.uint8)

# Tehdään OpenCV kuva
kuva = cv.imdecode(buff, 1)

# Muutetaan harmaasävyksi
gray = cv.cvtColor(kuva,cv.COLOR_BGR2GRAY)

# Etsitään harmaasävyisestä kuvasta kasvot
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Piirretään löytyneiden kasvojen ympärille neliöt värilliseen kuvaan
for (x,y,w,h) in faces:
    cv.rectangle(kuva,(x,y),(x+w,y+h),(255,0,0),2)

# Näytetään kuva
cv.imshow('Kasvot',kuva)
# Kuvan tallennus levylle
cv.imwrite('/home/pi/koodi/d4/d4t8_tulos.jpg', kuva)

cv.waitKey(0)
cv.destroyAllWindows()