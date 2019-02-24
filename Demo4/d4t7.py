# -*- coding: utf-8 -*-
# Ohjelma etsii kuvasta kasvot ja piirtää kasvojen ympärille neliön

import numpy as np
import cv2 as cv

# Ladataan koulutettu kasvojen tunnistin:
face_cascade = cv.CascadeClassifier('/home/pi/opencv-3.1.0/data/haarcascades_cuda/haarcascade_frontalface_default.xml')

# Ladataan kuva
kuva = cv.imread('d4t7_kasvot.jpg')
# Tehdään kuvasta harmaasävyinen
gray = cv.cvtColor(kuva, cv.COLOR_BGR2GRAY)

# Etsitään harmaasävyisestä kuvasta kasvot
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Piirretään löytyneiden kasvojen ympärille neliöt värilliseen kuvaan
for (x,y,w,h) in faces:
    cv.rectangle(kuva,(x,y),(x+w,y+h),(255,0,0),2)

# Näytetään kuva
cv.imshow('Kasvot',kuva)
# Kuvan tallennus levylle
cv.imwrite('/home/pi/koodi/d4/d4t7_tulos.jpg', kuva)

cv.waitKey(0)
cv.destroyAllWindows()