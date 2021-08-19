from swagger_server.models.server_addr import ServerAddr  # noqa: E501
from swagger_server import util

from datetime import datetime

import os


class ServerDict:
    serverdict = {}
    path_to_log = None
    log_file = None

    def __init__(self):
        self.path_to_log = os.environ.get("SERVERLOGPATH")
        if self.path_to_log is None:
            self.path_to_log = "../logs/log.txt"

        os.makedirs(os.path.dirname(self.path_to_log), exist_ok=True)
        self.log_file = open(self.path_to_log, 'a')
        self.log_file.write(datetime.now().strftime('%X %x %Z') + ' server started\n')
        self.log_file.flush()

# Found to open be deleted before __del__ being called
#     def __del__(self):
#         if self.log_file is not None:
#             self.log_file.close()

#         self.path_to_log = os.environ.get("SERVERLOGPATH")
#         if self.path_to_log is not None:
#             with open(self.path_to_log, 'a') as log:
#                 log.write(datetime.now().strftime('%X %x %Z') + ' server stopped\n')
# 
    
    def add(self, body):
        if body.time > datetime.now():
            raise Exception("invalid time")
        self.serverdict[(body.ip, body.port)] = body.time
        if self.log_file is not None:
            self.log_file.write(datetime.now().strftime('%X %x %Z') + ' add ' + body.ip + ':' + str(body.port) + ' ' + body.time.strftime('%X %x %Z') + '\n')
            self.log_file.flush()
    
    def get(self):
        body = self.serverdict.popitem()
        if self.log_file is not None:
            self.log_file.write(datetime.now().strftime('%X %x %Z') + ' send ' + body[0][0] + ':' + str(body[0][1]) + ' ' + body[1].strftime('%X %x %Z') + '\n')
            self.log_file.flush()
        return body

    def remove(self,body):
        if (body.ip, body.port) in self.serverdict:
            time = self.serverdict[(body.ip, body.port)]
            del self.serverdict[(body.ip, body.port)]
            if self.log_file is not None:
                self.log_file.write(datetime.now().strftime('%X %x %Z') + ' del ' + body.ip + ':' + str(body.port) + ' ' + time.strftime('%X %x %Z') + '\n')
                self.log_file.flush()
            return time
        raise Exception("no such server in dict")


ServerDictInst = ServerDict()