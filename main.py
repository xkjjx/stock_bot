import os

from tweepy.client import Client
from dotenv import load_dotenv
from TwitterBot import create_tweet
from StockPricePost import StockPricePost
from datetime import datetime

if __name__ == '__main__':
    load_dotenv()
    consumer_key = os.getenv("X_API_KEY")
    consumer_secret = os.getenv("X_API_KEY_SECRET")
    access_token = os.getenv("X_ACCESS_TOKEN")
    access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

    client = Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )

    twitter_post = StockPricePost("AAPL", 250, datetime.now())

    print("Now posting tweet with text:", twitter_post.get_post_text(), sep="\n")

    # create_tweet(client, twitter_post)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
