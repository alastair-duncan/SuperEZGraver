
from machine import Pin, PWM, ADC, I2C
import utime, math, _thread
from ssd1306 import SSD1306_I2C
from oled import Write, GFX, SSD1306_I2C
from oled.fonts import ubuntu_mono_15

# setup the oled display
WIDTH =128
HEIGHT= 32
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=400000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)
write15 = Write(oled, ubuntu_mono_15)


#output pin for PWM values this is connected to the mosfet
pwm13 = PWM(Pin(13))
#assign the pin to read the power values from
pot_pwm = ADC(28)
#assign the pin to read the frequency values from
pot_freq = ADC(27)
#set the frequency of the pwm output
pwm13.freq(400)
#setup some variables to be used in the while loop
duty_cycle_val = 0
pot_freq_val = 0
#the frequency value is in the range of 0 to 65536 which will be divided by the quantisation_factor which gives 65536//quantisation_factor different speed values
#this seems to work ok. If a finer granularity is required then change the quantisation_factor
quantisation_factor = 655
#using 100 here unsigned int16 max
max_freq_sleep = 65536//quantisation_factor
# adjust this value if a faster frequency is required, lower values = more rpms - remember that lower values will produce more heat
default_sleep_freq = 25
# this value determins how long the power is applied to the solenoid. 15ms seems to be the lowest for the 13/30 for a full length stroke
# this may need altering for different solenoids - higher values will produce more heat.
default_sleep_duty = 15
#values from 1 to slow_speed_value will be slowed right down 
slow_speed_value = 30
duty_percent = 0
freq_rpm = 0

sLock = _thread.allocate_lock()

def updateDisplay():
    
    while True:
        #percentage calc for the display
        duty_percent =  math.ceil((duty_cycle_val / 65536) * 100)
        write15.text("freq:           ", 0, 0)
        write15.text("duty:           ", 0, 15)
        write15.text("freq: " + str(freq_rpm), 0, 0)
        write15.text("duty: " + str(duty_percent), 0, 15)
        oled.show()

# map function taken directly from arduino codebase
def map(value_to_map, fromLow, fromHigh, toLow, toHigh):
    """
        Re-maps a number from one range to another. That is, a value of fromLow would get mapped to toLow, a value of fromHigh to toHigh, values in-between to values in-between, etc.

        Parameters
        ----------unsigned int16
        value_to_map : value read from the pin
        ----------unsigned int16 max
        fromLow: the lower bound of the value’s current range.
        ----------unsigned int16 
        fromHigh: the upper bound of the value’s current range.
        ----------unsigned int16 
        toLow: the lower bound of the value’s target range.
        ----------unsigned int16 
        toHigh: the upper bound of the value’s target range.
    """
    return int((value_to_map - fromLow) * (toHigh - toLow) / (fromHigh - fromLow) + toLow)
        
# as the pi pico has 2 cores run the oled update in a thread as it will affect the timing otherwise
# oled device is pretty slow and will block execution and hence slow down the system
# no need for synchronisationas its a read operation from a shared global variable
#synchronisation affects the timing of the system, slows everything down.
_thread.start_new_thread(updateDisplay,())

print(" **************************************************************** ")
print(" Super EZ Graver pi pico software ")
print(" **************************************************************** ")
while True:
    
    #freq_rpm = 0
    pot_freq_val = pot_freq.read_u16()//quantisation_factor
    
    if (pot_freq_val > 1 ):
        #read the value from the foot pedal potentiometer range of 0-65536
        duty_cycle_val = pot_pwm.read_u16()
        #print("duty " + str(duty_cycle_val))
        #remap the value to one that is meaningful, anything under 30000 will not power the solenoid
        duty_cycle_val = map(duty_cycle_val, 150, 65536, 20000, 65536)
        # the duty cycle value has been remapped from 30000 to 65536 but the least value should be 0 otherwise
        # there will still be power being transmitted to the solenoid at the lowest value even if there is
        # not enough power to move the piston so anything under the minimum swithc it off
        if (duty_cycle_val < 30000):
            duty_cycle_val = 0
        
        #print("duty " + str(int((duty_cycle_val / 65536) * 100)))
        pwm13.duty_u16(duty_cycle_val)
        # the value of 15ms or above alows for the full travel of the XRN13/30 solenoid a different solenoid may require adjustment of this value 
        #print("duty_ns " + str(pwm13.duty_ns()))
        utime.sleep_ms(default_sleep_duty)
        #make sure there's no power
        pwm13.duty_u16(0)
        # a linear ramp up of speed is not necessarily required so manipulate is slightly
        #so that when its slow its really slow
        #if its a slow speed value slow it right down
        if(pot_freq_val < slow_speed_value):
            # delay before next hit, ramp up the speed slowly so that its a smooth transition
            # this is in addition to the rpm sleep but only added for lower rpms
            rpm_sleep_time = ((slow_speed_value  - pot_freq_val) * 10)
            #print("rpm_sleep_time = " + str(rpm_sleep_time))
            utime.sleep_ms(rpm_sleep_time)
        else:
            #needs to be reset if its done here the display behaves itself better
            freq_rpm = 0
        freq_rpm = 65536 // (freq_rpm + (default_sleep_freq + (max_freq_sleep - pot_freq_val)))
      
    else:
        freq_rpm = 0
    #switch off the power 
    pwm13.duty_u16(0)
    
    # this calculation smooths out ramp up, if the default_sleep_freq is used then its very top heavy, not much movement in the pedal before its at max rpm
    # this makes it much more usable - for me at least ;-)
    sleep_time = (default_sleep_freq + (max_freq_sleep - pot_freq_val))
    #print("sleep_time = " + str(sleep_time))
    #and go to sleep
    utime.sleep_ms(sleep_time)
     