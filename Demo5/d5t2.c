/* Ohjelma matkii liikennevalojen toimintaa. Oletuksena näytetään autoilijoille vihreää valoa.
 Jalankulkija painaa painiketta, kun haluaa itselleen vihreät valot. Liiketunnistin odottaa, 
 ettei autoja tule, jonka jälkeen vaihtaa autoille punaiset valot ja kävelijälle vihreän.
 Lopuksi vielä näytetään kävelijälle punaista ja autoille taas vihreää valoa.
 */
#include <wiringPi.h>
#include <stdio.h>
int main (void)
{
	// Otetaan käyttöön pinnien BCM numerointi
	wiringPiSetupGpio();
	
	// Auton liikennevalojen pinnit:
	int LED_AUTO_PUNAINEN = 16;
	int LED_AUTO_KELTAINEN = 20;
	int LED_AUTO_VIHREA = 21;

	// Jalankulkijan liikennevalojen pinnit:
	int LED_JALANK_PUNAINEN = 5;
	int LED_JALANK_VIHREA = 6;
	int LED_ODOTTAAVAIHTUMISTA = 19;

	// Sisääntulojen pinnit:
	int PAINIKE = 26;				// liikennevalon napille
	int LIIKETUN = 13;				// liiketunnistukselle
	
	//int vaihtopyydetty = 0;
	
	// Pinnien alustus
	pinMode(LED_AUTO_PUNAINEN, OUTPUT);
	pinMode(LED_AUTO_KELTAINEN, OUTPUT);
	pinMode(LED_AUTO_VIHREA, OUTPUT);
	pinMode(LED_JALANK_PUNAINEN, OUTPUT);
	pinMode(LED_JALANK_VIHREA, OUTPUT);
	pinMode(LED_ODOTTAAVAIHTUMISTA, OUTPUT);

	pinMode(PAINIKE, INPUT);
	pinMode(LIIKETUN, INPUT);


	// Liikennevalojen asetus alkuarvoihin:
	digitalWrite(LED_AUTO_PUNAINEN, 0);
	digitalWrite(LED_AUTO_KELTAINEN, 0);
	digitalWrite(LED_AUTO_VIHREA, 1);

	digitalWrite(LED_JALANK_PUNAINEN, 1);
	digitalWrite(LED_JALANK_VIHREA, 0);
	digitalWrite(LED_ODOTTAAVAIHTUMISTA, 0);

	for (;;)
	{
		delay (50);
		if (digitalRead (PAINIKE)) 						// Painikkeen tilan tarkastus
		{
			printf("Jalankulkija tulossa \n");			// led-syttyy jalankulkijan pyynnön merkiksi.
			digitalWrite(LED_ODOTTAAVAIHTUMISTA, 1);	// Odotetaan silmukassa, kunnes liikkeentunnistin 
			while (digitalRead (LIIKETUN) == 1)			// ei huomaa enää liikennettä.
			{
				// Jos liikennettä näkyy, niin odotetaan kaksi sekuntia, ennen uutta tarkastusta.
				// Lisäksi valontunnistimessa on oma ajastin, jonka aikana liikennettä ei saa olla
				// näkynyt, ennen kun sensori ilmoittaa, ettei liikettä ole.
				printf("Autoja ajaa\n");
				delay (1000);
			} 
			
			// Muutetaan liikenne valot samalla tavalla kuin oikeassa elämässäkin:
			// Sytyttää autoille keltaisen valon
			digitalWrite(LED_AUTO_KELTAINEN, 1);
			digitalWrite(LED_AUTO_VIHREA, 0);
			delay (2000);
			
			// Sytyttää autoille punaisen valon
			digitalWrite(LED_AUTO_PUNAINEN, 1);
			digitalWrite(LED_AUTO_KELTAINEN, 0);
			delay (2000);
			
			// Jalankulkijoille vihreä valo ja napin led pois päältä
			digitalWrite(LED_JALANK_PUNAINEN, 0);
			digitalWrite(LED_JALANK_VIHREA, 1);
			digitalWrite(LED_ODOTTAAVAIHTUMISTA, 0);
			delay(3000);
			
			// Jalankulkijoille punainen valo 
			digitalWrite(LED_JALANK_PUNAINEN, 1);
			digitalWrite(LED_JALANK_VIHREA, 0);
			delay (2000);
			
			// Sytyttää autoille keltaisen (punainen palaa jo)
			digitalWrite(LED_AUTO_KELTAINEN, 1);
			delay (1000);
			
			// Sytyttää autoille vihreän
			digitalWrite(LED_AUTO_PUNAINEN, 0);
			digitalWrite(LED_AUTO_KELTAINEN, 0);
			digitalWrite(LED_AUTO_VIHREA, 1);
		}
	}
}