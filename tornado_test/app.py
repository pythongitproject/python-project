#/usr/bin/env python3
#coding=utf-8
import tornado.web
import tornado.ioloop
from tornado_test.controllers import Home

settings = {
    'static_path':'statics',
    'template_path':'views',
    'cookie_secret':'MTg4MTQyODg3ODQrMjAxOC0wMS0yMCAwMTowMDowMA',
}
application = tornado.web.Application([
    (r'/', Home.BaseHandler),
    (r'/index', Home.IndexHandler),
    (r'/login',Home.LoginHandler),
    (r'/logout',Home.LogoutHandler),
    (r'/dropout',Home.DropoutHandler),
    (r'/check_code',Home.Check_codeHandler),
    ], **settings)

if __name__ == '__main__':
    application.listen(7777)
    tornado.ioloop.IOLoop.instance().start()

