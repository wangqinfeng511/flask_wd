from flask.views import MethodView
from flask import render_template,request
import os,json
class User_passwd(MethodView):
    def get(self):
        return render_template('password.html')
    def post(self):
        res=request.form
        user=res.get('user')
        password1=res.get('passworsd1')
        password2 = res.get('password2')
        path=os.path.split(os.path.realpath(__file__))[0]
        file_path=os.path.join(path,'data')
        with open(file_path,'r') as f:
            data=json.loads(f.read())
        if user==data.get('user') and password1==password2:
            data['password']=password1
            with open(file_path,'w') as f:
                f.write(json.dumps(data))
            return render_template('password_set_ok.html',value='修改完成！')
        else:
            return render_template('password_set_ok.html',value='ERROR！请确定用户名正确，密码输俩次！')