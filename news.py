'''

    news.py

    Retrieves news articles using the News API.

'''


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

    '''
        getArticle() returns a list of articles (filtered if their length
        is 0)
    '''
    def getArticles(self):
        return self._filteredArticles


    '''
        getDescriptions() returns only the descriptions from the
        articles
    '''
    def getDescriptions(self):
        result = []
        for article in self._filteredArticles:
            if len(article['description']) > 0:
                result.append(article['description'])

        return result


    '''
        searchArticles(articles) returns the filtered articles by whether the
        search query exists in the title or description of the article
    '''
    def searchArticles(self, articles):
        filteredArticles = []

        for article in articles:
            try:
                if self._query.lower() in article['description'].lower() or self._query.lower() \
                        in article['title'].lower():
                    filteredArticles.append(article)
            except AttributeError:
                continue

        return filteredArticles
