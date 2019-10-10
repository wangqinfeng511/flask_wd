import subprocess,re,os,json
from subprocess import Popen
from  ..src.config import Config
import os

class Addr:
    def get_addr(self,device_name):
        # path = os.getcwd()
        # file_path = os.path.join(path, 'index', 'data', 'data')
        path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
        file_path = os.path.join(path, 'data','data')
        if os.path.isfile(file_path):
            with open(file_path,'r') as f:
                data=json.loads(f.read())
            if data.get(device_name)==None:
                conf=Config()
                config=conf.config()
                if device_name==config.get('Wired_interface'):
                    data[device_name]={'ip':config.get('Wired_interface_IP'),'netmask':config.get('Wired_interface_NetMask')}
                elif device_name==config.get('Wifi_interface'):
                    data[device_name] = {'ip': config.get('Wifi_interface_IP'),
                                                          'netmask': config.get('Wifi_interface_NetMask')}
                else:
                    pass
        else:
            conf=Config()
            config=conf.config()
            data={}
            data[config.get('Wired_interface')]={'ip':config.get('Wired_interface_IP'),
                                                 'netmask':config.get('Wired_interface_NetMask')}
            data[config.get('Wifi_interface')] = {'ip': config.get('Wifi_interface_IP'),
                                                       'netmask': config.get('Wifi_interface_NetMask')}
        with open(file_path, 'w') as f:
            f.write(json.dumps(data))
        return {'ip': data.get(device_name).get('ip'), 'netmask': data.get(device_name).get('netmask'), 'getway':data.get(device_name).get('getway')}

    def post_addr(self, device_name, addr_dict=None):
        path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
        file_path = os.path.join(path, 'data','data')
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                data=json.loads(f.read())
                data[device_name] = addr_dict
            with open(file_path, 'w') as f:
                f.write(json.dumps(data))
        else:
            with open(file_path, 'w') as f:
                c={}
                c[device_name]=addr_dict
                f.write(json.dumps(c))
        # with Popen(['/bin/bash','-l','-c',"ifconfig {} {} {}".format(device_name,data.get(device_name).get('ip'),
        #                                                                 data.get(device_name).get('netmask'))]
        #             ,stdout=subprocess.PIPE,stderr=subprocess.STDOUT) as p:
        #         p.wait()
        return {'ip':data.get(device_name).get('ip'),
                'netmask':data.get(device_name).get('netmask'),'getway':data.get(device_name).get('getway')}
    def post_default_getway(self,default_getway):
        path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
        file_path = os.path.join(path, 'data','data')
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                data=json.loads(f.read())
                data['default_getway'] = default_getway
            with open(file_path, 'w') as f:
                f.write(json.dumps(data))
        return data['default_getway']
    def get_default_getway(self):
        path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
        file_path = os.path.join(path, 'data','data')
        with open(file_path, 'r') as f:
            data = json.loads(f.read())
        return data.get('default_getway')

    def set_addr(self,device_name):
        # path = os.getcwd()
        path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
        file_path = os.path.join(path, 'data','data')
        # file_path = os.path.join(path, 'index', 'data', 'data')
        with open(file_path, 'r') as f:
                data = json.loads(f.read())
        if data.get(device_name)==None:
            conf=Config()
            config=conf.config()
            if device_name==config.get('Wired_interface'):
                data[device_name]={'ip':config.get('Wired_interface_IP'),
                                   'netmask':config.get('Wired_interface_NetMask'),'gatway':'192.168.1.1'}
            elif device_name==config.get('Wifi_interface'):
                data[device_name] = {'ip': config.get('Wifi_interface_IP'),
                                     'netmask': config.get('Wifi_interface_NetMask'), 'gatway': '192.168.2.1'}
            with open(file_path,'w') as f:
                f.write(json.dumps(data))
        with Popen(['/bin/bash', '-l', '-c', "ifconfig {} {} {}".format(device_name, data.get(device_name).get('ip'),
                                                                            data.get(device_name).get('netmask'))]
                    , stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as p:
                p.wait()
        gatwey=data.get(device_name).get('getway')
        netmask=data.get(device_name).get('netmask')
        # if len(gatwey)!='':
        #     list_getway=gatwey.split('.')
        #     print('这是{}',list_getway)
        #     net=list_getway[0]+'.'+list_getway[1]+'.'+list_getway[2]+'.0'
        #     with Popen(['/bin/bash','-l','-c',"route add -net {net} gw {gatwey} netmask {netmask} dev {device_name}".format(
        #             net=net,gatwey=gatwey,netmask=netmask,device_name=device_name)]
        #                , stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as p :
        #         p.wait()
        if data.get('default_getway')!='':
            with Popen(['/bin/bash','-l','-c',"route add default gw {}".format(data.get('default_getway'))]
                    ,stdout=subprocess.PIPE,stderr=subprocess.STDOUT) as p:
                p.wait()

