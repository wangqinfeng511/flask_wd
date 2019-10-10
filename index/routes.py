from flask import Flask,Blueprint
from index.src.Index import Index,LogIn
from index.src.config_network import Wifi_addr,Wired_addr,Wifi_connect,Default_GetWay
from index.src.Collector import Collector
from .src.temperature import Temperature,API
from .src.reboot import Reboot
from .src.user_password import User_passwd
index=Blueprint('index',__name__,template_folder="templates", static_folder='static')
index.add_url_rule('/config_wifi_addr',view_func=Wifi_addr.as_view('config_wifi_addr'))
index.add_url_rule('/wifi_connect',view_func=Wifi_connect.as_view('wifi_connect'))
index.add_url_rule('/config_wired_addr',view_func=Wired_addr.as_view('config_wired_addr'))
index.add_url_rule('/LOG_IN',view_func=LogIn.as_view('login'))
index.add_url_rule('/',view_func=Index.as_view('index'))
index.add_url_rule('/collector',view_func=Collector.as_view('collector'))
index.add_url_rule('/temperature',view_func=Temperature.as_view('temperature'))
index.add_url_rule('/api',view_func=API.as_view('api'))
index.add_url_rule('/reboot',view_func=Reboot.as_view('reboot'))
index.add_url_rule('/user',view_func=User_passwd.as_view('password'))
index.add_url_rule('/default_getway',view_func=Default_GetWay.as_view('default_getway'))