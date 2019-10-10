from flask import Flask,render_template
from flask.views import MethodView
from .authentication_cookie import cookie
from ..script.temperature import getwd
import os,json

class Temperature(MethodView):
    @cookie
    def get(self):
        # dir=os.getcwd()
        # file_path=os.path.join(dir,'index','data','data')
        path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
        file_path = os.path.join(path, 'data','data')
        with open(file_path,'r') as f:
            data=json.loads(f.read())
            devices={}
            for i in data['devices']:
                devices[i[0]]=i[1]
        wendu=getwd()
        wendu_list=[]
        for i in devices:
            wendu_list.append([i,wendu.get_wd(device_name=devices[i])])
        return render_template('temperature.html',wendu=wendu_list)
class API(MethodView):
    def get(self):
        path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
        file_path = os.path.join(path, 'data','data')
        with open(file_path,'r') as f:
            data=json.loads(f.read())
            devices={}
            for i in data['devices']:
                devices[i[0]]=i[1]
        wendu=getwd()
        wendu_list=[]
        for i in devices:
            wendu_list.append([i,wendu.get_wd(device_name=devices[i])])
        return json.dumps(wendu_list)
