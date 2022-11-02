import tweepy, os
from dotenv import load_dotenv

load_dotenv()
consumer_key=os.getenv('API_KEY')
consumer_secret=os.getenv('API_KEY_SECRET')
access_token=os.getenv('ACCESS_TOKEN')
access_token_secret=os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

client=tweepy.Client(
    bearer_token=os.getenv('BEARER'),
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret, 
)


for tweet in api.search_tweets(q='O brasil vai virar venezuela',count='10'):
    try:
        print("usuario: @"+tweet.user.screen_name)
    except tweepy.TweepyError as e:
        print(e.reason)
    except StopIteration:
        break
