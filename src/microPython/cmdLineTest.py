# Command line testing
# Note that on ESP8266 module, pin 0 is high on reboot.  Don't power the solenoid until the init code has been run.

import machine
import time
from machine import Pin, PWM

outputPin = 0
pulseLength = 15     # ms
maxFreq = 5000/60   # Hz - representation is Strokes Per Minute
speedBias = 0.05  # ignore any readings below this and don't switch on
pwmFreq = 1000  # max 1000
pwmRange = 1023

pwmPin = PWM(Pin(outputPin))
pwmPin.freq(pwmFreq)
pwmPin.duty(0)

def runGraver(speed, power, duration):
    # speed 0.0..1.0
    if speed < 0.0 or speed > 1.0:
        print("Error - speed must be in the range 0.0..1.0")
        return 

    if power < 0.0 or power > 1.0:
        print("Error - power must be in the range 0.0..1.0")
        return

    # power 0.0..1.0
    # duration seconds
    offTime = (int)(1000/(maxFreq * speed)) - pulseLength
    duty = (int)(power * pwmRange)

    assert True, offTime >= pulseLength # 50% overall duty cycle max


    if speed >= speedBias:
        startTime = time.ticks_ms()
        while time.ticks_diff(time.ticks_ms(), startTime) < duration * 1000:
                # on
                pwmPin.duty(duty)
                time.sleep_ms(pulseLength)
                # Switch off
                pwmPin.duty(0)
                # Wait
                time.sleep_ms(offTime)
        print("Duration complete")

    else:
        print("Speed < bias, ignore")

    pwmPin.deinit()