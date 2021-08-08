
import queue
import threading
import time

#  Class for the graver
class Graver(threading.Thread):

    __debug = True

    def __init__(self, speedQueue, powerQueue):
        self.currentSpeed = 0.0     # 0..1.0
        self.currentPower = 0.0     # 0..1.0
        self.pulseLength = 10       # ms
        self.maxFreq = 2500/60      # Hz - representation is Strokes Per Minute
        self.bias = 0.05

        self.speedQueue = speedQueue
        self.powerQueue = powerQueue

        self.__running = True

    def __readQueues(self):
        # Speed
        # lock
        if not self.speedQueue.empty():
            self.currentSpeed = self.speedQueue.get()
            if self.__debug:
                print("graver - speed read as ", (int)(self.currentSpeed * 100), "%")

        if not self.powerQueue.empty():
            self.currentPower = self.powerQueue.get()
            if self.__debug:
                print("graver - power read as ", (int)(self.currentPower * 100), "%")

    def setSpeed(self, speed):
        self.currentSpeed = speed

    def getSpeed(self):
        return self.currentSpeed

    def setPower(self, power):
        self.CurrentPower = power

    def getPower(self):
        return self.currentPower

    def terminate(self):
        self.__running = False

    def run(self):
        while self.__running:
            self.__readQueues()
            if self.CurrentSpeed > self.bias:
                # Switch on
                # Wait
                time.sleep_ms(self.pulseLength)
                # Switch off
                # Wait
                offTime = 1000/(self.maxFreq * self.currentSpeed) - self.pulseLength
                time.sleep_ms(offTime)

                if self.__debug:
                    print("Tick")
            else:
                # sleep 100ms
                time.sleep_ms(50)   # 1/2 of sample rate for input
                if self.__debug:
                    print("Speed < bias")

        # Cleanup - shutdown output
        if self.__debug:
            print("Shutdown")

# Check limitations of microPython + threads

# Class for the input ADC

class Input(threading.Thread):

    __debug = True

    def __init__(self, pin, range, outputQueue):
        # Configure the pin for ADC
        self.pin = pin
        self.range = range
        self.outputQueue = outputQueue
        self.currentValue = 0.0
        self.sleepTime = 100 # ms - sample rate

        self.__running = True

    def terminate(self):
        self.__running = False

    def run(self):
        while self.__running:
            # Read input
            self.currentValue = 0.0
            # Get queue lock
            # Push value to queue (NB do we interpret this to a fixed range? 0..1 for example?)
            # Release queue lock
            # sleep
            if self.__debug:
                print("Current input reading for ", self, " = ", self.currentValue)

        # Cleanup