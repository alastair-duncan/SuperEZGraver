/*
   Arduino Uno sketch to show how it can be used as a speed controller for
   driving a solenoid
*/


/*
    this is the pwm digital pin 2 in this example
*/
#define MOSFET_PIN 2

/*
 * This is the pin used to determin which type of pedal is connected
 * Not connected by default so assume its hall effect
 * if connected to ground then it will be detected as m-audio pedal
 */
#define JUMPER_PIN 7
/*
   sensor pin for the accellerator pedal
*/
#define ACCELERATOR_PEDAL  1

//default pedal type is hall effect
int pedal_type = 0;

#define QUANTIZATION_FACTOR 201
void setup() {
  // uncomment if you want to use the serial monitor on your computer
  Serial.begin(115200);
  // tell thje arduino that the mosfet pin is an output
  pinMode(MOSFET_PIN, OUTPUT);
  pinMode(JUMPER_PIN, INPUT_PULLUP);

  if (digitalRead(JUMPER_PIN) == LOW)
  {
    //jumper is inserted pedal type is m-audio
    pedal_type = 1;
    Serial.print("Pedal type is set for M-Audio ");
  }
  else{
    // default pedal type
    Serial.print("Pedal type is set for Hall effect pedal ");
  }
}

void loop() {
  /*
     grab the value from the sensor pin and map it to the quantization factor.
     In this example there will be 200 different speed values
     pot_value is the mapped potentiometer value
  */
  int pot_value;
  // hall effect footpedal values
  if(pedal_type == 0){
    pot_value = map(analogRead(ACCELERATOR_PEDAL), 180, 875, -2, QUANTIZATION_FACTOR);
    pot_value = QUANTIZATION_FACTOR - pot_value;
  } 
  else{
    // m-autio pedal
    pot_value = map(analogRead(ACCELERATOR_PEDAL),0,1023, 0, QUANTIZATION_FACTOR);
  }
  
  // uncomment if you want to see the values of the potentiometer in the serial monitor
  // Serial.print("acc ");
  // Serial.println( pot_value);

  //

  /*
     if the mapped potentiometer value is in the range
     0 to 199 then write to the mosfet pin
  */
  
  if (pot_value < 200) {
    //Serial.println( "About to write high");
    digitalWrite(MOSFET_PIN, HIGH);
    // this is to give the solenoid time to act, for different solenoids this may have to be larger!!
    delay(15);
    
    digitalWrite(MOSFET_PIN, LOW);
    //this is the speed control here. it also determins the duty cycle for the solenoid
    delay(pot_value + 25);
  } else
  {
    // if its out of the 0 - 199 range ensure that the mosfet is low
    digitalWrite(MOSFET_PIN, LOW);
    delay(pot_value+20);
  }

}
