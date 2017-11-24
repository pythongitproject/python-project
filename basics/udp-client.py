#!/usr/bin/env python3
#coding=utf-8

#udp编程
#使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，
# 就可以直接发数据包。但是，能不能到达就不知道了
#速度快
import socket
#SOCK_DGRAM指定了这个Socket的类型是UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    s.sendto(data,('127.0.0.1',9999))
    print(s.recv(1024).decode('utf-8'))
s.close()
