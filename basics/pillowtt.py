#!/usr/bin/env python3
#coding=utf-8
#pillow

from PIL import Image,ImageFilter

#打开一个当前目录图像
im = Image.open('../test.jpg')
#获取图像尺寸
w,h = im.size
print(w,h)
#缩放到50%
im.thumbnail((w//2,h//2))
#保存为jpeg文件
im.save('thumbnail.jpg','jpeg')
ib = Image.open('thumbnail.jpg')
w1,h1 = ib.size
print(w1,h1)

#应用模糊滤镜
im2 = ib.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')