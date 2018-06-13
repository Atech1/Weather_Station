import plotly.plotly as py
import plotly.graph_objs as graph
from plotly.tools import set_credentials_file
from datetime import date, datetime

class GraphModel(object):

    def __init__(self, title, uri = None):
        self.title = title
        self.uri = None
    
    def update(self, data):
        layout = dict(title = self.title, xaxis = dict(title='time'), yaxis= dict(title = "percent of humidity %"))
        fg = dict(data=data, layout=layout)
        plot = py.plot(fg, filename=self.title, fileopt='extend')
        self.uri = str(plot)
    
    def get_last(self, count =0):
        if self.uri is not None:
            try:
                data = py.get_figure(self.uri).get_data()
                print(data['x'])
            except: print("graphing didn't work")
            return data.index(-1)['x']
        else:
            return None
    
    def create_new(self, data):
        layout = dict(title = self.title, xaxis = dict(title='time'))
        fg = dict(data=data, layout=layout)
        plot = py.plot(fg, filename=self.title, fileopt='new')
        self.uri = str(plot)

