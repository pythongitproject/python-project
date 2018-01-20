#/usr/bin/env python3
#coding=utf-8
import tornado.web
import json
from tornado_drawer.utils import db
from tornado_drawer.models.models import *
#基类
class BaseHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        #默认访问登录页
        self.render('login.html',status_text = '')

class Check_codeHandler(BaseHandler):
    def get(self, *args, **kwargs):
        import io
        mstream = io.BytesIO()
        #获取验证码
        from tornado_drawer.utils import check_code
        img, code = check_code.create_validate_code()
        self.set_cookie('code',code)
        img.save(mstream, "PNG")
        self.write(mstream.getvalue())

class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        status = self.get_secure_cookie('is_login')
        uname = self.get_secure_cookie('uname')
        self.render('index.html',flag=status,username=uname,item_list=None)

class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('login.html',status_text = '')

    def post(self, *args, **kwargs):
        username = self.get_argument('username',None)
        pwd = self.get_argument('password',None)
        check_code = self.get_argument('code',None)
        dic = {'status': True, 'msg': '','typeid':0}
        if check_code.upper() == self.get_cookie('code').upper():
            try:
                uinfo = db.getSession().query(userinfo).filter_by(name=username).first()
                print(0)
            except:
                print(1)
                dic['status'] = False
                dic['typeid'] = -3
                dic['msg'] = '该用户不存在！'
                self.write(json.dumps(dic))
            if uinfo:
                if pwd == uinfo.pwd :
                    self.clear_cookie('code')
                    self.set_secure_cookie('is_login', 'True')
                    self.set_secure_cookie('uname', 'linweili')
                    dic['typeid'] = 2
                    self.write(json.dumps(dic))
                else:
                    dic['status'] = False
                    dic['typeid'] = -1
                    dic['msg'] = '用户名或密码错误！'
                    self.write(json.dumps(dic))
            else:
                dic['status'] = False
                dic['typeid'] = -3
                dic['msg'] = '该用户不存在！'
                self.write(json.dumps(dic))
        else:
            dic['status'] = False
            dic['typeid'] = -2
            dic['msg'] = '验证码错误，请重新输入！'
            self.write(json.dumps(dic))

class LogoutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.clear_all_cookies()
        self.redirect('/index')
