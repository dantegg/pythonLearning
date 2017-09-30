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
    itchat.send("哈哈哈，我又来啦~~~，起床啦起床啦！", toUserName=userName)
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
                count = count + 1
                return u'嘻嘻嘻，亲爱的，早上好哟！'
            if count == 1:
                count = count + 1
                return u'希望这次不要失败了'
            if count == 2:
                count = count + 1
                return u'是不是surprise？（←—___←——— ||| 看来失败了）'
            if count == 3:
                count = count + 1
                return u'就是想大洋彼岸的你早晨醒来时能看到我的问好'
            if count == 4:
                count = count + 1
                return u'这样看其实我也成功啦！！！撒花！！！'
            if count == 5:
                count = count + 1
                return u'好啦，好啦，今天我也要放假了呢！就看你玩的那么爽！！！'
            if count == 6:
                count = count + 1
                return u'但是要多发图知不知道！小猫小狗小花小草草泥马都可以，当然最终要的是有小仙女（单压X1）'
            if count == 7:
                count = count + 1
                return u'楠楠爱你哟， 玩的开心~~~'
            if count >7 and count != 10 and count != 11 and count != 12:
                count = count + 1
                return u'嘻嘻嘻'
            if count == 10:
                count = count + 1
                return u'你好无聊啊，后面都是嘻嘻嘻，别试啦'
            if count == 11:
                count = count + 1
                return u'骗你的啦~~~'
            if count == 12:
                count = count + 1
                return u'恭喜您已达成成就：无聊の人！'
            # count = count + 1
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
   

        