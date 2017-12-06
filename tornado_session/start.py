#!/usr/bin/env python3
#coding=utf-8

import tornado.web
import tornado.ioloop
import time

container = {}
class Session:
    def __init__(self,handler):
        self.handler = handler
        self.random_str = None
        pass

    #生成随机字符串
    def __generate__random_str(self):
        import hashlib
        import time
        obj = hashlib.md5()
        obj.update(bytes(str(time.time()),encoding='utf-8'))
        random_str = obj.hexdigest()
        return random_str

    def set_value(self,key,value):
        #在container中加入随机字符串
        #定义专属于自己的数据
        #在客户端写入随机字符串
        if not self.random_str:
            random_str = self.handler.get_cookie('u')
            if not random_str:
                random_str = self.__generate__random_str()
                container[random_str] = {}
            else:
                if random_str in container.keys():
                    pass
                else:
                    random_str = self.__generate__random_str()
                    container[random_str] = {}
        container[random_str][key] = value
        self.handler.set_cookie('u',random_str)

    def get_value(self,key):
        random_str = self.handler.get_cookie('u')
        if not random_str:
            return None
        user_info_dict = container.get(random_str)
        if not user_info_dict:
            return None
        value = user_info_dict.get(key)
        if not value:
            return None
        return value



class ManagerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        s = Session(self)
        val = s.get_value('is_login')
        if val:
            self.render('manager.html')
        else:
            self.redirect('/login')

class LogoutHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        s = Session(self)
        val = s.get_value('is_login')
        if val:
            s.set_value('is_login', False)
            self.redirect('/login')

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html',status_text = '')

    def post(self, *args, **kwargs):
        username = self.get_argument('username',None)
        pwd = self.get_argument('password',None)
        if username == 'linweili' and pwd == '123':
            s = Session(self)
            s.set_value('is_login',True)
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