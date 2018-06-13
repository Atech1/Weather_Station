import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import set_credentials_file
from graphing.GraphModel import GraphModel
from WeatherRecord import WeatherRecord, initialize
from settings import get_settings
import settings

class GraphManager(object):
    def __init__(self):
        self.settings = get_settings()
        set_credentials_file(username=self.settings.USERNAME, api_key=self.settings.GRAPHING_KEY)
        if len(self.settings.GRAPH_URIs) > 1:
            self.graphs = {name:GraphModel(title=name, uri=self.settings.GRAPH_URIs[name]) for name in self.settings.GRAPH_URIs.keys()}
        else:
            self.graphs = {name:GraphModel(title=name, uri=None) for name in self.settings.GRAPH_NAMES}
    
    def update_graphs(self):
        for graph in self.graphs.keys():
            last = self.graphs[graph].get_last()
            if last is not None:
                data = WeatherRecord.select().where(WeatherRecord.Time > last)
                self.graphs[graph].update(self.fill_in_data(self.graphs[graph].title, data))
            else:
                data = []
                for d in WeatherRecord.select().order_by(WeatherRecord.Time): data.append(d)
                self.graphs[graph].create_new(self.fill_in_data(self.graphs[graph].title, data))
        self.save()
        return
    
    def fill_in_data(self, name, data):
        attribute = [ d.getAttr(name) for d in data]
        time = [d.getAttr('Time') for d in data]
        trace = go.Scatter(y=attribute, x=time, mode='lines+markers', name=name)
        if name == 'Temperature':
            dewpoint = [d.getAttr('DewPoint') for d in data]
            trace2 = go.Scatter(y=dewpoint, x=time, mode='lines+markers', name=name)
            return [trace, trace2]
        return [trace]

    def save(self):
        for graph in self.graphs.keys():
            self.settings.GRAPH_URIs[graph] = self.graphs[graph].uri
        self.settings.save()
        return
