ps -aux|grep shedule_run | grep -v grep | cut -c 9-15 | xargs kill -9



ps -aux|grep python


pkill -9 shedule_run


sudo kill -9 $(pidof shedule_run)