#!/usr/bin/env python3
#coding=utf-8

#udp编程
#使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，
# 就可以直接发数据包。但是，能不能到达就不知道了
#速度快
import socket
#SOCK_DGRAM指定了这个Socket的类型是UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
print('bind udp on 9999...')
while True:
    data,addr = s.recvfrom(1024)  #recvfrom()方法返回数据和客户端的地址与端口
    print('reeived from %s:%s.' % addr)
    s.sendto(b'hello,%s!' % data,addr)
