# -*- coding: utf-8 -*-
# Ohjelma yhdistää MQTT palvelimelle ja lähettää käyttäjän kirjoittamia 
# viestejä tiettyyn topiciin.
# Ohjelman voi lopettaa painamalla CTRL + c.
import paho.mqtt.client as mqtt

# Palvelinasetukset
palvelin = '192.168.1.2'
topic = 'testitopikki'

client = mqtt.Client()

# Yhdistetään palvelimeen ja topikkiin
client.connect(palvelin)
client.subscribe(topic)

print("Palvelin: " + palvelin + ", topic: " + topic)
print("Paina CTRL + c lopettaaksesi")
try:
	while True:
		viesti = raw_input('Lähetä viesti: ')
		client.publish(topic, viesti)

except KeyboardInterrupt:
	pass

client.disconnect()