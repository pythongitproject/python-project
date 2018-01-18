#/usr/bin/env python3
#coding=utf-8
import tornado.web
import tornado.ioloop
from tornado_drawer.controllers import Home


settings = {
    'static_path':'statics',
    'template_path':'views'
}
application = tornado.web.Application([
    (r'/', Home.LoginHandler),

    ],**settings
)

if __name__ == '__main__':
    application.listen(6666)
    tornado.ioloop.IOLoop.instance().start()

