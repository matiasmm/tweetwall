# -*- coding: utf-8 *-*
from twython import Twython

class OAuth(object):

	def __init__(self, oauth_callback, consumer_key, consumer_secret):
		self.twython = Twython(app_key=consumer_key,
            app_secret=consumer_secret,
            callback_url=oauth_callback)


	def get_authenticate_url(self):
		return self.twython.get_authentication_tokens()['auth_url']



