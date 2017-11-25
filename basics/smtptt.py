#!/usr/bin/env python3
#coding=utf-8

#smtp发送邮件

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = '18814288784@163.com' #input('From: ') 邮件发送者
password = '123456a' #input('Password: ') 授权码
to_addr = '295287765@qq.com' #input('')  邮件接收者
smtp_server = 'smtp.163.com'        #input('') smtp邮件发送服务器

msg = MIMEText('Hello,smtp by python','plain','utf-8')
msg['From'] = _format_addr('python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自smtp的问候。。。','utf-8').encode()

server = smtplib.SMTP(smtp_server,25)
#加密smtp，创建安全连接
server.starttls()
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
print('send seccess!')