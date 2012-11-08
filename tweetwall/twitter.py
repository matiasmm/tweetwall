# -*- coding: utf-8 *-*
from twython import Twython
from django.conf import settings

'''
The Twitter class manages authentication

'''
class Twitter():

    def __init__(self, oauth_token=None, oauth_token_secret=None, callback_url=None):

        self.twython = Twython(twitter_token=settings.CONSUMER_KEY,       twitter_secret=settings.CONSUMER_SECRET, oauth_token=oauth_token,oauth_token_secret=oauth_token_secret, callback_url=callback_url)

    def get_authentication_tokens(self):
        return self.twython.get_authentication_tokens()

    def get_authorized_tokens(self):
        return self.twython.get_authorized_tokens()

    def get_home_timeline(self):
        return self.twython.request('statuses/home_timeline', params={'include_entities' : '1'})