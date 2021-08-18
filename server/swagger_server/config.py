from swagger_server.models.server_addr import ServerAddr  # noqa: E501
from swagger_server import util

from datetime import datetime


class ServerDict:
    serverdict = {}
    
    def ServerDict_add(self, body):
        if body.time > datetime.now():
            raise Exception("invalid time")
        self.serverdict[(body.ip, body.port)] = body.time
    
    def ServerDict_get(self):
        return self.serverdict.popitem()


ServerDictInst = ServerDict()