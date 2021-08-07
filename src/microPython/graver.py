
import queue
import threading
import time

#  Class for the graver
class Graver(threading.Thread):

    __debug = True

    def __init__(self, speedQueue, powerQueue):
        self.currentSpeed = 0
        self.currentPower = 0
        self.pulseLength = 10     # ms
        self.maxFreq = 2500/60   # Hz - representation is Strokes Per Minute
        self.bias = 0.05

        self.speedQueue = speedQueue
        self.powerQueue = powerQueue

        self.__running = True

    def __readQueues():
        # Speed
        # lock
        if not self.speedQueue.empty():
            self.currentSpeed = self.speedQueue.get()
            if __debug:
                print("graver - speed read as ", self.currentSpeed)

        if not self.powerQueue.empty():
            self.currentPower = self.powerQueue.get()
            if __debug:
                print("graver - power read as ", self.currentPower)

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
                # Switch off
                # Wait
            else
                # sleep 100ms

        # Cleanup - shutdown output

# Check limitations of microPython + threads

# Class for the input ADC

class Input(threading.Thread):

    __debug = True

    def __init__(self, pin, range, outputQueue)
        # Configure the pin for ADC
        self.pin = pin
        self.range = range
        self.outputQueue = outputQueue

        self.sleepTime = 100 # ms

        self.__running = True

    def terminate():
        self.__running = False

    def run(self):
        while self.__running:
            # Read input
            # Get queue lock
            # Push value to queue (NB do we interpret this to a fixed range? 0..1 for example?)
            # Release queue lock
            # sleep

        # Cleanup