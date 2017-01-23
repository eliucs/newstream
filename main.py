from flask import Flask, render_template, request
from news import News
import sentiment

app = Flask(__name__)

cache = dict()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', text='Try searching for something.')


@app.route('/search', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':

        query = request.form['search']

        if query not in cache:

            news = News(query)
            articles = news.getArticles()
            descriptions = news.getDescriptions()

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

            newCache = {'queryHeader': query,
                        'sentimentScore': averageSentiment,
                        'sentimentValue': sentimentValue,
                        'spread': spread,
                        'color': color,
                        'result': result}

            cache[query] = newCache

            return render_template('search.html',
                                   queryHeader=query,
                                   sentimentScore='{0:.6f}'.format(averageSentiment),
                                   sentimentValue=sentimentValue,
                                   spread='{0:.6f}'.format(spread),
                                   color=color,
                                   result=result)
        else:
            return render_template('search.html',
                                   queryHeader=cache[query]['queryHeader'],
                                   sentimentScore='{0:.6f}'.format(cache[query]['sentimentScore']),
                                   sentimentValue=cache[query]['sentimentValue'],
                                   spread='{0:.6f}'.format(cache[query]['spread']),
                                   color=cache[query]['color'],
                                   result=cache[query]['result'])

    else:
        return render_template('index.html', text='Try searching for something.')


if __name__ == "__main__":
    app.run(debug=True)