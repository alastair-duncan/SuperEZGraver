# Command line testing
import machine
import time
from machine import Pin, PWM

outputPin = 0
pulseLength = 10     # ms
maxFreq = 5000/60   # Hz - representation is Strokes Per Minute
speedBias = 0.05  # ignore any readings below this and don't switch on
pwmFreq = 1000  # max 1000
pwmRange = 1023

def runGraver(speed, power, duration):
    # speed 0.0..1.0
    # power 0.0..1.0
    # duration seconds
    offTime = (int)(1000/(maxFreq * speed)) - pulseLength
    assert True, offTime >= pulseLength # 50% overall duty cycle max

    pwmPin = PWM(Pin(outputPin))
    pwmPin.freq(pwmFreq)

    if speed >= speedBias:
        startTime = time.ticks_ms()
        while time.ticks_diff(time.ticks_ms(), startTime) < duration * 1000:
                # on
                pwmPin.duty(power * pwmRange)
                time.sleep_ms(pulseLength)
                # Switch off
                pwmPin.duty(0)
                # Wait
                time.sleep_ms(offTime)
        print("Duration complete")

    else:
        print("Speed < bias, ignore")

    pwmPin.deinit()