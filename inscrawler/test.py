import schedule


def job():
    print("YangCheng")


def run():
    schedule.every(1).second.do(job)
    while True:
        schedule.run_pending()


run()
