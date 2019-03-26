import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import schedule
import inscrawler.crawl as crawl
import inscrawler.utils.post_wordpress as post_wordpress


def job():
    crawl.scrap()
    post_wordpress.post()


def run():
    # schedule.every(10).minutes.do(job)
    # schedule.every().hour.do(job)
    job()
    schedule.every(1).day.at("10:30").do(job)
    # schedule.every(5).to(10).days.do(job)
    # schedule.every().monday.do(job)
    # schedule.every().wednesday.at("13:15").do(job)
    while True:
        schedule.run_pending()


run()
