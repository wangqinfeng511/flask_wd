from flask import request,redirect,url_for
import jwt,datetime,os,json
from functools import wraps
def cookie(fun):
    @wraps(fun)
    def wrapper(*args,**kwargs):
        req=request
        cookie=req.cookies.get('user')
        path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
        file_path = os.path.join(path, 'src','data')
        with open(file_path, 'r') as f:
            data = json.loads(f.read())
            user = data.get('user')
            password = data.get('password')
            key=data.get('key')
        # print(cookie)
        if cookie!=None:
            try:
                cookie=jwt.decode(cookie,key,['HS512'])
            except:
                redirect(url_for('.LOGIN'))
            # print(cookie)
            if cookie.get('user')==user and cookie.get('password')==password:
                return fun(*args, **kwargs)
            else:
                return redirect('/index/LOG_IN')
        else:
            return redirect('/index/LOG_IN')

    return wrapper