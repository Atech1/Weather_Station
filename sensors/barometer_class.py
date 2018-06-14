import time
from BMP085 import BMP085
class Barometer(object):
    
    def __init__(self, sensor = None):
        self.sensor = sensor

    def read(self):
        temp = self.sensor.read_temperature()
        pressure = self.sensor.read_pressure()
        return pressure, temp
    
    def destroy(self):
        # GPIO.cleanup()
        return
    
    @staticmethod
    def BMP085():
        return BMP085()
