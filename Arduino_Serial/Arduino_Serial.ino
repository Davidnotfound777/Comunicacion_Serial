const int ledPin = 8;
String comando = "";
void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  Serial.begin(9600);
}
void loop() {
  if (Serial.available() > 0) {
    comando = Serial.readStringUntil('\n');
    comando.trim();
    if (comando == "ON") {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED ENCENDIDO");
    }
    else if (comando == "OFF") {
      digitalWrite(ledPin, LOW);
      Serial.println("LED APAGADO");
    }
  }
}
