# -*- coding: utf-8 -*-
# Ohjelma käynnistää MQTT kuuntelijan ja tulostaa tiettyyn topikkiin
# saapuvat viestit. Ohjelman voi lopettaa painamalla CTRL + c.
import paho.mqtt.client as mqtt
import time

# Palvelinasetukset
palvelin = '192.168.1.2'
topic = 'testitopikki'

# Callback, johon mennään kun vastaanotetaan viesti kuunnellusta topicista.
def on_message(client1, userdata, message):
    print("Viesti vastaanotettu: " + str(message.payload.decode("utf-8")))


# Jos yhteys katkeaa, ja yhdistetään uudelleen niin uusitaan subscribe
def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)


client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect

# Yhdistetään palvelimeen ja topikkiin
client.connect(palvelin)
client.loop_start()
client.subscribe(topic)

print("Palvelin: " + palvelin + ", topic: " + topic)
print("Paina CTRL + c lopettaaksesi")
try:
	while True:
		time.sleep(1)

except KeyboardInterrupt:
	pass

# Yhteyksien purkaminen
client.disconnect()
client.loop_stop()