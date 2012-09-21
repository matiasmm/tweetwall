from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'tweetwall.views.home', name='home'),

)
