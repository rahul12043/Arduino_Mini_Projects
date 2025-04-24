#include "DHT.h"
#include "RTClib.h"

#define DHT_PIN 8
#define DHTTYPE DHT22
#define LDR_PIN 9

DHT dht(DHT_PIN, DHTTYPE);
RTC_DS1307 rtc;

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(LDR_PIN, INPUT);
  
   if (!rtc.begin()) {
    Serial.println("Couldn't find RTC");
    while (1);
  }

  if (!rtc.isrunning()) {
    Serial.println("RTC is NOT running, setting the time...");
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));  // Sets time from computer compile time
  }

  delay(2000); 
}

void loop() {
  float temp = dht.readTemperature();
  float humid = dht.readHumidity();
  int ldrValue = digitalRead(LDR_PIN);

  DateTime now = rtc.now();
  if (isnan(humid) || isnan(temp)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Time: ");
  Serial.print(now.hour());
  Serial.print(":");
  Serial.print(now.minute());
  Serial.print(":");
  Serial.println(now.second());
  
  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.println(" °C");

  Serial.print("Humidity: ");
  Serial.print(humid);
  Serial.println(" %");

  Serial.print("LDR Value: ");
  Serial.println(ldrValue);

  delay(2000);
}
