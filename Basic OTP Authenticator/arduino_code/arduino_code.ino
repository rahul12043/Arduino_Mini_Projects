#include <Wire.h>
#include <RTClib.h>

RTC_DS3231 rtc;
const int buttonPin = 2;  // Button connected to pin 2
unsigned long lastSent = 0;
const unsigned long debounceDelay = 500;  // Debounce delay for button press

void setup() {
  Serial.begin(9600);
  rtc.begin();
  pinMode(buttonPin, INPUT_PULLUP);  // Set the button pin as input with pull-up

  // Optional: Check RTC is running fine
  if (!rtc.begin()) {
    Serial.println("Couldn't find RTC");
    while (1);  // Infinite loop if RTC is not found
  }
}

void loop() {
  static bool lastButtonState = HIGH;
  bool buttonState = digitalRead(buttonPin);

  // Handle button press
  if (buttonState == LOW && lastButtonState == HIGH && (millis() - lastSent > debounceDelay)) {
    sendOTP();  // Send OTP when button is pressed
    lastSent = millis();  // Update the last sent time to debounce the button
  }

  lastButtonState = buttonState;  // Update the button state
}

void sendOTP() {
  DateTime now = rtc.now();
  uint32_t timestamp = now.unixtime();

  // Format the data into JSON manually
  String jsonString = "{";
  jsonString += "\"rtc_time\":\"" + String(now.year()) + "-" + String(now.month()) + "-" + String(now.day()) + " " + 
                String(now.hour()) + ":" + String(now.minute()) + ":" + String(now.second()) + "\",";
  jsonString += "\"unix_time\":" + String(timestamp) + ",";
  
  uint32_t timeChunk = timestamp / 30;  // Create time-based chunks for OTP generation
  uint32_t secret = 0xABCDEF;  // Secret key for OTP generation
  uint32_t otp = (timeChunk ^ secret) % 1000000;  // XOR the time chunk with the secret and mod by 1 million
  jsonString += "\"otp\":" + String(otp);
  
  jsonString += "}";

  // Send the JSON string to Python via Serial
  Serial.println(jsonString);
}
