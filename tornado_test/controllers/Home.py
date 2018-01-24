#/usr/bin/env python3
#coding=utf-8
import tornado.web
from sqlalchemy.sql import and_,or_
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
        telno = self.get_secure_cookie('telno')
        uname = self.get_secure_cookie('username')
        poststype = self.get_argument('posts_type',None)
        try:
            item_list = self.db.query(Posts.id,Posts.title,UserInfo.name,Posts.content,Posts.adddate,Posts.click_count,Posts.like_count).join(UserInfo).order_by(Posts.adddate.desc(),Posts.click_count.desc(),Posts.like_count.desc()).all()[0:3]
            self.db.close()
        except:
            item_list = ''
        if telno:
            uinfo = self.db.query(UserInfo).filter_by(telno=bytes.decode(telno)).first()
            self.db.close()
            if status:
                self.render('index.html', flag=bytes.decode(status), username=bytes.decode(uname), item_list=item_list)
            else:
                self.render('index.html', flag=None, username=None, item_list=item_list)
        else:
            self.render('index.html',flag=None,username=None,item_list=item_list)

class Single_indexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        status = self.get_secure_cookie('is_login')
        uname = self.get_secure_cookie('username')
        userid = self.get_secure_cookie('userid')
        if status and uname and userid:
            item_list = self.db.query(Posts.id, Posts.title, UserInfo.name, Posts.content, Posts.adddate,
                                      Posts.click_count, Posts.like_count).join(UserInfo).filter(
                Posts.user_id == bytes.decode(userid)).order_by(Posts.adddate.desc(), Posts.click_count.desc(),
                                                  Posts.like_count.desc()).all()[0:3]
            self.db.close()
            if item_list:
                self.render('singleindex.html', flag=bytes.decode(status), username=bytes.decode(uname),
                            item_list=item_list)
            else:
                self.render('index.html', flag=bytes.decode(status), username=bytes.decode(uname), item_list='')
        else:
            self.redirect('/login')

class RegisterHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('register.html',status_text='')

    def post(self, *args, **kwargs):
        dic = {'status': True, 'msg': '', 'typeid': 0}
        username = self.get_argument('username')
        password = self.get_argument('password')
        telno = self.get_argument('telno')
        try:
            uinfo = self.db.query(UserInfo).filter_by(telno=telno).first()
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
                self.db.add(UserInfo(name=username, telno=telno, pwd=password, adddate=adddate))
                self.db.commit()
                self.db.close()
                dic['msg'] = '注册成功，点击跳往登录页'
                self.write(json.dumps(dic))
            except:
                dic['status'] = False
                dic['msg'] = '注册失败，请重试！'
                dic['typeid'] = -1
                self.write(json.dumps(dic))

class ClickHandler(BaseHandler):
    def post(self, *args, **kwargs):
        dict = {'status': True,'typeid':1 ,'msg':'完美的一击~'}
        userid = self.get_secure_cookie('userid')
        if userid:
            userid = bytes.decode(userid)
            newsid = self.get_argument('newsid')
            click_count = int(self.get_argument('click_count'))
            import time
            adddate = time.strftime("%Y-%m-%d", time.localtime())
            count = self.db.query(ClickPosts).filter(ClickPosts.postsid ==newsid,ClickPosts.user_id ==userid,ClickPosts.adddate >= adddate ).count()
            if count>0 :
                dict['status'] = False
                dict['typeid'] = -3
                dict['msg'] = '今天已点赞，明天赶脚哦~'
                self.write(json.dumps(dict))
            else:
                try:
                    cpost = ClickPosts(postsid=newsid, user_id=userid, adddate=datetime.datetime.now())
                    self.db.add(cpost)
                    click_count += 1
                    print(click_count)
                    self.db.query(Posts).filter(Posts.id==newsid).update({Posts.click_count:click_count})
                    print(2)
                    self.db.commit()
                    self.db.close()
                    self.write(json.dumps(dict))
                except:
                    dict['status'] = False
                    dict['typeid'] = -4
                    dict['msg'] = '姿势不对，点赞失败了~'
                    self.db.close()
                    self.write(json.dumps(dict))
        else:
            dict['status'] = False
            dict['typeid'] = -1
            dict['msg'] = '登录才可以点赞哦~'
            self.write(json.dumps(dict))

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
                userinfo = self.db.query(UserInfo).filter_by(telno=telno).first()
            except:
                dic['status'] = False
                dic['typeid'] = -3
                dic['msg'] = '该用户不存在,请注册后登录！'
                self.write(json.dumps(dic))
            if userinfo:
                if pwd == userinfo.pwd :
                    self.clear_cookie('code')
                    self.set_secure_cookie('is_login', 'True')
                    self.set_secure_cookie('telno', telno)
                    self.set_secure_cookie('username', userinfo.name)
                    self.set_secure_cookie('userid', str(userinfo.id))
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
            self.db.query(UserInfo).filter_by(telno = bytes.decode(telno)).delete()
            self.db.commit()
            self.db.close()
            self.clear_all_cookies()
            self.redirect('/index')
        except:
            self.redirect('/index')

class ReleaseHandler(BaseHandler):
    def post(self, *args, **kwargs):
        dd = {
            'status':True,
            'typeid':1
        }
        title = self.get_argument('title')
        content = self.get_argument('content')
        adddate = datetime.datetime.now()
        telno = bytes.decode(self.get_secure_cookie('telno'))
        u1 = self.db.query(UserInfo).filter_by(telno=telno).first()
        p1 = Posts(title=title, content=content, adddate=adddate)
        u1.pts.append(p1)
        self.db.add(p1)
        try:
            self.db.commit()
            self.db.close()
            self.write(json.dumps(dd))
        except:
            dd['typeid'] = -1
            dd['status'] = False
            self.write(json.dumps(dd))




