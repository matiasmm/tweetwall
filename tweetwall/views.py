# -*- coding: utf-8 *-*
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect, render_to_response
from tweetwall import Tweetwall


def signin(request):
	tweetwall = Tweetwall(settings.OAUTH_CALLBACK, settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
	request.session['oauth_token'] = tweetwall.get_authentication_token()
	request.session['oauth_token_secret'] = tweetwall.get_authentication_token_secret()
	return redirect(tweetwall.get_authenticate_url())


def oauth_callback(request):
	tweetwall = Tweetwall(settings.OAUTH_CALLBACK, settings.CONSUMER_KEY, settings.CONSUMER_SECRET,
						request.session.get('oauth_token'), request.session.get('oauth_token_secret'))
	request.session['oauth_token'] = tweetwall.get_authorized_token()
	request.session['oauth_token_secret'] = tweetwall.get_authorized_token_secret()
	return redirect('/tweetwall/wall')


def wall(request):
	tweetwall = Tweetwall(settings.OAUTH_CALLBACK, settings.CONSUMER_KEY, settings.CONSUMER_SECRET,
						request.session.get('oauth_token'), request.session.get('oauth_token_secret'))
	return render_to_response('wall.html', {'tweets':tweetwall.get_tweets()})