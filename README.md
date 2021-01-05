# SuperEZGraver

This is the Super EZ Graver project documentation. If any of the documentation doesn't make sense or links are broken etc please letme know and I'll do my best to fix it.


## Parts list.

Some of the links are to google searches, this is because actual products will become unavailable at some point so a list of products that you can select from is probably better.

[Arduino Uno](https://store.arduino.cc/arduino-uno-rev3), this is a link to the official Uno page. You can get unofficial versions much cheaper. Other Arduinos can be used but this is a cost effective board which can be run off the same 12VDC power supply so makes it very convenient. [Ebay arduinos](https://www.google.com/search?q=arduino+uno+ebay&oq=Arduino+uno+ebay)

[Mosfet](https://www.google.com/search?q=15A+400W+DC+5V-36V+Mosfet) Link to google search for appropriate mosfet. This is used by the Arduino to send a pulse of electricity to the solenoid.

[PWM power controller](https://www.google.com/search?q=DC+6-60V+12V+24V+36V+48V+30A+PWM+DC+Motor+Speed+Controller+(PWM)) Link to google search for appropriate PWM opwer controller. This is used to control how much power is sent via the mosfet to the solenoid.

[Power Supply](https://www.google.com/search?q=DC+12V+5A+to+50A+Amp+110V+220V+Power+Supply+12V+-+AC+110+-+220) Link to google search for appropriate 12VDC power supply. The XRN-13/30TL solenoid draws a maximum of 23w which is around 1.8 amps so a 5amp power supply will be ample.

[Foot pedal - potentiometer](https://www.google.com/search?q=M-Audio+EX-P+Expression+Controller+Pedal&oq=M-Audio+EX-P+Expression+Controller+Pedal)Link to google search for potentiometer foot pedal. I use this for control of the PWM speed controler. It is not absulutly necessary as you can use the potentiometer that comes with the PWM speed controller. It does add some flexibility to allow alteration of how much power is transmmitted while engraving.

[Foot pedal - hall effect](https://www.google.com/search?q=Electric+Scooter+Foot+Throttle+Speed+Pedal+Accelerator+Bike+Golf+Cart+Go+Kart) Link to google search for hall effect foot pedal. I use this foot pedal for controling the frequency of the pulses that are sent to the solenoid. You could use a further potentiometer foot pedal for frequency control. The Arduino code will require appropriate parameter changes to use the potentiometer foot pedal.

[Solenoid](https://www.google.com/search?q=XRN-13%2F30TL+12vdc) Link to google search for XRN-13/30TL 12vdc solenoid. This is the tubular solenoid that I've used to power the  fabricated and 3d printed handpieces

[Cable connectors](https://www.google.com/search?q=Breadboard+Jumper+Wires+Ribbon+Cables+Kit+for+arduino&oq=Breadboard+Jumper+Wires+Ribbon+Cables+Kit+for+arduino) Link to google search for cable connectors. For connection of the arduino to the other components.

### Other parts

[connectors - male](https://www.google.com/search?q=1%2F4+Inch+6.35mm+Solder+Stereo+Plug%2C+Ancable+Solder+Type+Plastic+6.35mm+TRS+Phone+Connector+with+Shrinkle+Tube+for+Patch+Cables%2C+XLR+Cables) Link to google search for connectors. I use these for connection of the foot pedals to the PWM controller and Arduino.

[connectors - female](https://www.google.com/search?q=1%2F4%22+Stereo+Female+Jack+6.35mm+TRS+Panel+Mount+Socket) Link to google search for connectors. I use these for connection of the foot pedals to the PWM controller and Arduino.

[connectors - power](https://www.google.com/search?q=2.1+mm+centre-positive+barrel+plug+connector) Link to google search for connectors. For 12 power connection to the Arduino.

[Cable](https://www.google.com/search?q=Speaker+Cable+2+x+1.5+mm) Link to google search for speaker cable. I've used a cheap speaker cable which seems to work fine.

[Heat shrink tubing](https://www.google.com/search?q=heat+shrink+tubing) Link to google search for heat shrink tubing. If you are soldering cables together the assortment packs are useful for insulation once they are soldered.

You will also require a box to put everything in. I use a clear plastic storage box.

## Arduino code

The code for the arduino can be found in the [src](src) directory of theis github project.

[Arduino programming setup guide](https://www.arduino.cc/en/Guide/ArduinoUno) Link to the  guide for setting up the programming environment for the Arduino.

[Arduino setup YouTube](https://www.youtube.com/watch?v=ELUF8m24sZo) Link to the video guide for setting up the programming environment for the Arduino.

## Wiring diagram

[Mosfet and Arduino background](https://bildr.org/2012/03/rfp30n06le-arduino/) This is the background to mosfets for power control using the arduino. I've used a mosfet module that has the mosfet, diode and resister in a package so its much easier to connect the components up.

![Wiring Diagram](docs/images/wiring.svg)

# Handpiece

I've created a 3d modelled handpiece in the open source 3d modelling application [Blender](https://www.blender.org/). The [blender source files](docs/design/blender) are available to download as well as the [stl](docs/design/stl). There is a YouTube video on how to [setup the handpiece](https://www.youtube.com/watch?v=aNY35ATTJbg). This was first produced using petg but it may be better to use a more heat conductive material such as [ice9](https://tcpoly.com/shop/) for better heat dissapation. I've not tried this yet.

The first handpiece that I made was fabricated from brass and delrin. A YouTube video is available for the [handpiece](https://www.youtube.com/watch?v=D4yPBS8mucQ) along with a video on the handpiece [design refinement](https://www.youtube.com/watch?v=ALAtECnq1Rg)






 