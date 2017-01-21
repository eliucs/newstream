from news import News
import sentiment

query = input('Query: ')

news = News(query)
articles = news.getArticles()
descriptions = news.getDescriptions()

sentiments = list()
result = list()
max = 0
min = 1

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
    result.append(article)

spread = max - min
print(spread)

print(result)

sumSentiments = sum(sentiments)
averageSentiment = sumSentiments / len(sentiments)
sentimentValue = sentiment.getSentimentText(averageSentiment)

print(averageSentiment)
print(sentimentValue)






