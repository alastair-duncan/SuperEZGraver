# Command line testing
# Note that on ESP8266 module, pin 0 is high on reboot.  Don't power the solenoid until the init code has been run.

import machine
import time
from machine import Pin, PWM

# Defaults
outputPin = 0               # 
defaultPulseLength = 15     # ms
maxFreq = 2500/60           # Hz - representation is Strokes Per Minute
speedBias = 0.01            # ignore any readings below this and don't switch on
pwmFreq = 1000              # max 1000
pwmRange = 1023             # Will vary

coolingTime = 4

# Init the PWM - primarily, turn it off if on
pwmPin = PWM(Pin(outputPin))
pwmPin.freq(pwmFreq)
pwmPin.duty(0)

#
# runGraver
#
# Inputs:
# speed 0.0..1.0 - proportion of maxFreq
# power 0.0..1.0 - sets PWM duty cycle (0..100%)
# duration - how long to run the test in seconds
# pulseLength - optional, will default to defaultPulseLength
#
# Outputs:
# Drives solenoid via PWM
#
# Returns:
# None
#
def runGraver(speed, power, duration, pulseLength = defaultPulseLength):
    # speed 0.0..1.0
    if speed < 0.0 or speed > 1.0:
        print("Error - speed must be in the range 0.0..1.0")
        return 

    if power < 0.0 or power > 1.0:
        print("Error - power must be in the range 0.0..1.0")
        return

    offTime = (int)(1000/(maxFreq * speed)) - pulseLength
    duty = (int)(power * pwmRange)

    if offTime <= pulseLength:
        offTime = pulseLength # 50% overall duty cycle max
        print("\nOff time throttled")

    print()
    print("On time = ", pulseLength, "ms")
    print("Off time = ", offTime, "ms")
    print("SPM = ", (60 * 1000/(pulseLength + offTime)))
    print("Duration = ", duration, "s")
    print()

    cumulativeOnTime = 0;

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

                # Guard the solenoid - it doesn't like being energised for long and there's not much detail on actual duty cycles
                cumulativeOnTime += pulseLength
                if cumulativeOnTime >= 2000:
                    print("2s on-time reached; cooling")
                    duration += coolingTime
                    time.sleep(coolingTime)
                    cumulativeOnTime = 0
                    print("Continue")

        print("Duration complete")

    else:
        print("Speed < bias, ignore")


    pwmPin.deinit()