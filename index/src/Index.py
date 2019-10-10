from flask import Flask,render_template,request,redirect,Blueprint,url_for,make_response
from flask.views import  MethodView
import json,os,jwt,datetime
from .authentication_cookie import cookie


class Index(MethodView):
    @cookie
    def get(self):
        return render_template('config_addrs.html')

class LogIn(MethodView):
    def get(self):
        return  render_template('login.html')
    def post(self):
        user_password=request.form
        renzheng=self.cookie(user_password)
        if renzheng !=None:
            res = make_response(render_template('config_addrs.html'))
            res.set_cookie('user',renzheng)
            return res
        else:
            return redirect(url_for('.login'))
    def cookie(self,user_password):
        path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
        file_path = os.path.join(path, 'src','data')
        print(file_path)
        with open(file_path, 'r') as f:
            data = json.loads(f.read())
            user = data.get('user')
            password = data.get('password')
            key=data.get('key')
            print(user,password,key)
        if user_password.get('user') == user and user_password.get('password') == password:
            d=datetime.datetime.now()+datetime.timedelta(hours=8)
            token=jwt.encode({'user':user_password.get('user'),
                              'password':user_password.get('password'),
                              'exp':d},key,'HS512')
            return token
        else:
            return None


