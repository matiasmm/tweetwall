# -*- coding: utf-8 *-*
from twython import Twython

class Tweetwall(object):

	def __init__(self, oauth_callback, consumer_key, consumer_secret,
				 oauth_token=None, oauth_token_secret=None):
		self.twython = Twython(app_key=consumer_key,
            app_secret=consumer_secret,
            oauth_token=oauth_token,
            oauth_token_secret=oauth_token_secret,
            callback_url=oauth_callback)


	def get_authenticate_url(self):
		return self.twython.get_authentication_tokens()['auth_url']


	def get_authentication_token(self):
		return self.twython.get_authentication_tokens()['oauth_token']

	def get_authentication_token_secret(self):
		return self.twython.get_authentication_tokens()['oauth_token_secret']

	def get_authorized_token(self):
		return self.twython.get_authorized_tokens()['oauth_token']

	def get_authorized_token_secret(self):
		return self.twython.get_authorized_tokens()['oauth_token_secret']

	def get_tweets(self):
		return self.twython.getHomeTimeline()