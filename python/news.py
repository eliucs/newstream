import json
from urllib.request import urlopen


class News:
    def __init__(self, query):
        self._query = query

    def getArticles(self):
        filteredArticles = []

        url = 'http://newsapi.org/v1/articles?'
        with open('sources.json') as data_file:
            sources = json.load(data_file)

        for source in sources['sources']:
            root = 'source=' + source['id'] + '&apiKey='
            res = urlopen(url + root).read().decode('utf-8')
            articles = json.loads(res)

            filteredArticles.append(self.searchArticles(articles['articles']))

        print(len(filteredArticles))

    def searchArticles(self, articles):
        filteredArticles = []

        for article in articles:
            try:
                if self._query.lower() in article['description'].lower() or self._query.lower() \
                        in article['title'].lower():
                    filteredArticles.append(article)
            except AttributeError:
                # DO nothing lol
                print("Error happened")

        return filteredArticles
