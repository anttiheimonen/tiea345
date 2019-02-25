# -*- coding: utf-8 -*-
# Ohjelma hakee Samalla koneella olevasta Redis-palvelusta viestejä
# ja tulostaa, mikäli uusi viesti on tullut.
import redis
import time	

red = redis.StrictRedis(host='localhost', port=6379, db=0)
pub = red.pubsub()
# Kuunneellan topicia esimtopik
pub.subscribe('esimtopik')

print("Paina CTRL + c lopettaaksesi")
try:
	while True:
	# Haetaan viesti Redisista
		viesti=pub.get_message() 
		# Jos viesti on tullut, niin tulostetaan
		if (viesti != None):
			print 'Kanava: ', viesti["channel"]
			print 'Viesti: ', viesti["data"]
		time.sleep(1)
except KeyboardInterrupt:
	pass