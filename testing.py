from WeatherRecord import WeatherRecord, initialize
from graphing.GraphManager import GraphManager
from random import Random
from datetime import datetime, date
from settings import get_settings


def make_test_data(s,time, r):
    for m in range(s, time):
        for d in range(1, 28):
            for h in range(1, 23, 4):
                data = sensor_test_data(r)
                WeatherRecord.create(Temperature=data[0], Humidity=data[1], Pressure=data[2], Time=datetime(2015, m, d, h), WindSpeed=0)

def sensor_test_data(r):
    temperature = r.triangular(15.0, 25.0)
    humidity = r.triangular(20.0, 100.0)
    pressure = r.triangular(1009.0, 1030.0, 1023.0)
    return [temperature, humidity, pressure]

def recall_all_records():
    print("printing all")
    for record in WeatherRecord.select():
        print(record.display())

def main():
    r = Random()
    initialize()
    make_test_data(2, 3, r) # pre-fetch
#    recall_all_records()
    gp = GraphManager()
    gp.update_graphs()



if __name__ == '__main__':
    main()
