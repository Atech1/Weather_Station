import Adafruit_BMP.BMP085 as BMP
from barometer_class import Barometer
import time

class BMP085(Barometer):
    def __init__(self):
        super.__init__(BMP.BMP085())
    
    def read(self):
        temp = self.sensor.read_temperature()
        pressure = self.sensor.read_pressure()
        return pressure, temp