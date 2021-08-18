# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.server_addr import ServerAddr  # noqa: E501
from swagger_server.test import BaseTestCase


class TestServerController(BaseTestCase):
    """ServerController integration test stubs"""

    def test_server_delete_ip(self):
        """Test case for server_delete_ip

        delete server IP
        """
        response = self.client.open(
            '/Skoltech_OpenRAN_5G/iperf_load_balancer/0.0.1/addr',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_server_post_ip(self):
        """Test case for server_post_ip

        post self ip to balancer
        """
        body = ServerAddr()
        response = self.client.open(
            '/Skoltech_OpenRAN_5G/iperf_load_balancer/0.0.1/addr',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
