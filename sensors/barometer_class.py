import Adafruit_BMP.BMP085 as BMP
import time

class Barometer(object):
    
    def __init__(self):
        self.sensor = BMP.BMP085()

    def read(self):
        temp = self.sensor.read_temperature()
        pressure = self.sensor.read_pressure()
        return pressure, temp
    
    def destroy(self):
        #GPIO.cleanup()
        return

if __name__ == "__main__":
    barom = Barometer()
    while(True):
        try:
            print(barom.read())
            time.sleep(0.5)
        except KeyboardInterrupt:
            barom.destroy()
            
