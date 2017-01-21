#
#
#   sentiment.py
#   -------------
#   Makes a request to Indico's Text Analysis API and
#   returns the sentiment of a particular text or
#   list of texts
#
#


import indicoio as indico


indico.config.api_key = '5318bb1846008c9c7f9bbd51256861fb'


#   getSentiment(str) consumes a string and uses the Indico API to
#   return its sentiment value as a float value
def getSentiment(str):
    return indico.sentiment(str)


#   printSentiment(str) consumes a string and prints the result
#   of getSentiment(str) to the console
def printSentiment(str):
    print(getSentiment(str))


#   getBatchSentiment(lst) consumes a list of strings and uses
#   the Indico API to return a list of sentiment values as a list of
#   float values
def getBatchSentiment(lst):
    return indico.sentiment(lst)


#   printBatchSentiment(lst) consumes a list of strings and prints the
#   result of getBatchSentiment(lst) to the console
def printBatchSentiment(lst):
    print(getBatchSentiment(lst))


#   getAverageSentiment(lst) consumes a list of strings and returns the
#   average sentiment value as a float value
def getAverageSentiment(lst):
    sentimentList = getBatchSentiment(lst)
    sum = 0

    for item in sentimentList:
        sum += item

    return '{0:.6f}'.format(sum / len(sentimentList))


#   printAverageSentiment(lst) consumes list of strings and prints the
#   result of getAverageSentiment(lst) to the console
def printAverageSentiment(lst):
    print(getAverageSentiment(lst))


#   getSentimentText(score) consumes a sentiment score as a float value
#   and returns its associated text label
def getSentimentText(score):
    if score <= 0.1:
        return "Overwhelmingly Negative"
    elif score <= 0.2:
        return "Extremely Negative"
    elif score <= 0.3:
        return "Very Negative"
    elif score <= 0.4:
        return "Generally Negative"
    elif score <= 0.5:
        return "Moderately Negative"
    elif score <= 0.6:
        return "Moderately Positive"
    elif score <= 0.7:
        return "Generally Positive"
    elif score <= 0.8:
        return "Very Positive"
    elif score <= 0.9:
        return "Extremely Positive"
    else:
        return "Overwhelmingly Positive"