import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

# api key
api_key = "Tea3Dqms54I277E9LNyOjxers"
# api secret key
api_secret_key = "OklGcTyWnBfjobU91LfXpc3LU0RkyGWiQaOMVU1AgO6q59b2R8"
# access token
access_token = "1054557010509713408-X3DJCCkzrQAiBU63YuKvl513DSn1ik"
# access token secret
access_token_secret = "kqx2llO7IYysVyeGX3BEOHwTsN8o2mUHiDjtc1CUIKiUE"

authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)

def get_related_tweets(text_query):
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 50
    try:
        # Pulling individual tweets from query
        for tweet in api.search(q=text_query, count=count):
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)
