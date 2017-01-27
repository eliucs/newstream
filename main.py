'''

    Newstream

    PennApps XV: Aggregating news and Tweets and applying
    sentiment analysis on various topics.

    Authors: Eric Liu (https://github.com/eliucs)
             Jason Pham (https://github.com/suchAHassle)

'''


from flask import Flask, render_template, request
import pyrebase
from graph import Graph
from news import News
import sentiment
from twitterProcessing import TwitterProcessing


app = Flask(__name__)

cache = dict()

# Initialize Firebase for caching search results
config = {
  "apiKey": "AIzaSyBvz2GVPQJBnQjblZneyffJeLIAusKkUOE",
  "authDomain": "newstream-166cf.firebaseapp.com",
  "databaseURL": "https://newstream-166cf.firebaseio.com",
  "storageBucket": "newstream-166cf.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
}

firebase = pyrebase.initialize_app(config)

# Get a reference to the database service
db = firebase.database()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', text='Try searching for something.')


@app.route('/search', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':

        query = request.form['search']

        cache = db.child('data').get()

        if query not in cache.val():

            news = News(query)
            articles = news.getArticles()

            sentiments = list()
            result = ''
            max = 0
            min = 1

            if len(articles) <= 0:
                return render_template('index.html', text='No results.')

            for article in articles:
                description = article['description']

                if len(description) <= 0:
                    continue

                sentimentValue = sentiment.getSentiment(str(article['description']))
                sentiments.append(sentimentValue)

                if sentimentValue > max:
                    max = sentimentValue

                if sentimentValue < min:
                    min = sentimentValue

                article['sentimentValue'] = article.get('sentimentValue', '') + sentiment.getSentimentText(sentimentValue)

                result += '<div class="article-container">' \
                          '<div class="article-element">' \
                          '<img class="image" src="' + str(article['urlToImage']) + '' \
                          '" alt="' + str(article['title']) + '"></div>' \
                          '<div class="article-element"><div class="article-title"><a href="' + str(article['url']) + ''\
                          '">' + str(article['title']) + '</a></div><div class="article-description">' + str(article['description']) + ''\
                          '</div><div class="article-link"><a href="' + str(article['url']) + '">Read More &rarr;</a></div>' \
                          '</div><div class="article-element"><div class="article-sentiment-title">Consensus</div>' \
                          '<div class="article-sentiment" style="color:' + str(sentiment.getSentimentColor(sentimentValue)) + ''\
                          ';">' + str(sentiment.getSentimentText(sentimentValue)) + '</div></div></div>'

            spread = max - min
            sumSentiments = sum(sentiments)
            averageSentiment = sumSentiments / len(sentiments)
            sentimentValue = sentiment.getSentimentText(averageSentiment)
            color = sentiment.getSentimentColor(averageSentiment)


            tweets = TwitterProcessing(query)
            sentimentsLastFiveDays = tweets.getTweetSentiment()
            sentimentsLastFiveDays.append(float('{0:.6f}'.format(averageSentiment)))

            graph = Graph(sentimentsLastFiveDays)
            graph.getGraph()

            newCache = {'queryHeader': query,
                        'sentimentScore': averageSentiment,
                        'sentimentValue': sentimentValue,
                        'spread': spread,
                        'color': color,
                        'result': result}

            db.child('data').update({query: newCache})

            return render_template('search.html',
                                   queryHeader=query,
                                   sentimentScore='{0:.6f}'.format(averageSentiment),
                                   sentimentValue=sentimentValue,
                                   spread='{0:.6f}'.format(spread),
                                   color=color,
                                   result=result)
        else:
            oldCache = cache.val()
            info = oldCache[query]

            tweets = TwitterProcessing(query)
            sentimentsLastFiveDays = tweets.getTweetSentiment()
            sentimentsLastFiveDays.append('{0:.6f}'.format(info['sentimentScore']))

            graph = Graph(sentimentsLastFiveDays)
            graph.getGraph()

            return render_template('search.html',
                                   queryHeader=info['queryHeader'],
                                   sentimentScore='{0:.6f}'.format(info['sentimentScore']),
                                   sentimentValue=info['sentimentValue'],
                                   spread='{0:.6f}'.format(info['spread']),
                                   color=info['color'],
                                   result=info['result'])

    else:
        return render_template('index.html', text='Try searching for something.')


if __name__ == "__main__":
    app.run(debug=True)