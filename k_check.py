# coding=utf-8
def k_check(p,s):
    import json as ss
    import sys
    import maya.cmds as cc
    import os    
    import time
    import struct
    import datetime
    path='D:/ziliao/201707/python_site-packages'
    if not path in sys.path:
        sys.path.append(path)
    import datetime
    from bson.objectid import ObjectId
    import pymongo
    client=pymongo.MongoClient('10.99.40.10',27017)
    db = client['k_text']
    kpost = db['check']


    import socket
    checkIP=('127.0.0.1',999)
    ksocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ksocket.connect(checkIP)
    sys.path.append('\\\\ftdyproject\\digital\\film_project\\hq_tool\\Maya\\hq_maya\\scripts\\fantabox\\common') 
    reload(sys)
    sys.setdefaultencoding('gbk')       
    import check    
    k_envpath='E:/work/7_0327_mayapy/text2/release/json/' 
    k_enablefiles=ss.loads(open(r'%sk_enable.json' %k_envpath).read(),encoding='gbk')
    k_enables=ss.loads(s,encoding='gbk')       
    cc.file(p,f=1,op="v=0;",esn=0,ignoreVersion=1,typ="mayaBinary",o=1)
    k_Treturn={}

    k_enablesize=0
    for i in k_enables.keys():
        if k_enables[i][0]:
            k_enablesize+=1

    kpercent=100./k_enablesize
    kprogres=0
    for k_enable in k_enables:
        if k_enables[k_enable][0]:
            kType=1
            k_return='check.%s()' %k_enable
            k_returna=eval(k_return)
            if k_returna:
                kType=2
            k_update={k_enable:k_returna}
            k_Treturn.update(k_update)

            kprogres=kprogres+kpercent
            ksend={kprogres:k_update}
            ksend=ss.dumps(ksend)

            #ver = 1
            #cmd = 100
            header = [ksend.__len__()]
            headPack = struct.pack("I", *header)
            ksendData = headPack+ksend.encode()

            ksocket.send(ksendData)
            #kreply=ksocket.recv(1024)

    #k_outputs=ss.dumps(k_Treturn)
    #
    check_post={u"检查人":"k",u"上传时间":datetime.datetime.now(),"maya_check":k_Treturn}
    kpost_id=kpost.insert(check_post)
    #print kpost_id
    ksend={"_id":str(kpost_id)}
    #ksend=ss.dumps(ksend)
    #ksocket.send(ksend)
    ksocket.close()









'''    for k_Treturns in k_Treturn:
        if k_Treturn[k_Treturns]:
            print ('---------'+k_enablefiles[k_Treturns][2]+'--------------')
            for k_Treturnss in k_Treturn[k_Treturns]:
                print (k_Treturnss) '''

