import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import inscrawler.crawl as crawl
import inscrawler.utils.post_wordpress as post_wordpress


def job():
    crawl.scrap()
    post_wordpress.post()


job()
