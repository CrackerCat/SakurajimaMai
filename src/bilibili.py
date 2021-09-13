import requests
import send
from config import bIds
import time
api = {
    'userinfo': 'http://api.bilibili.com/x/space/acc/info',
    'videos_info': 'https://api.bilibili.com/x/space/arc/search?mid=5970160',
    'video_play': 'https://www.bilibili.com/video/',
}

starttime = time.mktime(time.localtime())


def bilibili_monitor(upid):
    params = {
        'mid': upid
    }
    response = requests.get(api['videos_info'], params=params)
    videos = response.json()['data']['list']['vlist']
    for i in videos:
        if i['created'] >= starttime:
            ding_talk(i, upid)
        else:
            break


def ding_talk(video,upid):
    params = {
        'mid': upid
    }
    bv = video['bvid']
    video_title = video['title']
    pic = f"![pic]({video['pic']})"
    name = requests.get(api['userinfo'], params=params).json()['data']['name']
    play = api['video_play'] + bv
    title = f"{name} 发布了新的视频"
    msg = f"### <{name}> 发布了新的视频 {video_title}\n" \
          f"\n" \
          f"{pic}\n" \
          f"\n" \
          f"播放地址：{play}"
    send.sendmsg(title=title, msg=msg)


def startmonitor():
    if len(bIds) == 0:
        print('没有关注的up主，b站监控退出')
        return
    while True:
        for id in bIds:
            try:
                bilibili_monitor(id)
            except:
                continue
        time.sleep(3600)