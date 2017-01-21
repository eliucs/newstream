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

'''
    getDates() returns a list containing the dates of the
    last five days (including today's date)
'''
def getDates():
    dates = list()

    for i in range(5):
        date = datetime.now() - timedelta(days=i)
        dateFormatted = date.strftime('%A %B %d')
        dates.append(dateFormatted)

    dates.reverse()

    return dates

dates = getDates()

# Mock data, need to be replaced by actual sentiment
sentiment = [0.123456, 0.345678, 0.234567, 0.678901, 0.456789]

# create graph trace
trace = go.Scatter(
    x = dates,
    y = sentiment,
    name = 'Sentiment',
    line = {'color': 'rgb(22, 96, 167',
            'width': 4}
)

data = [trace]

layout = {'xaxis': {'title': 'Last 5 Days'},
          'yaxis': {'title': 'Sentiment Score'}}

fig = {'data': data,
       'layout': layout}

url = py.plot(fig, filename='graph', auto_open=False)
html = tls.get_embed(url, width='100%', height=400)

print(html)
