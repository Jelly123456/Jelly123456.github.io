#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
RELATIVE_URLS = False

PATH = 'content'
STATIC_PATHS = ['images', 'extra']

PLUGIN_PATHS = ['plugins']
#PLUGINS = ['render_math']

OUTPUT_PATH = 'output/'
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git', 'README.md', 'CNAME']

THEME = 'Flex/'
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'

AUTHOR = 'YiLi'
#SITEURL = 'https://alexioannides.github.io'
SITEURL = 'https://jelly123456.github.io'
SITENAME = AUTHOR
SITETITLE = AUTHOR
SITESUBTITLE = 'A data scientist - A coder'
SITEDESCRIPION = 'YiLi on data science: data mining, statistics, machine learning, AI, functional programming, R, Python, Scala, Spark, Elasticsearch, AWS, DevOps...'

# to match old WordPress site
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TIMEZONE = 'Asia/Singapore'
DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 15
TYPOGRIFY = True

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'

MAIN_MENU = True
MENUITEMS = (('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
             ('Archives', '/archives.html'))

# Feeds
FEED_DOMAIN = SITEURL

CATEGORY_FEED_ATOM = 'feeds/category/{slug}/atom.xml'
TAG_FEED_ATOM = 'feeds/tag/{slug}/atom.xml'

CATEGORY_FEED_RSS = 'feeds/category/{slug}/rss.xml'
TAG_FEED_RSS = 'feeds/tag/{slug}/rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Markdown
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {'title': ''},
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Flex theme specific
#SITELOGO = '//avatars1.githubusercontent.com/u/5968486?s=460&v=4'
SITELOGO = '/images/Pic1.JPG'
#FAVICON = '/images/favicon.ico'
FAVICON = '/images/favicon.ico'
PYGMENTS_STYLE = 'monokai'
ROBOTS = 'index, follow'
DISABLE_URL_HASH = True

SOCIAL = (('github', 'https://github.com/Jelly123456'),
          ('linkedin', 'https://www.linkedin.com/in/han-yili-a3860659/'),
          ('leetcode', 'https://leetcode.com/HanYiLi/'),)

# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'))

# Flex theme integrations
DISQUS_SITENAME = 'YiLi Han'
GOOGLE_ANALYTICS= 'UA-125604661-1'