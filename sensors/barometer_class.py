import time

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
    

