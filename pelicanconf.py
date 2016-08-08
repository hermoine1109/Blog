#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u' '
SITENAME = u'GNU Linux Users Group'
SITEURL = ''

PATH = 'content'
THEME = '/home/sudeshna/virtualenvs/pelican/html5-dopetrope'
TIMEZONE = 'Asia/Kolkata'
#BOOTSTRAP_THEME = 'lovers'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


#SITESUBTITLE ='Sub-title that goes underneath site name in jumbotron.'
#SITETAG = "Text that's displayed in the title on the home page."

# Extra stylesheets, for bootstrap overrides or additional styling.
#STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)

# Put taglist at end of articles, and use the default sharing button implementation.
#CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
#CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"



# Blogroll
LINKS = (('GLUG Website', 'http://nitdgplug.org'),
	('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('NIT Durgapur', 'http://nitdgp.ac.in/'),
         )

# Social widget
SOCIAL = (('Google+', 'http://plus.google.com/userid',
         'fa fa-google-plus-square fa-fw fa-lg'),
        ('Twitter', 'https://twitter.com/username',
         'fa fa-twitter-square fa-fw fa-lg'),
        ('LinkedIn', 'http://linkedin-url',
         'fa fa-linkedin-square fa-fw fa-lg'),
        ('BitBucket', 'http://bitbucket.org/username',
         'fa fa-bitbucket-square fa-fw fa-lg'),
        ('GitHub', 'http://github.com/username',
         'fa fa-github-square fa-fw fa-lg'),
        )

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
