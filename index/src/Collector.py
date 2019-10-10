from flask.views import MethodView,request
from  flask import render_template,redirect
from .authentication_cookie import cookie
from ..script.device import device_name
class Collector(MethodView):
    @cookie
    def get(self):
        d=device_name()
        devices=d.dict_device()
        return render_template('collector.html',devices=devices)
    @cookie
    def post(self):
        res=request
        d = device_name()
        for i in res.form:
            d.update_data(skey=i,dkey=res.form[i])
        return redirect(res.path)