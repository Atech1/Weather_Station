from sensors.DHT_class import DHT
from sensors.barometer_class import Barometer
from sensors.Wind_Sensor import WindSensor
import time
from datetime import datetime
from WeatherRecord import WeatherRecord, initialize
from settings import get_settings
from sensors.BMP085 import BMP085

class SensorManager(object):

    def __init__(self):
        initialize()
        settings = get_settings()
        self.dht = DHT(settings.DHT_PIN)
        self.windsensor = WindSensor()
        if settings.BAROMETER_MODEL == "BMP085":
            self.barom = BMP085()

    def record(self):
        pressure, temp1 = self.barom.read()
        humidity, temp2 = self.dht.read()
        windspeed = self.windsensor.read()
        time = datetime.now().strftime("%Y-%m-%d %H:%M")
        WeatherRecord.create(Time=time, Humidity=humidity, Temperature=temp1, Pressure=pressure, WindSpeed=windspeed)
        return
    
    def recall_all_records(self):
        for record in WeatherRecord.select().order_by(WeatherRecord.Time):
            print(record.display())


if __name__ == '__main__':
    manager = SensorManager()
    manager.record()
    manager.recall_all_records()

