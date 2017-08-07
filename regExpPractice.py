import re

#编译
re_email = re.compile(r'(.+)@(\w+\.\w+)')
#使用
reTest = re_email.match('!df@gmail.com')
if reTest:
    print('success')
else:
    print('fail')

reEmail = re_email.match('someone@gmail.com')
if reEmail:
    print('success')
else:
    print('fail')


reEmail = re_email.match('bill.gates@gmail.com')

print(reEmail.groups())