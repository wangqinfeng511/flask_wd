import os
from  ..src.config import Config
class getwd:
    def get_wd(self,dir=None,device_name=None):
        conf=Config()
        config=conf.config()

        device_dir=os.path.join(config.get('device_bus_dir'),device_name)
        print(device_dir)
        if os.path.isdir(device_dir):
            save_file=os.path.join(device_dir,'w1_slave')
            if os.path.isfile(save_file):
                with open(save_file) as f:
                    wd=f.read().split()[-1].split('=')
                    Wd=int(wd[-1])//1000
            else: Wd=-255
        else:
            return 'device not cun zai'
        return Wd
if __name__=='__main__':
    d=getwd()
    d.get_wd(device_name='28-0416a253caff')
