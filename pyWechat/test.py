import itchat
import time
import sched
import threading
count = 0

schedule = sched.scheduler(time.time, time.sleep)

def sendOneWechatMessage():
    itchat.send("Hello World Again!", 'filehelper')

def clockFunc():
    account=itchat.search_friends('杨雨婷')
    userName = account[0]['UserName']
    morningTime = 3600 * 3 - 900
    time.sleep(morningTime)
    print('haha')
    itchat.send("么么哒~~~", toUserName=userName)
    print(account)
    #_time = 1 * 30
    #schedule.enter(_time, 0, sendOneWechatMessage)

@itchat.msg_register('Text')
def text_reply(msg):
    if not msg['FromUserName'] == myUserName:
        print (msg['FromUserName'], '======================', msg['User']['RemarkName'])
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),msg['User']['NickName'],msg['Text']), 'filehelper')
        if msg['User']['RemarkName'] == u'杨雨婷':
            global count
            print('yes', count)
            if count == 0:
                return u'嘻嘻嘻，亲爱的（请用文字回复我哟~~~）'
            if count == 1:
                return u'早上好呀，（这是一个小游戏呢）'
            if count == 2:
                return u'是不是surprise？'
            if count == 3:
                return u'略略略，我才没有起床呢！！！'
            if count == 4:
                return u'但是我照样能回你微信呀'
            if count == 5:
                return u'好了，估计你应该看穿了，这是自动回复'
            if count == 6:
                return u'因为我还在睡觉啦，不能及时回你微信，所以就写了个小玩意'
            if count == 7:
                return u'楠楠爱你哟， 玩的开心~~~'
            if count >7 and count != 10 and count != 11 and count != 12:
                return u'嘻嘻嘻'
            if count == 10:
                return u'你好无聊啊，后面都是嘻嘻嘻，别试啦'
            if count == 11:
                return u'骗你的啦~~~'
            if count == 12:
                return u'恭喜您已达成成就：无聊之人！'
            count = count + 1
        # return u'嘻嘻嘻'

if __name__ == '__main__':
    itchat.auto_login()
    # itchat.send("Hello World Again 233 enter!", 'filehelper')
    myUserName = itchat.get_friends(update=True)[0]["UserName"]    
    t1 = threading.Thread(target=itchat.run)
    t2 = threading.Thread(target=clockFunc)
    t2.start()
    t2.join()
    t1.start()
    t1.join()
   

        