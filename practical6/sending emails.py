# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:01:57 2019

@author: Yiwei
"""
import re
fhand = open('address_information.csv', 'r')
x = str() 
L1 = []
name_list = []
address_list = []
subject_list = []
for a in fhand:
    mylist = re.split(r',', str(a))
    if re.search(r'.*@.*', mylist[1]):
       if re.match(r'.*com.*', mylist[1]):
         print(mylist[1], ':Correct Address!')
         name_list += [mylist[0]]
         address_list += [mylist[1]]
         subject_list += [mylist[2]]
       else:
         print(mylist[1], ':Wrong Address!')

import smtplib
from email.mime.text import MIMEText
from email.header import Header
fhand1 = open('body.txt', 'r') 
inp = fhand1.read()
print('From: 3180111428@zju.edu.cn')
print('Password: ******')
for i in range(0, len(address_list)):    
    from_address = '3180111428@zju.edu.cn'
    to_address = address_list[i]
    body = re.sub(r'User', name_list[i], inp)
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['From'] = Header("3180111428", 'utf-8')
    msg['To'] =  Header(name_list[i], 'utf-8')
    msg['Subject'] = Header(subject_list[i], 'utf-8')    
    text = msg.as_string()
    try:
       server = smtplib.SMTP('smtp.zju.edu.cn',25)
       server.ehlo()
       server.starttls()
       server.login('3180111428','******')
       server.sendmail(from_address, to_address, text)
       print('Mail sent successfully!')
    finally:
       server.quit()

