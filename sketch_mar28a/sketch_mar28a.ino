#include <string.h>
#include <Wire.h>

int motor = 11; //this is the pin number
int inputFromPi = 7; //same ^^
int sens1 = 0;
int sens2 = 0;
int sens3 = 0;
int sens4 = 0;
int sens5 = 0;
int sens6 = 0;
int sens7 = 0;
int sens8 = 0;

double currentOutput = 0;
double lastTime = 0;
byte sensor_request = 0;
byte sensor_value = 0;

//Function to give values back to PI
void requestEvent(){
   Serial.print("Request");
   Wire.write(sensor_value);
}

void receiveEvent(int howMany){
 Serial.print("howMany: ");
 Serial.print(howMany);
 while(Wire.available() > 1){
    sensor_request = Wire.read(); // receive byte as a character
    Serial.print(sensor_request);         // print the character
  }
  sensor_request = Wire.read();    // receive byte as an integer
  Serial.println(sensor_request);   
}


void setup() {
  Serial.begin(9600);
  pinMode(motor, OUTPUT);
  pinMode(inputFromPi, INPUT);
  pinMode(sens1, INPUT);
  pinMode(sens2, INPUT);
  pinMode(sens3, INPUT);
  pinMode(sens4, INPUT);
  pinMode(sens5, INPUT);
  pinMode(sens6, INPUT);
  pinMode(sens7, INPUT);
  pinMode(sens8, INPUT);
  Wire.begin(27);                // join i2c bus with address 27
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);

}

void loop() {
  if(digitalRead(inputFromPi)){
    digitalWrite(motor, rampUp(0.01, 127));
  }else{
    digitalWrite(motor, rampDown(0.01, 0));
  }
}

double rampUp(double rampRate, double setpoint){
  double output = currentOutput;
  double time2 = millis() + lastTime;
  double incr = (time2 - lastTime) * rampRate;
  if(output + incr > setpoint){
    output = setpoint;
  }else{
    output += incr;
  }
  lastTime = time2;
  currentOutput = output;
  return output;
}

double rampDown(double rampRate, double setpoint){
  double output = currentOutput;
  double time1 = millis() + lastTime;
  double decr = -((time1 - lastTime) * rampRate);
  if(output + decr < setpoint){
    output = setpoint;
  }else{
    output += decr;
  }
  lastTime = time1;
  currentOutput = output;
  return output;
}
