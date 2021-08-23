import connexion
import six

from swagger_server.models.server_addr import ServerAddr  # noqa: E501
from swagger_server import util

from ..config import *



def client_obtain_ip():  # noqa: E501
    """obtain iperf server ip list to connect to

    Return servers ip list # noqa: E501


    :rtype: List[ServerAddr]
    """
    try:
        ((ip, port), (time, port_iperf)) = ServerDictInst.get()
        return ServerAddr(ip=ip, port=port, port_iperf=port_iperf, time=time), 200
    except:
        return {}, 503
