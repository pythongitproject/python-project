#!/usr/bin/env python3
#coding=utf-8

import tornado.web
import tornado.ioloop

class ManagerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        ck = self.get_cookie('auth')
        if ck == '1':
            self.render('manager.html')
        else:
            self.redirect('/login')

class LogoutHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie('auth','0')
        self.redirect('/login')

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html',status_text = '')

    def post(self, *args, **kwargs):
        username = self.get_argument('username',None)
        pwd = self.get_argument('password',None)
        if username == 'linweili' and pwd == '123':
            self.set_cookie('auth','1')
            self.redirect('/manager')
        else:
            self.render('login.html',status_text = '登录失败')

settings = {
    'static_path': 'static',
    'template_path':'views',
}

application = tornado.web.Application([
    (r'/login',LoginHandler),
    (r'/manager',ManagerHandler),
    (r'/logout',LogoutHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()