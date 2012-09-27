# -*- coding: utf-8 *-*
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect
from auth import OAuth


def signin(request):
	oauth = OAuth(settings.OAUTH_CALLBACK, settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
	return redirect(oauth.get_authenticate_url())

def oauth_callback(request):

	return HttpResponse("<body>Exito!</body>")