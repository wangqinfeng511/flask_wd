import os,json
from ..src.config import Config
class device_name:
    def list_device(self):
        conf=Config()
        config=conf.config()
        device_bus_dir=config.get('device_bus_dir')
        d=os.listdir(device_bus_dir)
        devices=[]
        for i in d:
            if i.startswith('28-'):
                devices.append(i)
        return devices
    def dict_device(self):
        # path=os.getcwd()
        # file_path=os.path.join(path,'index','data','data')
        path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
        file_path = os.path.join(path, 'data','data')
        with open(file_path,'r') as f:
            data=json.loads(f.read())
        if data.get('devices')==None:
            devices=self.list_device()
            data['devices']=[]
            number=0
            for i in devices:
                data['devices'].append([number+1,i,1])
                number=number+1
        with open(file_path,'w') as f:
            f.write(json.dumps(data))
        return data.get('devices')
    def update_data(self,skey,dkey):
        path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
        file_path = os.path.join(path, 'data','data')
        with open(file_path,'r') as f:
            data=json.loads(f.read())
        number=0

        for i in data['devices']:
            if str(i[0])==skey:
                data['devices'][number][0]=dkey
            number=number+1

        with open(file_path,'w') as f:
            f.write(json.dumps(data))
        return data['devices']
    # def lsit_device_vs_data_devices(self,data):
    #     ds=[]
    #     s=self.list_device()
    #     for i in data['devices']:
    #         ds.append(i[1])
    #     if len(ds)>len(s):
    #         for i in ds:
    #             pass



