'''

    twitterProcessing.py


'''

import twitter

api = twitter.Api(consumer_key='hpB0DLPH70h4vcxIWkDqZJrgL',
                  consumer_secret='DbCwerWtAp8kWJa5hQYzKTBvsvbNfzFPj4KqLI4HJAYUzOPKMq',
                  access_token_key='3346342624-EkcyYwi0Ve0al2FPUbcQ3LTS18eiBsXcAJwZf9X',
                  access_token_secret='DS4Xreai4gP8P6jfkFxMnAdnYSG2QhYA8XLjWPkFTmDqE')


'''
    checkCredentials() used to verify successful credentials
'''
def checkCredentials():
    print(api.VerifyCredentials())


'''
    getTweets() retrieves Tweets based on search query
'''
def getTweets(query):
    results = api.GetSearch(raw_query='q=' + query + '%20&result_type=recent&since=2014-07-19&count=100')
    return results

for tweet in getTweets('donald trump'):
    string = tweet.AsDict()
    if len(string['text']) > 0:
        print(string['text'])






