import os
# from datetime import datetime
from dotenv import load_dotenv

load_dotenv()  # This loads variables from .env into os.environ

# CURRENT_YEAR = datetime.now().year

AUTHOR = 'Sarah Rogue'
SITENAME = 'Sarah\'s Website'

PATH = 'content'
OUTPUT_PATH = 'docs'

TIMEZONE = 'America/Indiana/Indianapolis'

DEFAULT_LANG = 'en-GB'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None  # default would write docs/feeds/all-{lang}.atom.xml

# DEFAULT_PAGINATION = 1

ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
DEFAULT_CATEGORY = 'other'
DISPLAY_TAGS_ON_MENU = True
EXTRA_PATH_METADATA = {
    'pages/about.adoc': {'url': 'about.html', 'save_as': 'about.html'},
    'pages/index.adoc': {'url': 'index.html', 'save_as': 'index.html'},
    'images/favicons/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'images/favicons/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'images/favicons/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'images/favicons/favicon.ico': {'path': 'favicon.ico'},
    'images/favicons/favicon.svg': {'path': 'favicon.svg'},
    'images/favicons/manifest.json': {'path': 'manifest.json'},
}
# the blog listing uses the theme's articles.html (instead of index.html)
# and is saved as /blog/index.html, leaving /index.html to pages/index.adoc
DIRECT_TEMPLATES = ['articles', 'tags', 'categories', 'authors']
PAGINATED_TEMPLATES = {'articles': None, 'tag': None, 'category': None, 'author': None}
ARTICLES_URL = 'blog/'
ARTICLES_SAVE_AS = 'blog/index.html'
FONT_AWESOME = os.getenv('FONT_AWESOME')
# HOSTING_PROVIDER = 'Cloudflare'
# HOSTING_PROVIDER_URL = 'https://www.cloudflare.com/'
# LICENSE = 'Attribution-NonCommercial-NoDerivatives 4.0 International'
# LICENSE_URL = 'https://creativecommons.org/licenses/by-nc-nd/4.0/'
OVERRIDE_CSS = 'styles.css'
PLUGIN_PATHS = ['plugins']
PLUGINS = ['asciidoc_reader', 'sitemap']
STATIC_PATHS = ['images', 'src', 'robots.txt', 'css']
# SUMMARY_MAX_PARAGRAPHS = 1
THEME = 'themes/will_i_am'
TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')
USE_FOLDER_AS_CATEGORY = False

# for sitemap plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'never',
    }
}
