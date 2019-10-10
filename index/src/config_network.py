from flask.views import MethodView
from flask import render_template,request,redirect,url_for
from .authentication_cookie import cookie
from ..script.addr import Addr
from ..script.connect_wifi import Wifi
from .config import Config
import os,json

class  Wired_addr(MethodView):
    @cookie
    def get(self):
        addrs=Addr()
        conf=Config()
        config=conf.config()
        device_name = config.get('Wired_interface')
        return render_template('wired_addr.html',addr=addrs.get_addr(device_name=device_name))
    @cookie
    def post(self):
        conf=Config()
        config=conf.config()
        device_name = config.get('Wired_interface')
        addrs = Addr()
        res_from=request.form
        addrs.post_addr(device_name=device_name,addr_dict={'ip':res_from.get('IP'),'netmask':res_from.get('NetMask'),
                                                           'getway':res_from.get('GetWay')})
        return render_template('wired_addr.html',addr=addrs.get_addr(device_name=device_name))
class Wifi_addr(MethodView):
    @cookie
    def get(self):
        addrs = Addr()
        conf=Config()
        config=conf.config()
        device_name = config.get('Wifi_interface')
        return render_template('wifi_config.html',addr=addrs.get_addr(device_name=device_name))
    def post(self):
        conf=Config()
        config=conf.config()
        device_name = config.get('Wifi_interface')
        addrs=Addr()
        res_from=request.form
        addrs.post_addr(
            addr_dict={'ip': res_from.get('IP'), 'netmask': res_from.get('NetMask'), 'getway': res_from.get('GetWay')},
        device_name=device_name)
        return render_template('wifi_config.html', addr=addrs.get_addr(device_name=device_name))
class Wifi_connect(MethodView):
    def __init__(self):
        self.wifi=Wifi()
    @cookie
    def get(self):
        return render_template('wifi_connect.html',ssid=self.wifi.list_wifi())
    @cookie
    def post(self):
        wifi_name_form=request.form
        wifi_name=wifi_name_form.get('wifi')
        password=wifi_name_form.get('password')
        if self.wifi.connect_wifi(wifi_name,password):
            path=os.path.dirname(os.path.realpath(__file__))
            data_file=os.path.join(os.path.dirname(path),'data','data')
            with open(data_file,'r') as f:
                data=json.loads(f.read())
                data['wifi']={'ssid':wifi_name,'password':password}
            with open(data_file,'w') as f:
                f.write(json.dumps(data))
            addr=Addr()
            conf = Config()
            config = conf.config()
            device_name = config.get('Wifi_interface')
            addr.set_addr(device_name)
            return redirect( url_for('.wifi_connect'))

        else:
            return 'connect error'
class Default_GetWay(MethodView):
    def get(self):
        addr = Addr()
        return render_template('default_getway.html',default_getway=addr.get_default_getway())
    def post(self):
        res=request
        default_getway=res.form.get('default_getway')
        addr=Addr()
        addr.post_default_getway(default_getway)
        return render_template('default_getway.html',default_getway=addr.get_default_getway())
