import sys
import time
import threading

import weibo, mealtime, bilibili, send

thread = []
weibo_monitor = threading.Thread(weibo.startmonitor())
thread.append(weibo_monitor)
b_monitor = threading.Thread(bilibili.startmonitor())
thread.append(b_monitor)
meal_remind = threading.Thread(mealtime.remind_start())
thread.append(meal_remind)


# 由于需要挂在github，所以需要设定好程序每次运行的周期，如果程序是在服务器运行，可以忽略该项
def cycle():
    count = 0
    times = 60 * 6
    while True:
        if count <= times:
            count += 1
        else:
            send.sendmsg('结束提醒', '机器人已循环一个周期')
            sys.exit()
        time.sleep(60)


thread.append(cycle())

for i in thread:
    i.setDaemon(True)
    i.start()
