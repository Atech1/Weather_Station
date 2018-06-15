from peewee import *
from settings import get_settings
import time
import inspect
from datetime import datetime
from random import Random

db = SqliteDatabase(None)
init = False
settings = get_settings()

class WeatherRecord(Model):
    Time = DateTimeField()
    Humidity = FloatField()
    Temperature = FloatField()
    Pressure = FloatField()
    WindSpeed = FloatField()

    def display(self):
        return "Temperature: {} C {} F, Humidity: {} %,\n Dew Point:  {} C or {} F,  Pressure {} Pa, Time: {}".format(
            self.Temperature, self.Farenhieght, self.Humidity, self.DewPoint, self.DewPointF, self.Pressure, self.Time)
    
    def getAttr(self, attr):
        return getattr(self, attr)
    
    def __getattr__(self, attr):
        return None
    
    @staticmethod
    def CtoF(temp):
        return round(((9.0/5.0) * temp) + 32, 3)

    @property
    def Farenhieght(self):
        return self.CtoF(self.Temperature)

    @property
    def DewPoint(self):
        return round(self.Temperature - (100-self.Humidity)/(5), 3)
    
    @property
    def DewPointF(self):
        return self.CtoF(self.DewPoint)

    class Meta:
        database = db

def initialize(): # do this only once
    global init, settings
    if init is False:
        if settings.DATA_LOGGING_ON:
            db.init(settings.DB_FILE)
            db.create_tables([WeatherRecord], safe=True)
            db.close()
        else:
            db.init(":memory:")
            db.create_tables([WeatherRecord], safe=True)
            db.close()
    return

def Test():
    initialize()
    record = WeatherRecord.select().get()
    for name in ['Humidity', 'Temperature', 'DewPoint', 'DewPointF', 'Thing']:
        print(record.getAttr(name))



if __name__ == '__main__':
    Test()