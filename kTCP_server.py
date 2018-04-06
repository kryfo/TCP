# -*- coding: utf-8 -*-
import socket
import threading
import time

# 1.创建socket，stream流式套接字,对应tcp
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# 设置允许复用地址,当建立连接之后服务器先关闭，设置地址复用
#  设置socket层属性    复用地址    允许
#s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#
# 2.绑定端口号
s.bind(('127.0.0.1',998))


# 3.接听状态
#listen中的black表示已经建立连接的总数
#如果当前已建立链接数以达到设定值，那么新客户端就不会connect成功，而是等待服务器。直到有链接退出。
s.listen(2)
print 'wait....'



def tcplink(sock,addr):

    kconnectioned = 'Accept new connection from %s:%s...     Welcome!!!' % addr
    sock.send(kconnectioned)	
    print '2.do!'
    time.sleep(2)
    while True:
    	# tcp recv() 只会返回接收到的数据
    	# 1024表示接受的数据长度
        data=sock.recv(1024)


        print ('3.cao,%s!'%data)
        time.sleep(5)

        #发送方关闭tcp的连接,recv()不会阻塞，而是直接返回''
        if data=='exit' or not data:
            break

        sock.send('Hello,%s!'%data)
    # 用完之后，关闭新创建的那个connect_socket
    sock.close()
    print '4 .Connection from %s:%s closed.'%addr
    #print ('sock is '+str(sock))
    #print ('addr is '+str(addr))
    

while True:
    
    #接受一个新连接 接受连接请求，创建新的连接套接字，用于客户端连通信
    sock,addr=s.accept()
    # 新创建连接用的socket, 客户端的地址
    #print(connect_socket)
    #print(client_addr)
    #创建新线程来处理TCP连接
    print '1.action'
    time.sleep(2)
    t=threading.Thread(target=tcplink(sock,addr))
