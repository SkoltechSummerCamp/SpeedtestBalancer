from swagger_server.models.server_addr import ServerAddr  # noqa: E501
from swagger_server import util

from datetime import datetime


class ServerDict:
    serverdict = {}
    
    def add(self, body):
        if body.time > datetime.now():
            raise Exception("invalid time")
        self.serverdict[(body.ip, body.port)] = body.time
    
    def get(self):
        return self.serverdict.popitem()

    def remove(self,body):
        if (body.ip, body.port) in self.serverdict:
            time = self.serverdict[(body.ip, body.port)]
            del self.serverdict[(body.ip, body.port)]
            return time
        raise Exception("no such server in dict")


ServerDictInst = ServerDict()