#!/usr/bin/env python3
#coding=utf-8

import tornado.web
import tornado.ioloop

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')

    def post(self, *args, **kwargs):
        dic = {'status':True,'msg':''}
        username = self.get_argument('username',None)
        pwd = self.get_argument('password',None)
        if username == 'linweili' and pwd == '123':
            pass
        else:
            dic['status'] = False
            dic['msg'] = '用户名或密码错误'
        import json
        self.write(json.dumps(dic))



settings = {
    'static_path': 'static',
    'template_path':'views',
}

application = tornado.web.Application([
    (r'/login',LoginHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()