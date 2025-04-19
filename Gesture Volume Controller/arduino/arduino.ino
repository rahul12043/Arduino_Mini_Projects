#define TRIG_PIN 9
#define ECHO_PIN 10

void setup() {
  Serial.begin(9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

float getDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  long duration = pulseIn(ECHO_PIN, HIGH);
  return duration * 0.034 / 2; // Distance in cm
}

void loop() {
  float distance = getDistance();
  
  if (distance < 15) {          // Close range (0-15cm)
    Serial.println("VOLUME_UP");
  } 
  else if (distance < 27) {     // Mid range (15-30cm)
    Serial.println("VOLUME_DOWN");
  }
  
  delay(150); // Reduced delay for faster response
}