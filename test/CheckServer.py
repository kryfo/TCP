# -*- coding: utf-8 -*-
import socket
import threading
import time
import struct
import json

#建立服务器
checkIP=('127.0.0.1',999)
ksocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ksocket.bind(checkIP)
ksocket.listen(5)
print 'wait...'


#设置反馈数据
number = 0
def dataHandle(headPack, body):
    global number
    number += 1
    print (u"第%s个数据包" % number)
    #print (u"ver:%s, bodySize:%s, cmd:%s" % headPack)
    print (body.decode())
    
#接收内容
def tcplink(sock,addr):
    #声明缓冲区，定义头包大小（打包信息）
    dataBuffer = bytes()
    headerSize = 4
    while True:
        data=sock.recv(2048)

        if data:
            # 把数据存入缓冲区，类似于push数据
            dataBuffer += data
            
            while True:
                #print 'data',data
                #print 'dataBuffer',dataBuffer
                #定义小于消息头长度的退出循环 （丢包与无消息情况下）
                if len(dataBuffer) < headerSize:
                    print(u"数据包（%s Byte）小于消息头部长度，跳出小循环" % len(dataBuffer))
                    break

                # 读取包头
                # struct中:!代表Network order，3I代表3个unsigned int数据
                headPack = struct.unpack('I', dataBuffer[:headerSize])
                bodySize = headPack[0]

                # 分包情况处理，跳出函数继续接收数据
                if len(dataBuffer) < headerSize+bodySize :
                    print(u"数据包（%s Byte）不完整（总共%s Byte），跳出小循环" % (len(dataBuffer), headerSize+bodySize))
                    break
                # 读取消息正文的内容
                print (u"数据包（%s Byte）完整（总共%s Byte）" % (len(dataBuffer), headerSize+bodySize))
                body = dataBuffer[headerSize:headerSize+bodySize]

                # 数据处理
                dataHandle(headPack, body)

                # 粘包情况的处理
                # 获取下一个数据包，类似于把数据pop出
                dataBuffer = dataBuffer[headerSize+bodySize:] 

        if data=='exit' or not data:
            break



while True:
    #获取客户端信息
    sock,addr=ksocket.accept()
    t=threading.Thread(target=tcplink(sock,addr))