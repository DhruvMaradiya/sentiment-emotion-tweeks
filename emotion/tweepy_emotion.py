from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy
import numpy as np
import pandas as pd

class Import_tweet_emotion:

	consumer_key="ojaz1t3F1Jah1e8bfV86NfAkn"
	consumer_secret="NtLdhFejfXfO3xaYEkbga16a7sSX0vG2kzEdJqeIOnx0Zct5vT"
	#AAAAAAAAAAAAAAAAAAAAAC0KYwEAAAAAjsV%2F9RPkCRFK2hRGHf5x2uY2Mt4%3DI2T7zN7MpHCjddmw98jNc0iMjoYsppNvAywv9trNiM30vZ6vzP

	access_token="857459502966243328-5J9ugicdJp4JEnKhajZSN81OB3PsExa"
	access_token_secret="Ul72M6Na1sLP3KTVKSOF7XSgbCQS8Sjpvn1V4P1MQf045"
     
	def tweet_to_data_frame(self, tweets):
		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
		return df

	def get_tweets(self, handle):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)

		account = handle
		item = auth_api.user_timeline(id=account,count=20)
		df = self.tweet_to_data_frame(item)

		all_tweets = []
		for j in range(20):
			all_tweets.append(df.loc[j]['Tweets'])
		return all_tweets

	def get_hashtag(self, hashtag):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)

		account = hashtag
		all_tweets = []

		for tweet in tweepy.Cursor(auth_api.search, q=account, lang='en').items(20):
			all_tweets.append(tweet.text)

		return all_tweets
