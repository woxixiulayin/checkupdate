#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
import sys
from config import *
# reload(sys)
# sys.setdefaultencoding( "utf-8" )

def send_mail(to_list, sub, content):
    me = u"git更新检查<zhigang7536308@163.com>"
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
    if len(sys.argv) != 2 :
        info = "need to input msg"
    else:
        info = sys.argv[1]
    # for post in Tieba_post_doc.objects():
        # info += post.title+'\n'
    if send_mail(mailto_list, "老大请看", info):
        print "send mail successfully"
    else:
        print "send mail fail"
