# -*- coding: utf-8 *-*
from django.conf import settings
from django.core.urlresolvers import reverse
from twython import Twython


class Tweetwall(object):

	def __init__(self, request):
		self.request = request


	def get_authentication_url(self, request):
		self.twython = Twython(twitter_token=settings.CONSUMER_KEY,
            twitter_secret=settings.CONSUMER_SECRET,
            callback_url=self.request.build_absolute_uri(reverse('tweetwall.views.wall')))
		auth_tokens = self.twython.get_authentication_tokens()
		request.session['oauth_token'] = auth_tokens['oauth_token']
		request.session['oauth_token_secret'] = auth_tokens['oauth_token_secret']

		return self.twython.get_authentication_tokens()['auth_url']


	def handle_callback(self, request):
		self.twython = Twython(twitter_token=settings.CONSUMER_KEY,
            twitter_secret=settings.CONSUMER_SECRET,
            oauth_token=request.session['oauth_token'],
            oauth_token_secret=request.session['oauth_token_secret'])
		auth_tokens = self.twython.get_authorized_tokens()
		request.session['oauth_token'] = auth_tokens['oauth_token']
		request.session['oauth_token_secret'] = auth_tokens['oauth_token_secret']


	def save_tokens(self, tokens):
		self.request.session['oauth_token'] = tokens['oauth_token']
		self.request.session['oauth_token_secret'] = tokens['oauth_token_secret']


	def get_oauth_token(self):
		return self.request.session.get('oauth_token')


	def get_oauth_token_secret(self):
		return self.request.session.get('oauth_token_secret')


	def get_tweets(self, request):
		self.twython = Twython(twitter_token=settings.CONSUMER_KEY,
            twitter_secret=settings.CONSUMER_SECRET,
            oauth_token=request.session['oauth_token'],
            oauth_token_secret=request.session['oauth_token_secret'])
		return self.twython.getHomeTimeline()