from  ..script.reboot import  shutdown
from .authentication_cookie import cookie
from flask.views import MethodView

class Reboot(MethodView):
    @cookie
    def get(self):
        shutdown()
