# Newstream

PennApps XV Project. Newstream aggregates news from a multitude of sources from the New York Times to Ars Technica and performs sentiment analysis on the articles to give an estimate on the overall sentiment (negative to positive) of that topic. Our goal was to visualize this data in a user-friendly, minimalist interface that was clear and concise.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need Python 3.5 and to install Flask, Indico, Plotly and Python-Twitter. You will need an API key for Twitter, Indico, Plotly and Firebase.

### Installing

```
$ pip3.5 install flask
```

```
$ pip3.5 install indicoio
```

```
$ pip3.5 install plotly
```

```
$ pip3.5 install python-twitter
```

### Running

Either run in your development environment or in the console:

```
$ export FLASK_APP=main.py
$ flask run
```

The server will start at 127.0.0.1:5000/.

## Built With

* [Flask](https://flask.pocoo.org) - Backend framework
* [News API](https://newsapi.org) - For retrieving articles
* [Twitter API](https://github.com/bear/python-twitter) - For retrieving articles, supplementing data used for sentiment analysis
* [Indico API](https://indico.io/) - Text analysis library, for calculating sentiment
* [Plotly API](https://plot.ly/python/) - For generating graph
* [Firebase API](https://firebase.google.com/) - For caching searches

## Authors

* **Eric Liu** - *Frontend and backend* - [eliucs](https://github.com/eliucs)
* **Jason Pham** - *Backend* - [suchAHassle](https://github.com/suchAHassle)
