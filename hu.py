import tweepy
import random

# API情報
BEARER_TOKEN = 'XXXXX'
ACCESS_TOKEN = 'XXXXX'
ACCESS_TOKEN_SECRET = 'XXXXXX'

CONSUMER_KEY = 'XXXXX'
CONSUMER_SECRET = 'XXXXX'

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
