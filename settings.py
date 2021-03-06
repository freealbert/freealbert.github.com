# -*- coding: utf-8 -*-

# Basic settings
Author = 'freealbert'
DEFAULT_CATEGORY = 'Tech'
OUTPUT_PATH = '.'
PATH ='./posts'
SUMMARY_MAX_LENGTH = 0
# Theming
THEME = 'pXq-simple'
# DISPLAY_PAGES_ON_MENU = False
SITENAME = "freealbert's blog"
SITEURL = "http://freealbert.github.com"
TIMEZONE = "Asia/Shanghai"

GITHUB_URL = "https://github.com/freealbert/"
# DISQUS_SITENAME = "freealbert.github.com"
GOOGLE_ANALYTICS = "UA-34015459-1"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_PAGINATION = 5#默认每页文章数

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS = (('D&L','http://dspandlinux.com/'),
          ('pxq','http://panxiuqing.github.com/'),)
SOCIAL = (('sina','http://www.weibo.com/u/1844630250?wvr=3.6&lf=reg'),)

# global metadata to all the contents
DEFAULT_METADATA = (('yeah','it is'),)

# static paths will be copied under the same name
STATIC_PATHS = ["pictures",]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/robots.txt','robots.txt'),)

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"
