from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From...')
password = input('Password...')
to_addr = input('To...')
smtp_server = input('SMTP server...')

msg = MIMEText('哈哈哈，终于发送成功了！傻叉网易！', 'plain', 'utf-8')
msg['From'] = _format_addr('无风险自测<%s>' % from_addr)
msg['To'] = _format_addr('章儒楠-高级运营组<%s>' % to_addr)
msg['Subject'] = Header('【beta】2017.9.5Interception', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()