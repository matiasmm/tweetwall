tweetwall
===========

Django app to visualize multimedia content (videos, images, audio, etc) from your twitter stream 

Installation
============

   # Install requirements listed in requirements.txt with pip.
   # Rename tweetwall/settings/dev_template.py to dev.py.
   # set STATICFILES_DIRS and TEMPLATE_DIRS in dev.py
   # configure database with DATABASES in dev.py
   # Add your application in dev.twitter.com and copy CONSUMER_KEY and CONSUMER_SECRET in dev.py
   # python manage.py syncdb
   # python manage.psyncdb --settings tweetwall.settings.dev

