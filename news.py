import json
from urllib.request import urlopen


class News:
    def __init__(self, query):
        self._query = query

        self._filteredArticles = []

        url = 'http://newsapi.org/v1/articles?'
        with open('sources.json') as data_file:
            sources = json.load(data_file)

        for source in sources['sources']:
            root = 'source=' + source['id'] + '&apiKey=712e402419e84ccd87fd1e5958456192'
            res = urlopen(url + root).read().decode('utf-8')
            articles = json.loads(res)

            response = self.searchArticles(articles['articles'])

            if response != []:
                self._filteredArticles.extend(response)

    def getArticles(self):
        return self._filteredArticles

    def getDescriptions(self):
        res = []
        for article in self._filteredArticles:
            if len(article['description']) > 0:
                res.append(article['description'])

        return res

    def searchArticles(self, articles):
        filteredArticles = []

        for article in articles:
            try:
                if self._query.lower() in article['description'].lower() or self._query.lower() \
                        in article['title'].lower():
                    filteredArticles.append(article)
            except AttributeError:
                # DO nothing lol
                # print("Yeah boi")
                continue

        return filteredArticles
