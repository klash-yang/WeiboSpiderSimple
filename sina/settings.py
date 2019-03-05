# -*- coding: utf-8 -*-

BOT_NAME = 'sina'

SPIDER_MODULES = ['sina.spiders']
NEWSPIDER_MODULE = 'sina.spiders'

ROBOTSTXT_OBEY = False

# 请将Cookie替换成你自己的Cookie
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie': '_T_WM=8656a19db3d6510d5d98d075c870772d; SUB=_2A25xaqaiDeRhGeBG7VQX8S7KzjuIHXVSlMrqrDV6PUJbkdAKLVjBkW1NRhYHFBLE3l266TH82D3DDJu_wCqbQf7c; SUHB=0D-VdYxkuDCT3W; SCF=AhFBbAX8QuC0xdS9sWh7h9fPHWOWHez53sGyP-uxEl6BQCYsroDgPNuVkKHY8amzYvbK0sEfzFFDUs7tf2pmP1Q.; SSOLoginState=1550767858'
}

# 当前是单账号，所以下面的 CONCURRENT_REQUESTS 和 DOWNLOAD_DELAY 请不要修改

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 3

DOWNLOADER_MIDDLEWARES = {
    'weibo.middlewares.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None
}

ITEM_PIPELINES = {
    'sina.pipelines.MongoDBPipeline': 300,
}

# MongoDb 配置
LOCAL_MONGO_HOST = '127.0.0.1'
LOCAL_MONGO_PORT = 27017
DB_NAME = 'Sina'

# WordPress Mysql 配置
WP_MYSQL_HOST = '132.232.113.103'
WP_MYSQL_USER = 'chouxiang'
WP_MYSQL_PWD = 'EYXHkjeKJD'
WP_MYSQL_DB = 'chouxiang'

# Scrap Info Mysql 配置
SCRAP_MYSQL_HOST = '132.232.113.103'
SCRAP_MYSQL_USER = 'scrapinfo'
SCRAP_MYSQL_PWD = 'KEBjhAPk2bZtaAG3'
SCRAP_MYSQL_DB = 'scrapinfo'

# Wordpress 配置
WORDPRESS_ADDRESS = 'https://www.onedaycp.com/'
WORDPRESS_ADMIN_NAME = 'poloyc'
WORDPRESS_ADMIN_PASSWORD = 'Suckerlove5'

# 最多爬多少天之前的微博
MAX_INTERVAL = 5

MAX_SCRAP_NUM = 20

MIN_LIKE = 5