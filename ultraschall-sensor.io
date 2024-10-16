// Pins für Sender
const int senden_left = 8;
const int senden_right = 6;
const int senden_front = 4;

// Pins für Empfänger
const int echo_left = 9;
const int echo_right = 7;
const int echo_front = 5;

// Entfernungen
long Entfernung_left = 0;
long Entfernung_right = 0;
long Entfernung_front = 0;

// Zeiten
long Zeit_left = 0;
long Zeit_right = 0;
long Zeit_front = 0;

void setup() 
{
  // Initialisiere die Pins für die Sender und Empfänger
  pinMode(senden_left, OUTPUT);
  pinMode(echo_left, INPUT);

  pinMode(senden_right, OUTPUT);
  pinMode(echo_right, INPUT);

  pinMode(senden_front, OUTPUT);
  pinMode(echo_front, INPUT);

  // Seriellen Monitor starten
  Serial.begin(9600);
}

void loop() 
{
  // Front Sensor
  digitalWrite(senden_front, LOW);
  delay(2); // Kurze Verzögerung um Störungen zu vermeiden
  digitalWrite(senden_front, HIGH);
  delayMicroseconds(10);
  digitalWrite(senden_front, LOW);

  // Zeit messen, bis das Signal zurückkommt
  Zeit_front = pulseIn(echo_front, HIGH);
  Entfernung_front = (Zeit_front / 2) * 0.03432;

  // Ausgabe der Entfernungsdaten
  Serial.print("Sensor Front: ");
  if (Entfernung_front > 0) 
  {
    Serial.print("Entfernung in cm: ");
    Serial.println(Entfernung_front);
  }
  else 
  {
    Serial.println("Keine gültige Messung");
  }

  // Abstandwarnung
  if (Entfernung_front > 0 && Entfernung_front < 30)
  {
    Serial.println("!Zu kleiner Abstand!");
  }

  // Kurze Verzögerung
  delay(100); 

  // Left Sensor
  digitalWrite(senden_left, LOW);
  delay(2);
  digitalWrite(senden_left, HIGH);
  delayMicroseconds(10);
  digitalWrite(senden_left, LOW);

  Zeit_left = pulseIn(echo_left, HIGH);
  Entfernung_left = (Zeit_left / 2) * 0.03432;

  // Ausgabe der Entfernungsdaten
  Serial.print("Sensor Left: ");
  if (Entfernung_left > 0) 
  {
    Serial.print("Entfernung in cm: ");
    Serial.println(Entfernung_left);
  }
  else 
  {
    Serial.println("Keine gültige Messung");
  }

  // Right Sensor
  digitalWrite(senden_right, LOW);
  delay(2);
  digitalWrite(senden_right, HIGH);
  delayMicroseconds(10);
  digitalWrite(senden_right, LOW);

  Zeit_right = pulseIn(echo_right, HIGH);
  Entfernung_right = (Zeit_right / 2) * 0.03432;

  // Ausgabe der Entfernungsdaten
  Serial.print("Sensor Right: ");
  if (Entfernung_right > 0) 
  {
    Serial.print("Entfernung in cm: ");
    Serial.println(Entfernung_right);
  }
  else 
  {
    Serial.println("Keine gültige Messung");
  }

  // Vergleich der Entfernungen
  if (Entfernung_left > 0 && Entfernung_right > 0) 
  {
    if (Entfernung_left < Entfernung_right)
    {
      
      Serial.println("Rechts");
    }
    else 
    {
      Serial.println("Links");
    }
  }

  delay(500); // Kurze Verzögerung, um Störungen zu minimieren
}
