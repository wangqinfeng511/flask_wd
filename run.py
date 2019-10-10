from flask import Flask, redirect
from index.routes import index
from index.script.addr import Addr
from index.script.connect_wifi import Wifi
from index.src.config import Config
import os,json
app=Flask(__name__)
app.register_blueprint(index,url_prefix='/index')
@app.route('/')
def main():
    return redirect('/index')
def connect_interface():
    addr = Addr()
    wifi = Wifi()
    conf = Config()
    config = conf.config()
    path=os.path.split(os.path.realpath(__file__))[0]
    data_file=os.path.join(path,'index','data','data')
    with open(data_file,'r') as f:
        data=json.loads(f.read())
    if data.get('wifi') != None:
        wifi_user_password = data.get('wifi')
        if wifi.connect_wifi(ssid=wifi_user_password.get('ssid')
                              , password=wifi_user_password.get('password')):
            addr.set_addr(config.get('Wifi_interface'))
    addr.set_addr(config.get('Wired_interface'))
if __name__=='__main__':
    connect_interface()
    app.run(host='0.0.0.0',port=80)
