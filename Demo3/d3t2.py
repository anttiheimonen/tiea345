# -*- coding: utf-8 -*-
# Ohjelma mittaa lämpötilan ja kosteuden ja päivittää tiedot
# Google Drivessä olevaan taulukkoon.
import gspread
import Adafruit_DHT
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Sensori on mallia DHT11
sensori = Adafruit_DHT.DHT11

pin = 23	# Sääanturin datan sisääntulo

# Sensori yrittää lukea dataa 15 kertaa kahden sekunnin välein
kosteus, temp = Adafruit_DHT.read_retry(sensori, pin)

if kosteus is not None and temp is not None:

	# Ottaa yhteyden Google Driveen tunnistiedoilla
	scope = ['https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(creds)

	# Avataan Temperature taulukon ensimmäinen välilehti
	sheet = client.open("Temperature").sheet1

	# Lisätään uusi rivi edellisten jälkeen
	row = [datetime.now().strftime('%Y-%m-%d %H:%M:%S'),temp,kosteus]
	sheet.append_row(row)