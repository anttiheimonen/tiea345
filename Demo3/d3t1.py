# -*- coding: utf-8 -*-
import Adafruit_DHT

# Sensori on mallia DHT11
sensori = Adafruit_DHT.DHT11

pin = 23	# Sääanturin datan sisääntulo

# Sensori yrittää lukea dataa 15 kertaa kahden sekunnin välein
kosteus, temp = Adafruit_DHT.read_retry(sensori, pin)

if kosteus is not None and temp is not None:
    print('Lämpötila {0:0.1f} C  Kosteus {1:0.1f}%'.format(temp, kosteus))
else:
    print('Sensorin lukeminen ei onnistunut!')