# SuperEZGraver

This is the Super EZ Graver project documentation. If any of the documentation doesn't make sense or links are broken etc please letme know and I'll do my best to fix it.


## Parts list.

Some of the links are to google searches, this is because actual products will become unavailable at some point so a list of products that you can select from is probably better.

[Arduino Uno](https://store.arduino.cc/arduino-uno-rev3), this is a link to the official Uno page. You can get unofficial versions much cheaper. Other Arduinos can be used but this is a cost effective board which can be run off the same 12VDC power supply so makes it very convenient.

[Mosfet](https://www.google.com/search?q=15A+400W+DC+5V-36V+Mosfet) Link to google search for appropriate mosfet. This is used by the Arduino to send a pulse of electricity to the solenoid.

[PWM power controller](https://www.google.com/search?q=DC+6-60V+12V+24V+36V+48V+30A+PWM+DC+Motor+Speed+Controller+(PWM)) Link to google search for appropriate PWM opwer controller. This is used to control how much power is sent via the mosfet to the solenoid.

[Power Supply](https://www.google.com/search?q=DC+12V+5A+to+50A+Amp+110V+220V+Power+Supply+12V+-+AC+110+-+220) Link to google search for appropriate 12VDC power supply. The XRN-13/30TL solenoid draws a maximum of 23w which is around 1.8 amps so a 5amp power supply will be ample.

[Foot pedal - potentiometer](https://www.google.com/search?q=M-Audio+EX-P+Expression+Controller+Pedal&oq=M-Audio+EX-P+Expression+Controller+Pedal)Link to google search for potentiometer foot pedal. I use this for control of the PWM speed controler. It is not absulutly necessary as you can use the potentiometer that comes with the PWM speed controller. It does add some flexibility to allow alteration of how much power is transmmitted while engraving.

[Foot pedal - hall effect](https://www.google.com/search?q=Electric+Scooter+Foot+Throttle+Speed+Pedal+Accelerator+Bike+Golf+Cart+Go+Kart) Link to google search for hall effect foot pedal. I use this foot pedal for controling the frequency of the pulses that are sent to the solenoid. You could use a further potentiometer foot pedal for frequency control. The Arduino code will require appropriate parameter changes to use the potentiometer foot pedal.

[Solenoid](https://www.google.com/search?q=XRN-13%2F30TL+12vdc) Link to google search for XRN-13/30TL 12vdc solenoid. This is the tubular solenoid that I've used to power the  fabricated and 3d printed handpieces

 
 



