from TwitterPost import TwitterPost
from tweepy.client import Client

def create_tweet(client: Client, twitter_post: TwitterPost):
    client.create_tweet(text=twitter_post.get_post_text())
