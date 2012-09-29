from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^tweetwall/$', TemplateView.as_view(template_name="index.html")),
	url(r'^tweetwall/signin$', 'tweetwall.views.signin'),
	url(r'^tweetwall/oauth_callback$', 'tweetwall.views.oauth_callback'),
	url(r'^tweetwall/wall$', 'tweetwall.views.wall'),
)

if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns()
