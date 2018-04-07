# -*- coding: utf-8 -*-
import socket
import time
import struct
import json

host = '127.0.0.1'
port = 999

ADDR = (host, port)

if __name__ == '__main__':
    client = socket.socket()
    client.connect(ADDR)

    ver = 3

    body1 = json.dumps(dict(hello="world3"))
    #print(body1)
    cmd = 103
    header = [ver, body1.__len__(), cmd]
    headPack1 = struct.pack("!3I", *header)

    ver = 4
    body2 = json.dumps(dict(hello="world4"))
    #print(body2)
    cmd = 104
    header = [ver, body2.__len__(), cmd]
    headPack2 = struct.pack("!3I", *header)

    ver = 5
    body3 = json.dumps(dict(hello="world5"))
    #print(body2)
    cmd = 105
    header = [ver, body3.__len__(), cmd]
    headPack3 = struct.pack("!3I", *header)

    sendData3 = headPack1+body1.encode()+headPack2+body2.encode()+headPack3+body3.encode()

    print sendData3
    # 粘包测试
    client.send(sendData3)
    #time.sleep(1)
    client.close()