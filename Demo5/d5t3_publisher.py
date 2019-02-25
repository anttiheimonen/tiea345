# -*- coding: utf-8 -*-
# Ohjelma lähettää viestejä paikallisella koneella olevalle Redis-palvelulle.
# Viestinä on sekunnin välein kasvava luku.
import redis
import time	

# Määritetään yhteys Redisiin
red = redis.StrictRedis(host='localhost', port=6379, db=0)

print("Paina CTRL + c lopettaaksesi")
luku = 0
try:
	while True:
		luku = luku + 1
		red.publish('esimtopik',luku)
		time.sleep(1)
		print("Lahetetty ", luku)
except KeyboardInterrupt:
	pass
		