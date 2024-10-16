// Include Library for Servo
#include "Servo.h"

// Servomotor = Datatype Servo
Servo servo;

void setup() {
  // Servomotor on Pin 8
  Servo.attach(9);
  // Start Serial Communication with RaspPi
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    int rotationVal = Serial.read() - '0';
    
    // Val 0 for Left, 45 for Middle, 90 for Right
    servo.write(rotationVal);
    delay(10);
    }
}