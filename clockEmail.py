from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib
import sched
import time

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# from_addr = input('From...')
# password = input('Password...')
# to_addr = input('To...')
# smtp_server = input('SMTP server...')

# msg = MIMEText('哈哈哈，终于发送成功了！傻叉网易！', 'plain', 'utf-8')
# msg['From'] = _format_addr('无风险自测<%s>' % from_addr)
# msg['To'] = _format_addr('章儒楠-高级运营组<%s>' % to_addr)
# msg['Subject'] = Header('【beta】2017.9.5Interception', 'utf-8').encode()

fromAddress = '635366043@qq.com'
passWord = 'zhang2jingchu02'
toAddress = 'han.zhang03@ele.me'
smtpServer = 'smtp.qq.com'

msg = MIMEText('哈哈哈，涵哥哥～～～～', 'plain', 'utf-8')
msg['From'] = _format_addr('啦啦啦<%s>' % fromAddress)
msg['To'] = _format_addr('张涵-高级运营组<%s>' % toAddress)
msg['Subject'] = Header('哟哟哟，不要害怕～～～', 'utf-8').encode()

def sendEmail():
    server = smtplib.SMTP(smtpServer, 25)
    server.set_debuglevel(1)
    server.starttls()
    server.login(fromAddress, passWord)
    server.sendmail(fromAddress, [toAddress], msg.as_string())
    server.quit()

schedule = sched.scheduler(time.time, time.sleep)

def eachHourSchedule():
    oneHour = 3600
    for i in range(0, 24):
        schedule.enter(i * oneHour, 0, sendEmail)
    schedule.run()

if __name__ == '__main__':
    eachHourSchedule()