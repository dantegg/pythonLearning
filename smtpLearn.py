from email.mime.text import MIMEText

msg = MIMEText('Boom, 内容爆炸， 服务器不要为难我啊，这不是一个垃圾邮件啊，求你别拦着我了', 'plain', 'utf-8')

from_addr = input('From...')
password = input('Password')

to_addr = input('To...')

smtp_server = input('SMTP server:')

import smtplib

server = smtplib.SMTP(smtp_server, 25) #SMTP协议默认端口是25
server.set_debuglevel(1)
server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
