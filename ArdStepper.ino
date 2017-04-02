#include <Stepper.h>

int stepsPerRev = 12;  //number of steps per revolution
Stepper Step(stepsPerRev, 8, 9, 10, 11); // pin initialization
int n=5;  //initial value of 'n'- number of times to actuate the stepper at 30 degree

void setup() 
{
  Serial.begin(9600);
}

void loop() 
{ 
  Step.setSpeed(60);
  Step.step(n);
  if(Serial.available())
  {
    n=Serial.read();
  }
  delay(1000);
}
