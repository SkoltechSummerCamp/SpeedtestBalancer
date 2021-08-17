import connexion
import six

from swagger_server.models.results import Results  # noqa: E501
from swagger_server import util

from flask import request


ip_dict = {}


def do_action():  # noqa: E501
    """send server ip to server

     # noqa: E501



    :rtype: None
    """
    remoteIP = request.remote_addr;
    remotePort = request.environ.get('REMOTE_PORT')
    
    ip_dict[remoteIP] = True;
    return remoteIP;


def get_results():  # noqa: E501
    """optain server IP

    Multiple status values can be provided with comma separated strings # noqa: E501


    :rtype: List[Results]
    """
    for ip in ip_dict:
        if ip_dict[ip] == True:
            ip_dict[ip] = False;
            print(type(ip))
            print(ip)
            return [{'ipv4': ip}]
    return 'no servers', 405
