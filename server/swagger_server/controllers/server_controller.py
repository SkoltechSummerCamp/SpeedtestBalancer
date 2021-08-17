import connexion
import six

from swagger_server.models.server_addr import ServerAddr  # noqa: E501
from swagger_server import util

from datetime import *



def server_delete_ip():  # noqa: E501
    """delete server IP

    Send by server during shutdown # noqa: E501


    :rtype: List[ServerAddr]
    """
    return 'do some magic!'


def server_post_ip(body=None):  # noqa: E501
    """post self ip to balancer

    When server makes free, post ip to balancer # noqa: E501

    :param body: port of iperf server. Ip and time could be emply
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ServerAddr.from_dict(connexion.request.get_json())  # noqa: E501
        print(type(body.ip))
        print(type(body.time))
        if body.ip is None:
            body.ip = connexion.request.remote_addr
        if body.time is None:
            body.time = datetime.now()
        print(body)
    return {}, 201
