from sensors.DHT_class import DHT
from sensors.barometer_class import Barometer
import time
from datetime import datetime
from WeatherRecord import WeatherRecord, initialize
from settings import get_settings

class SensorManager(object):

    def __init__(self):
        settings = get_settings()
        self.dht = DHT(5)
        if settings.BAROMETER_MODEL == "BMP085":
            self.barom = Barometer()

    def record(self):
        pressure, temp1 = self.barom.read()
        humidity, temp2 = self.dht.read()
        time = datetime.now()
        WeatherRecord.create(Time=time, Humidity=humidity, Temperature=temp1, Pressure=pressure, WindSpeed=0)
        return
    
    def recall_all_records(self):
        for record in WeatherRecord.select().order_by(WeatherRecord.Time):
            print(record.display())


if __name__ == '__main__':
    initialize()
    manager = SensorManager()
    manager.record()
    manager.recall_all_records()

