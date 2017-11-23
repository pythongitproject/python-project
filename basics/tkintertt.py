#!/usr/bin/env python3
#coding=utf-8
#tkinter gui

from tkinter import *
import tkinter.messagebox as messagebox

#第二步是从Frame派生一个Application类，这是所有Widget的父容器：
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text='Hello',
                                  command = self.hello)
        self.alertButton.pack()
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello,%s' % name)

app = Application()
print(app.master.title)
app.mainloop()