#/usr/bin/env python3
#coding=utf-8
import tornado.web
from sqlalchemy.sql import and_,or_
import json, datetime
from tornado_test.utils import db
from tornado_test.models.models import *
import requests

#基类
class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = db.getSession()
    def get_current_user(self):
        return self.get_secure_cookie('um')

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
                    self.set_secure_cookie('um', userinfo.name,expires_days=3,expires = time.time()+9900)
                    self.set_secure_cookie('uid', str(userinfo.id),expires_days=3,expires = time.time()+9900)
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
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.clear_all_cookies()
        self.redirect('/login')

class InterfaceHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('interface.html',username=self.current_user,inter='')


class AddInterfaceHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('add_interface.html', username=self.current_user)

    def post(self, *args, **kwargs):
        tt = self.get_argument('types')
        params = self.get_arguments('params')
        print(params)
        pp = ''.join(params)
        print(pp)
        print(json.loads(pp))
        testurl = self.get_argument('testurl');
        if tt.upper()=='GET':
            dic = {'type':1}
            try:
                r = requests.get(testurl,params= json.loads(pp))
                dic['status_code'] = r.status_code
                dic['head'] = str(r.headers)
                dic['resbody'] = r.json()
                self.write(json.dumps(dic))
            except:
                dic = {'type': -1}
                self.write(json.dumps(dic))
        else:
            dic = {'type': 1}
            try:
                r = requests.post(testurl,data=json.loads(pp))
                print(r.url)
                print(r.json())
                dic['status_code'] = r.status_code
                dic['head'] = str(r.headers)
                dic['resbody'] = r.json()
                self.write(json.dumps(dic))
            except:
                dic = {'type': -1}
                self.write(json.dumps(dic))

class ProjectHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('project.html',username='linweili')

class ModelHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('model.html', username='linweili')

class TimingtaskHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('timingtask.html', username='linweili')
class InterfaceCaseHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('interface_yongli.html', username='linweili')

class AdminHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('useradmin.html', username='linweili')

class TestResultHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('test_result.html', username='linweili')

class EventsHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('events.html', username='linweili')









