import tornado.web
import tornado.ioloop
import tornado_demo.uimethod as mt
import tornado_demo.uimodule as md

#static_url 静态文件自动更新缓存
#模板引擎的本质就是分割字符串拼接


INPUT_LIST = []
USER_INFO = {
    'is_login':None,
}
ITEM_LIST = [
    {'title':'python基础','content':'数据类型、条件判断、切片'},
]
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

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.render('index.html',is_login = IS_LOGIN['is_login'])
        self.render('index.html',user_info = USER_INFO,item_list = ITEM_LIST)

class LoginHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        username = self.get_argument('username',None)
        pwd = self.get_argument('pwd',None)
        if username == 'linweili' and pwd == '123':
            USER_INFO['is_login'] = True
            USER_INFO['username'] = username
        self.redirect('/index')

class PublishHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        if USER_INFO['is_login']:
            title = self.get_argument('title', None)
            content = self.get_argument('content', None)
            temp = {'title': title, 'content': content}
            ITEM_LIST.append(temp)
        # self.render('index.html',user_info = USER_INFO)
        self.redirect('/index')

settings = {
    'template_path':'views',    #模板路径配置
    'static_path':'static',    #静态文件路径配置
    'static_url_prefix':'/sss/',    #静态文件前缀
    'ui_methods': mt,
    'ui_modules':md,
}
#路由映射、路由系统
application = tornado.web.Application([
    # (r'/index',MainHandler),
    (r'/index',IndexHandler),
    (r'/login',LoginHandler),
    (r'/pub',PublishHandler),
], **settings)

if __name__ == '__main__':
    #socket运行起来
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()