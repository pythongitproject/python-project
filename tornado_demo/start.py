import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.write('hello, get')
        self.render('s1.html')

    def post(self, *args, **kwargs):
        self.write('hello, post')


settings = {
    'template_path':'template',    #模板路径配置
    'static_path':'static',    #静态文件路径配置
}
#路由映射、路由系统
application = tornado.web.Application([
    (r'/index',MainHandler),
], **settings)

if __name__ == '__main__':
    #socket运行起来
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()