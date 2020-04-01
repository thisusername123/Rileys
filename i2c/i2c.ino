#include <Wire.h>

#define SLAVE_ADDRESS 0x04
int number = 0;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600); // start serial for output
  // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);

  // define callbacks for i2c communication
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);

  Serial.println("Ready!");

  
}

void loop() {
  delay(100);
}

// callback for received data
void receiveData(int byteCount){
  number = Wire.read();
  Serial.print("data received: ");
  Serial.println(number);

  switch (number) {
    // Analog In
    case 0 ... 7:
      Serial.print("Sending: ");
      Serial.println(number);
      Wire.write(digitalRead(number));
      break;
    // Start Motor (25%)
    case 254:
      analogWrite(11, 128);
      break;
    // Kill Motor
    case 255:
      digitalWrite(11, 0);
  }
}

// callback for sending data
void sendData(){
  Serial.print("Sending Data:");
  Serial.println(number);
  
  switch (number) {
    // Analog In
    case 0 ... 7:
      Serial.print("Sending: ");
      Serial.println(number);
      Wire.write(digitalRead(number));
      break;
    // Start Motor (25%)
    case 254:
      analogWrite(11, 128);
      break;
    // Kill Motor
    case 255:
      digitalWrite(11, 0);
  }
}
