import connexion
import six

from swagger_server.models.server_addr import ServerAddr  # noqa: E501
from swagger_server import util


def client_obtain_ip():  # noqa: E501
    """obtain iperf server ip list to connect to

    Return servers ip list # noqa: E501


    :rtype: List[ServerAddr]
    """
    return 'do some magic!'
