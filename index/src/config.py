import os
path=os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
config_file=os.path.join(path,'conifg.conf')


class Config:
    def config(self):
        config={}
        with open(config_file,'r') as f:
            for i in f.readlines():
                tmp_config=i.split(': ')
                config[tmp_config[0]]=tmp_config[1].split('\n')[0]
        return config
