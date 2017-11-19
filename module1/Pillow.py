#!/usr/bin/env python3
#coding=utf-8
#第三方库:处理图像 Pillow

from PIL import Image
im = Image.open('test.jpg')
print(im.format,im.size,im.mode) #输入图片大小，阵列
im.thumbnail((200,100))
im.save('thumb.png')
print(Image.open('thumb.png').mode)