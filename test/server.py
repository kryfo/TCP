# Python Version:3.5.1
import socket
import struct

HOST = '127.0.0.1'
PORT = 998

dataBuffer = bytes()
headerSize = 12

sn = 0
def dataHandle(headPack, body):
    global sn
    sn += 1
    print(u"第%s个数据包" % sn)
    print(u"ver:%s, bodySize:%s, cmd:%s" % headPack)
    print(body.decode())
    print("")



if __name__ == '__main__':

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)

        if data:
            # 把数据存入缓冲区，类似于push数据
            dataBuffer += data
            print '-----------------'
            while True:
                print 'data',data
                print 'dataBuffer',dataBuffer

                if len(dataBuffer) < headerSize:
                    print(u"数据包（%s Byte）小于消息头部长度，跳出小循环" % len(dataBuffer))
                    break

                # 读取包头
                # struct中:!代表Network order，3I代表3个unsigned int数据
                headPack = struct.unpack('!3I', dataBuffer[:headerSize])
                bodySize = headPack[1]

                # 分包情况处理，跳出函数继续接收数据
                if len(dataBuffer) < headerSize+bodySize :
                    print(u"数据包（%s Byte）不完整（总共%s Byte），跳出小循环" % (len(dataBuffer), headerSize+bodySize))
                    break
                # 读取消息正文的内容
                body = dataBuffer[headerSize:headerSize+bodySize]

                # 数据处理
                dataHandle(headPack, body)

                # 粘包情况的处理
                dataBuffer = dataBuffer[headerSize+bodySize:] # 获取下一个数据包，类似于把数据pop出
