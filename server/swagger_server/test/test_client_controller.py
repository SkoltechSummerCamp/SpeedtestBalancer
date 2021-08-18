# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.server_addr import ServerAddr  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClientController(BaseTestCase):
    """ClientController integration test stubs"""

    def test_client_optain_ip(self):
        """Test case for client_optain_ip

        optain iperf server ip list to connect to
        """
        response = self.client.open(
            '/Skoltech_OpenRAN_5G/iperf_load_balancer/0.0.1/addr',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
