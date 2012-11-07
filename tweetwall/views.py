# -*- coding: utf-8 *-*
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect, render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from twython import Twython


def index(request):
    return render_to_response('index.html', {'settings': settings},
        context_instance=RequestContext(request))


def signin(request):
	twython = Twython(twitter_token=settings.CONSUMER_KEY,
					twitter_secret=settings.CONSUMER_SECRET,
					callback_url=request.build_absolute_uri(reverse('tweetwall.views.oauth_callback')))
	auth_tokens = twython.get_authentication_tokens()
	request.session['oauth_token'] = auth_tokens['oauth_token']
	request.session['oauth_token_secret'] = auth_tokens['oauth_token_secret']
	return redirect(auth_tokens['auth_url'])


def oauth_callback(request):
	twython = Twython(twitter_token=settings.CONSUMER_KEY,
					twitter_secret=settings.CONSUMER_SECRET,
					oauth_token=request.session.get('oauth_token'),
					oauth_token_secret=request.session.get('oauth_token_secret'))
	twitter_tokens = twython.get_authorized_tokens()
	request.session['oauth_token'] = twitter_tokens['oauth_token']
	request.session['oauth_token_secret'] = twitter_tokens['oauth_token_secret']
	return redirect(reverse('tweetwall.views.wall'))


def wall(request):
	twython = Twython(twitter_token = settings.CONSUMER_KEY,
					twitter_secret = settings.CONSUMER_SECRET,
					oauth_token = request.session.get('oauth_token'),
					oauth_token_secret = request.session.get('oauth_token_secret'))
	return render_to_response('wall.html', {'tweets':twython.getHomeTimeline(),
		'settings': settings}, context_instance=RequestContext(request))
