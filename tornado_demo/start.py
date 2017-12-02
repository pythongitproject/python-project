import tornado.web
import tornado.ioloop
import tornado_demo.uimethod as mt
import tornado_demo.uimodule as md

#static_url 静态文件自动更新缓存



INPUT_LIST = []
class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.write('hello, get')

        self.render('s1.html',npm = 'NPM888',xxxooo = INPUT_LIST)

    def post(self, *args, **kwargs):
        name = self.get_argument('xxx', None)  #提交默认值
        if name:
            INPUT_LIST.append(name)
        # self.write('hello, post',xxxooo = INPUT_LIST)
        self.render('s1.html',npm = 'NPM888', xxxooo=INPUT_LIST)


settings = {
    'template_path':'template',    #模板路径配置
    'static_path':'static',    #静态文件路径配置
    'static_url_prefix':'/sss/',    #静态文件前缀
    'ui_methods': mt,
    'ui_modules':md,
}
#路由映射、路由系统
application = tornado.web.Application([
    (r'/index',MainHandler),
], **settings)

if __name__ == '__main__':
    #socket运行起来
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()