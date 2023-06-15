#include <SoftwareSerial.h>

int photoPin = A0;
int ledPin = 7;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.println("Hello World");

    // Begin serial communication
  Serial.begin(9600);
}

void loop() {
  int lightRaw = analogRead(photoPin);
  Serial.println(lightRaw);
  if (lightRaw > 50) {
    digitalWrite(ledPin, HIGH);
  }

  else {
    digitalWrite(ledPin, LOW);
  }
  delay(100);
}
