# this is a setting file to separate out what is needed to run this
import sqlite3
import json
import jsonpickle

class Settings(object):

    def __init__(self):
        self.DATA_LOGGING_ON = True # this will record to :memory: if False
        self.DB_FILE = "Weather_Data.db" # name of the file saved to.

        self.OFFLINE = False
        self.GRAPHING_ON = True
        self.GRAPH_NAMES = ["Humidity", "Temperature", "Pressure"]
        self.USERNAME = "studentAl"
        self.GRAPHING_KEY = "s5rOqZu8dwFdDrwriB5u" # make a plotly account and find the key
        self.GRAPH_URIs = {}
        self = self.load()
        print(self.OFFLINE)

    def load(self):
        with open("settings.json", 'r') as setting_file:
            self = jsonpickle.decode(setting_file.read())
            print(self.OFFLINE)
            return self

    def save(self):
        this = jsonpickle.encode(self, unpicklable=False)
        with open("settings.json", 'w') as setting_file:
            setting_file.write(this)
        return

def main():
    settings = Settings()
    print(settings.OFFLINE)

if __name__ == '__main__':
    main()