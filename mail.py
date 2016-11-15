#!/usr/bin/python
# -*- coding: utf8 -*-

import smtplib
import time
from email.mime.text import MIMEText
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from random import shuffle

MAILS_PATH = 'mails.csv'
BODY_MSG = 'Hello %s, \n Your secret target is %s %s'
FROM = 'xjouppe@smartadserver.com'
TITLE = 'Secret Santa !'
PSWD = 'prune&K6'

def parse():
    fp = open(MAILS_PATH, 'rb')
    data = fp.read().split('\n')
    fp.close()

    print([d for d in data if len(d.split(',')) != 3])
    send_all(data)

def send_all(data):
    data = [[d.strip() for d in value.split(',')] for value in data if len(value.split(',')) == 3]
    shuffle(data)
    for pos, value in enumerate(data):
        curr = value
        next = data[0] if pos+1>=len(data) else data[pos+1]
        msg = BODY_MSG % (curr[1], next[1], next[0])
        to_mail = curr[2]
        print(curr[1], next[1])
        #send(msg,TITLE, PSWD, FROM, to_mail)

def send(body_msg, title_msg, passwd, from_mail, to_mail):
    time.sleep(1)
    print(to_mail)
    msg = MIMEMultipart()
    msg['From'] = 'santa@smartadserver.com'
    msg['To'] = to_mail
    msg['Subject'] = title_msg
    msg.add_header('From', 'santa@smartadserver.com')

    msg.attach(MIMEText(body_msg))

    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(from_mail, passwd)
    mailserver.sendmail(msg['From'], [msg['To']], msg.as_string())
    mailserver.quit()

if __name__ == '__main__':
    parse()
