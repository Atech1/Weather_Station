from sensors.SensorManager import SensorManager
from graphing.GraphManager import GraphManager
import schedule
import time

def main():
    sensors = SensorManager()
    graphs = GraphManager()
    schedule.every(5).seconds.do(sensors.record())
    schedule.every(1).minutes.do(sensors.recall_all_records())



if __name__ == '__main__':
    main()
    print('doing scheduled work')
    while True:
        schedule.run_pending()
        time.sleep(0.5)
