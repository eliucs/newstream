'''

    graph.py

    This module uses the Plotly library to generate the code to
    embed an iframe with a graph given sentiment data of the last
    5 days.

'''


from datetime import datetime, timedelta
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls

py.sign_in('ericliu', 'rSJWRQWumGJUoETt3end')

class Graph:

    def __init__(self, sentiment):
        self._sentiment = sentiment


    '''
        getDates() returns a list of the last five says in
        day-of-week month day format
    '''
    def _getDates(self):
        dates = list()

        for i in range(5):
            date = datetime.now() - timedelta(days=i)
            dateFormatted = date.strftime('%A %B %d')
            dates.append(dateFormatted)

        dates.reverse()

        return dates


    '''
        getGraph() creates a graph of the sentiments of the last five days
        from the list of sentiments and returns the html link
    '''
    def getGraph(self):
        dates = self._getDates()

        # Create graph trace
        trace = go.Scatter(
            x=dates,
            y=self._sentiment,
            name='Sentiment',
            line={'color': 'rgb(22, 96, 167',
                  'width': 4}
        )

        data = [trace]

        layout = {'xaxis': {'title': 'Last 5 Days'},
                  'yaxis': {'title': 'Sentiment Score'}}

        fig = {'data': data,
               'layout': layout}

        url = py.plot(fig, filename='graph', auto_open=False)
        html = tls.get_embed(url, width='100%', height=400)

        return html
