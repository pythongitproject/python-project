#/usr/bin/env python3
#coding=utf-8
import tornado.web
from sqlalchemy.sql import and_,or_
import json, datetime
from tornado_test.utils import db
from tornado_test.models.models import *

#基类
class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = db.getSession()
    def get_current_user(self):
        return self.get_secure_cookie('uid')

class Check_codeHandler(BaseHandler):
    def get(self, *args, **kwargs):
        import io
        mstream = io.BytesIO()
        #获取验证码
        from tornado_drawer.utils import check_code
        img, code = check_code.create_validate_code()
        self.set_secure_cookie('code',code)
        img.save(mstream, "PNG")
        self.write(mstream.getvalue())

class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        um = self.get_secure_cookie('um')
        self.render('index.html',username=bytes.decode(um))

class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')
    def post(self, *args, **kwargs):
        telno = self.get_argument('telno',None)
        pwd = self.get_argument('password',None)
        check_code = self.get_argument('code',None)
        dic = {'status': True, 'msg': '','typeid':0}
        if check_code.upper() == bytes.decode(self.get_secure_cookie('code')).upper():
            try:
                userinfo = self.db.query(UserInfo).filter_by(telno=telno).first()
            except:
                dic['status'] = False
                dic['typeid'] = -3
                dic['msg'] = '该用户不存在,请联系管理员！'
                self.write(json.dumps(dic))
            if userinfo:
                if pwd == userinfo.pwd :
                    import time
                    #expires_day=None, 或者expires_day=3, 即3天, 都不会影响expires的, 因为expires比expires_days 的优先级高些. 所以这里设置为15分钟可以简化为
                    self.clear_cookie('code')
                    self.set_secure_cookie('um', userinfo.name,expires_days=3,expires = time.time()+900)
                    self.set_secure_cookie('uid', str(userinfo.id),expires_days=3,expires = time.time()+900)
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
                dic['msg'] = '该用户不存在,请联系管理员！'
                self.write(json.dumps(dic))
        else:
            dic['status'] = False
            dic['typeid'] = -2
            dic['msg'] = '验证码错误，请重新输入！'
            self.write(json.dumps(dic))

class DropoutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.clear_all_cookies()
        self.redirect('/login')

class LogoutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        telno = self.get_secure_cookie('telno')
        try:
            self.db.query(UserInfo).filter_by(telno = bytes.decode(telno)).delete()
            self.db.commit()
            self.db.close()
            self.clear_all_cookies()
            self.redirect('/index')
        except:
            self.redirect('/index')

class UserAdminHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('add_interface.html',username ='linweili',inte='')







