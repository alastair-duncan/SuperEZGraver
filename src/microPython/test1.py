#
# First test using microPython
#

import machine, time
from machine import Pin, PWM, ADC

pulseLength = 10     # ms
maxFreq = 5000/60   # Hz - representation is Strokes Per Minute
maxADCdeflection = 1024
outputPin = 0
speedPin = 1
powerPin = 2
speedBias = 20 # ignore any readings below this and don't switch on
pwmFreq = 1000 # max 1000
# configure PWM output pin
#  Duty cycle is 0..1023
pwmPin = PWM(Pin(outputPin))
pwmPin.freq(pwmFreq)

# configure input pin for analogue input - speed
# NB needs to be 0..1.0VDC
# read() method returns 0..1024 - check this, really not 1023?
speedSetting = ADC(speedPin)

# configure input pin for analogue input - PWM duty cycle (power)
powerSetting = ADC(powerPin)

# loop
while (True):

    # Read speed analogue input, quantise 
    currentSpeed = maxADCdeflection - speedSetting.read() # Low resistance = high Voltage, high speed
    # Read power input 
    currentPower = maxADCdeflection - powerSetting.read() # Low resistance = high power

    if (currentSpeed >= speedBias):
        # set PWM output level on   
        pwmPin.duty(currentPower)
        # Pulse length dictates duty cycle, determine minimum possible.
        # For max speed of 5000SPM can't go above 6ms and manage 50% duty cycle (assuming max power)
        time.sleep_ms(pulseLength)
        # Set output low - off time
        pwmPin.duty(0)

        quantisedPeriod = 1/(maxFreq * currentSpeed/maxADCdeflection) * 1000 # ms
        time.sleep_ms(quantisedPeriod - pulseLength)
    else:
        time.sleep_ms(100) #  Because why not



