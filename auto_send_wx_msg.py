from threading import Timer
from wxpy import *
import requests

# bot = Bot()
bot = Bot(console_qr=2, cache_path="botoo.pkl")

def get_news():
    print('in get_news()')
    url = 'http://open.iciba.com/dsapi/'
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note

def send_news():
    try:
        contents = get_news()
        print('contents is ', contents)
        # my_friend = bot.friends().search(u'安迪_Tu')[0]
        # my_friend = bot.file_helper
        my_friend.send(contents[0])
        my_friend.send(contents[1])
        my_friend.send('Have a good day!')
    except:
        # my_friend = bot.friends().search(u'安迪_Tu')[0]
        my_friend = bot.self
        my_friend.send('今天消息发送失败了')

if __name__=='__main__':
    send_news()
    # myself = bot.self
    # bot.file_helper.send('Hello from wxpy!')
















# import itchat
# import json
# # from apscheduler.schedulers.blocking import BlockingScheduler
#
# def auto_send(msg, toUser):
#     itchat.send(msg=msg, toUserName=toUser)
#
# if __name__ == "__main__":
#     # itchat.login()
#     itchat.auto_login(hotReload=True)
#     #获取好友列表
#     friends = itchat.get_friends()
#     #转换为字典
#     friendsStr = json.dumps(friends)
#     print(friendsStr)
#     #发送消息
#     # itchat.send(msg="你好", toUserName="8a30fa2addcac31cfe916506d80b2254")
#
#     try:
#         for item in friends:
#             if(item["NickName"] == "安迪_Tu"):
#                 toUser = item["UserName"]
#             # scheduler = BlockingScheduler()
#             # scheduler.add_job(auto_send, "cron", day_of_week="0-6", hour=15, minute=17, args=["你好", toUser])
#             # scheduler.start()
#             auto_send('你好，我是机器人', toUser)
#             itchat.run()
#     except Exception as ex:
#         print('get exception')
#         itchat.logout()
#         print(ex)