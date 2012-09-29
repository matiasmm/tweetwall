from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^/$', TemplateView.as_view(template_name="index.html")),
	url(r'^/signin$', 'tweetwall.views.signin'),
	url(r'^/oauth_callback$', 'tweetwall.views.oauth_callback'),
	url(r'^/wall$', 'tweetwall.views.wall'),
)

if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns()
