'''

    twitterProcessing.py

    From a given search query, this module retrieves Tweets from the
    last 5 days and these will be used to be processed later on with
    Indico API.

'''

from datetime import datetime, timedelta
import sentiment
import twitter


api = twitter.Api(consumer_key='hpB0DLPH70h4vcxIWkDqZJrgL',
                  consumer_secret='DbCwerWtAp8kWJa5hQYzKTBvsvbNfzFPj4KqLI4HJAYUzOPKMq',
                  access_token_key='3346342624-EkcyYwi0Ve0al2FPUbcQ3LTS18eiBsXcAJwZf9X',
                  access_token_secret='DS4Xreai4gP8P6jfkFxMnAdnYSG2QhYA8XLjWPkFTmDqE')

class TwitterProcessing:

    def __init__(self, query):
        self._query = query


    '''
        checkCredentials() used to verify successful credentials
    '''
    def _checkCredentials(self):
        print(api.VerifyCredentials())


    '''
        getDates() returns a list of strings containing the last four dates
        in YYYY-MM-DD format
    '''
    def _getDates(self):
        dates = list()

        for i in range(4):
            date = datetime.now() - timedelta(days=i)
            dateFormatted = date.strftime('%Y-%m-%d')
            dates.append(dateFormatted)

        dates.reverse()

        return dates


    '''
        getTweetSentiment() returns a list of the sentiment score of the last four days
    '''
    def getTweetSentiment(self):
        sentiments = []
        dates = self._getDates()

        for date in dates:
            results = api.GetSearch(raw_query='q=' + self._query + '%20&result_type=recent&until=' + date + '&count=100')

            tweets = []

            for result in results:
                tweet = result.AsDict()
                tweets.append(tweet['text'])

            sentimentScore = float(sentiment.getAverageSentiment(tweets))

            sentiments.append(sentimentScore)

        return sentiments
