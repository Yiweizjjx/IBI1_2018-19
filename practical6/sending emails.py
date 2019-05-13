# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:01:57 2019

@author: Yiwei
"""
import re
#open the file
fhand = open('address_information.csv', 'r')
name_list = []
address_list = []
subject_list = []
#test the address
for a in fhand:
    mylist = re.split(r',', str(a))
    if re.search(r'.*@.*', mylist[1]):
       if re.match(r'^[0-9A-Za-z_]+@[0-9A-Za-z_]+(\.[0-9A-Za-z_]+)+$', mylist[1]):
         print(mylist[1], ':Correct Address!')
         name_list += [mylist[0]]
         address_list += [mylist[1]]
         subject_list += [mylist[2]]
       else:
         print(mylist[1], ':Wrong Address!')
#send the email
import smtplib
from email.mime.text import MIMEText
from email.header import Header
#read the file into a single string
fhand1 = open('body.txt', 'r') 
inp = fhand1.read()
from_address=input('From:')
loginname=from_address.split('@')[0] #get the login name
password=input('Password:') #get the password
for i in range(0, len(address_list)):    
    to_address = address_list[i]
    body = re.sub(r'User', name_list[i], inp) # change salutation for different users
    msg = MIMEText(body, 'plain', 'utf-8')
    to_name=Header(name_list[i],'utf-8') #set Header to correct properties
    to_name.append(to_address,'ascii')
    msg['From'] = Header('Yiwei', 'utf-8')
    msg['To'] =  to_name
    msg['Subject'] = Header(subject_list[i], 'utf-8')    
    try:
       server = smtplib.SMTP('smtp.zju.edu.cn',25)
       server.login(loginname,password)
       server.sendmail(from_address, [to_address], msg.as_string())
       server.quit()
       print('Mail sent successfully!')
    except smtplib.SMTPEception:
       print('Mail delevery failed!')

