import pywifi,time
from pywifi import const
class Wifi():
    def __init__(self):
        wifi=pywifi.PyWiFi()
        self.interfice=wifi.interfaces()[0]
    def list_wifi(self):
        ssid=set()
        for i in self.interfice.scan_results():
            ssid.add(i.ssid)
        return list(ssid)
    def connect_wifi(self,ssid,password):
        self.interfice.disconnect()
        assert self.interfice.status() in [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE]
        wifi = pywifi.PyWiFi()
        interfice = wifi.interfaces()[0]
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password
        interfice.remove_all_network_profiles()
        tmp_profile = interfice.add_network_profile(profile)
        interfice.connect(tmp_profile)
        number=0
        while interfice.status() != const.IFACE_CONNECTED:
            time.sleep(2)
            if interfice.status() == const.IFACE_CONNECTED:
                return True
            else:
                print(number)
                number=number+1
                if number>=3:
                    print('connect error!')
                    break
        return False
if __name__ =='__main__':
    c=Wifi()
    print(c.list_wifi())
    print(c.connect_wifi('hpyy2floor','111222333W'))
    # print(interfice.status(),const.IFACE_CONNECTED)
