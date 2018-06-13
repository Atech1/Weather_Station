# this is a setting file to separate out what is needed to run this
import sqlite3
import json
import jsonpickle
import copy

class Settings(object):

    def __init__(self):
        self.BAROMETER_MODEL = "BMP085"
        self.DATA_LOGGING_ON = True # this will record to :memory: if False
        self.DB_FILE = "Weather_Data.db" # name of the file saved to.
        self.OFFLINE = False

        self.GRAPHING_ON = True
        self.GRAPH_NAMES = ["Humidity", "Temperature", "Pressure"]
        self.USERNAME = "studentAl"
        self.GRAPHING_KEY = "s5rOqZu8dwFdDrwriB5u" # make a plotly account and find the key
        self.GRAPH_URIs = {}

    def load(self):
        with open("settings.json", 'r') as setting_file:
            obj = jsonpickle.decode(setting_file.read())
        self.__dict__.update(obj)
        return

    def save(self):
        this = json.dumps(json.loads(jsonpickle.encode(self, unpicklable=False)), indent=4)
        with open("settings.json", 'w') as setting_file:
            setting_file.write(this)
        return


settings = Settings()
settings.load()

def get_settings():
    return settings

if __name__ == '__main__': # example of how to use this class
    settings = get_settings()
    print(settings.OFFLINE)
