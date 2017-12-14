#!/usr/bin/env python3
#coding=utf-8

import tornado.web
import tornado.ioloop
import time

class ManagerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        ck = self.get_cookie('auth')
        if ck == '1':
            self.render('manager.html')
        else:
            self.redirect('/login')

class LogoutHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie('auth','1',expires=time.time())  #设置当前时间为cookie失效时间
        self.redirect('/login')

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html',status_text = '')

    def post(self, *args, **kwargs):
        username = self.get_argument('username',None)
        pwd = self.get_argument('password',None)
        check = self.get_argument('auto',None)
        if username == 'linweili' and pwd == '123':
            if check:
                # self.set_cookie('auth', '1', expires_days=7，path='/')  #cookie生效路径
                self.set_cookie('username',username)
                self.set_cookie('auth', '1',expires_days=7) #设置cookie过期时间为七天后
                self.redirect('/manager')
            else:
                r = time.time()+10
                self.set_cookie('username', username)
                self.set_cookie('auth', '1',expires=r)    #设置cookie过期时间为10秒
                self.redirect('/manager')

        else:
            self.render('login.html',status_text = '登录失败')

settings = {
    'static_path': 'static',
    'template_path':'views',
}

application = tornado.web.Application([
    #(r'/index/(?p<page>\d*)',LoginHandler),   动态路由
    (r'/login',LoginHandler),
    (r'/manager',ManagerHandler),
    (r'/logout',LogoutHandler),
], **settings)

#二级域名路由映射如buy.localhost.com
application.add_handlers('buy.localhost.com$',[
    (r"/index/(?P<page>\d*)", LoginHandler),      #二级域名访问函数
])


if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
