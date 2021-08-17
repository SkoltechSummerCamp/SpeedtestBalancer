import connexion
import six

from swagger_server.models.results import Results  # noqa: E501
from swagger_server import util

from flask import request

ip_dict = {}


def delete_ip():  # noqa: E501
    """delete server IP

    Send by server during shutdown # noqa: E501


    :rtype: List[Results]
    """
    return 'do some magic!'


def get_ip():  # noqa: E501
    """optain server IP

    Multiple status values can be provided with comma separated strings # noqa: E501


    :rtype: List[Results]
    """
    for ip in ip_dict:
        if ip_dict[ip] == True:
            ip_dict[ip] = False;
            [{'ipv4': ip[0]}, {'port': ip[1]}];
    return 'no servers', 503


def post_ip():  # noqa: E501
    """send server ip to balancer

     # noqa: E501


    :rtype: List[Results]
    """
    remoteIP = request.remote_addr;
    remotePort = request.environ.get('REMOTE_PORT')
    
    ip_dict[[remoteIP, remotePort]] = True;
    return [{'ipv4': remoteIP}, {'port': remotePort}];
