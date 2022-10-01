import tweepy

from . import models


# Read the values
api_key = "**********"
api_key_secret = "**********"
access_token = "**********"
access_token_secret = "**********"


auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)




def get_tweets_by_user_name(username):
    limit=3000
    tweets = tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode='extended').items(limit)
    for tweet in tweets:
        tweet_model=models.Tweet_user(username=tweet.user.screen_name,user_id=tweet.user.id,date=tweet.created_at,text=tweet.full_text)
        tweet_model.save()

def autofollow(username):
    api.create_friendship(username)

def get_tweets_hashtag(hashtag):
    limit=3000
    tweets = tweepy.Cursor(api.search_tweets,q=hashtag, tweet_mode='extended').items(limit)
    for tweet in tweets:
        tweet_model=models.Tweet_hashtag(hashtag=hashtag,username=tweet.user.screen_name,user_id=tweet.user.id,date=tweet.created_at,text=tweet.full_text)
        tweet_model.save()

def create_tweet(tweet_text,image_path="-"):
    if image_path=="-":
        api.update_status(tweet_text)
    else:
        api.update_status_with_media(tweet_text,image_path)


def retweet(id):
    api.retweet(id)
