#/usr/bin/env python3
#coding=utf-8
import tornado.web
import json, datetime
from tornado_drawer.utils import db
from tornado_drawer.models.models import *
#基类
class BaseHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        #默认访问登录页
        self.render('login.html',status_text = '')
    def initialize(self):
        self.db = db.getSession()

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
    def get(self, *args, **kwargs):
        status = self.get_secure_cookie('is_login')
        telno = self.get_secure_cookie('telno',None)
        if telno:
            uinfo = self.db.query(userinfo).filter_by(telno=bytes.decode(telno)).first()
            self.render('index.html', flag=status, username=uinfo.name, item_list=None)
        else:
            self.render('index.html',flag=status,username=None,item_list=None)

class RegisterHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('register.html',status_text='')

    def post(self, *args, **kwargs):
        dic = {'status': True, 'msg': '', 'typeid': 0}
        username = self.get_argument('username')
        password = self.get_argument('password')
        telno = self.get_argument('telno')
        try:
            uinfo = self.db.query(userinfo).filter_by(telno=telno).first()
        except:
            dic['status'] = False
            dic['msg'] = '网络闹情绪了，请重试！'
            dic['typeid'] = -3
            self.write(json.dumps(dic))
        if uinfo:
            dic['status'] = False
            dic['msg'] = '该用户已存在'
            dic['typeid'] = -2
            self.write(json.dumps(dic))
        else:
            try:
                adddate = datetime.datetime.now()
                self.db.add(userinfo(name=username, telno=telno, pwd=password, adddate=adddate))
                self.db.commit()
                dic['msg'] = '注册成功，点击跳往登录页'
                self.write(json.dumps(dic))
            except:
                dic['status'] = False
                dic['msg'] = '注册失败，请重新注册！'
                dic['typeid'] = -1
                self.write(json.dumps(dic))




class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('login.html',status_text ='')

    def post(self, *args, **kwargs):
        telno = self.get_argument('telno',None)
        pwd = self.get_argument('password',None)
        check_code = self.get_argument('code',None)
        dic = {'status': True, 'msg': '','typeid':0}
        if check_code.upper() == bytes.decode(self.get_secure_cookie('code')).upper():
            try:
                uinfo = self.db.query(userinfo).filter_by(telno=telno).first()
            except:
                dic['status'] = False
                dic['typeid'] = -3
                dic['msg'] = '该用户不存在,请注册后登录！'
                self.write(json.dumps(dic))
            if uinfo:
                if pwd == uinfo.pwd :
                    self.clear_cookie('code')
                    self.set_secure_cookie('is_login', 'True')
                    self.set_secure_cookie('telno', telno)
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
                dic['msg'] = '该用户不存在,请注册后登录！'
                self.write(json.dumps(dic))
        else:
            dic['status'] = False
            dic['typeid'] = -2
            dic['msg'] = '验证码错误，请重新输入！'
            self.write(json.dumps(dic))

class DropoutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.clear_all_cookies()
        self.redirect('/index')

class LogoutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        telno = self.get_secure_cookie('telno')
        try:
            self.db.query(userinfo).filter_by(telno = bytes.decode(telno)).delete()
            self.db.commit()
            self.clear_all_cookies()
            self.redirect('/index')
        except:
            self.redirect('/index')

