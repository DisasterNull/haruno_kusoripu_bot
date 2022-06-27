import tweepy
import random

# API情報
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAMNocgEAAAAAbAdSdESlBJmaOCsTwOcCENfy7V4' \
               '%3DgsFXqmox7uptr2ehETo6BD55eLkvxBofvp30T3BLLr8ryoQ5AI'
ACCESS_TOKEN = '1505388214563241985-HdSobVQevOEQwnBqyziiZeKLkB0Ab2'
ACCESS_TOKEN_SECRET = 'd52tWfw02DkvMsTdytBMhxaMMFQuk4bTCNknDfryFbDBF'

CONSUMER_KEY = '6RtDnTRUUnuOKVUowCm7HTZLr'
CONSUMER_SECRET = 'b0O6rI513WK2BEiG6u3mK7tCA8FC2yUFHqIiZsqNqGxF2JvQWe'

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
# リプライツイート

Account = 'Hrno_'

# user_timelineで指定したユーザーのタイムラインのTweetを取得(最大20個まで)
tweets = api.user_timeline(screen_name=Account, count=20, page=1)

for tweet in tweets:
    print("="*80)
    print('ツイートID：', tweet.id)
    print('ツイート本文：', tweet.text)
