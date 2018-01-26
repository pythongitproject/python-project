#/usr/bin/env python3
#coding=utf-8
import tornado.web
import tornado.ioloop
from tornado_test.controllers import Home
import tornado.autoreload

settings = {
    'static_path':'statics',
    'template_path':'views',
    'cookie_secret':'MTg4MTQyODg3ODQrMjAxOC0wMS0yMCAwMTowMDowMA',
    'login_url': '/login',
    'xsrf_cookies':True,
    #'debug':True
}
application = tornado.web.Application([
    (r'/', Home.LoginHandler),
    (r'/index', Home.IndexHandler),
    (r'/login',Home.LoginHandler),
    (r'/dropout',Home.DropoutHandler),
    (r'/check_code',Home.Check_codeHandler),
    (r'/interface',Home.InterfaceHandler),
    (r'/test_yongli',Home.InterfaceCaseHandler),
    (r'/events',Home.EventsHandler),
    (r'/project',Home.ProjectHandler),
    (r'/model',Home.ModelHandler),
    (r'/admin',Home.AdminHandler),
    (r'/test_result',Home.TestResultHandler),
    (r'/timingtask',Home.TimingtaskHandler),
    (r'/add_interface',Home.AddInterfaceHandler),
    ], **settings)

if __name__ == '__main__':
    application.listen(7777)
    tornado.ioloop.IOLoop.instance().start()

