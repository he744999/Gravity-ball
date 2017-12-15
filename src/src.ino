
#include <SoftwareSerial.h>


const int rxpin = 2;
const int txpin = 3;

SoftwareSerial bluetooth(rxpin, txpin);

int lightPin = 13;

String comdata = "";
int mark = 0;

void setup()
{

  pinMode(lightPin, OUTPUT);

  Serial.begin(9600);
  Serial.println("Serial ready");
  //Initialize the bluetooth
  bluetooth.begin(9600);
  bluetooth.println("Bluetooth ready");
}

void loop()
{

  //Check for new data
  while (bluetooth.available() > 0) {
    //Remember new data

    comdata += char(bluetooth.read());
    delay(2);
    mark = 1;
  }

  if (mark == 1) {
    deal_data(comdata);
    comdata = String("");
    mark = 0;
  }
}



