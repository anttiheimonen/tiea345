/* Ohjelma lukee liiketunnistimen tilan ja sytyttää ledin, jos
  liikettä havaitaan. Ledi sammutetaan, kun liikettä ei enää havaita.
*/
#include <wiringPi.h>
int main (void)
{
	int LED = 17;			// Led-pin
	int PIR = 26;			// PIR-pin
	wiringPiSetupGpio();
	pinMode(LED, OUTPUT);
	pinMode(PIR, INPUT);
	for (;;)
	{
		// Asetetaan LEDin tilaksi liiketunnistimen antama tila.
		// 1, eli päällä, jos liikettä havaittu, muutoin 0.
		digitalWrite (LED, digitalRead(PIR)); 
		delay (500);
	}
	return 0 ;
}