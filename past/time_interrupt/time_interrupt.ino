//Include the module so we don't
//have to use the default Serial
//so the Arduino can be plugged in
//to a computer and still use bluetooth
#include <SoftwareSerial.h>

//Define the pins used for receiving
//and transmitting information via Bluetooth
const int rxpin = 2;
const int txpin = 3;
//Variable to store input value
//initialized with arbitrary value
char k = 'A';
//Connect the Bluetooth module
SoftwareSerial bluetooth(rxpin, txpin);

//Define the pin to control the light
int lightPin = 13;

String comdata = "";
int mark = 0;

void setup()
{
  //Set the lightbulb pin to put power out
  pinMode(lightPin, OUTPUT);
  //Initialize Serial for debugging purposes
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



