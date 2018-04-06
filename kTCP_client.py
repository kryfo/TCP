# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:40:41 2016

@author: zhanghc
"""
import time
import socket

print '1.go'
time.sleep(0)

# 1.创建socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print '2.bulid'
time.sleep(0)

# 2.指定服务器的地址和端口号
s.connect(('127.0.0.1',998))
print '3.connect'
time.sleep(5)

krecv=s.recv(1024)
print ('4.'+krecv)
time.sleep(5)

for data in ['aaa','bbb','ccc']:
	# 向服务器请求数据
    s.send(data)
    print '5.sended'
    time.sleep(2)
    krecv=s.recv(1024)
    print ('6.'+krecv)
    time.sleep(2)

s.send('exit')
s.close()