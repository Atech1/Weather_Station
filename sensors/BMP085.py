import Adafruit_BMP.BMP085 as BMP
from barometer_class import Barometer
import time

class BMP085(Barometer):
    def __init__(self):
        super.__init__(BMP.BMP085())