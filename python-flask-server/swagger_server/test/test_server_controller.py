# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.results import Results  # noqa: E501
from swagger_server.test import BaseTestCase


class TestServerController(BaseTestCase):
    """ServerController integration test stubs"""

    def test_delete_ip(self):
        """Test case for delete_ip

        delete server IP
        """
        response = self.client.open(
            '//server',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ip(self):
        """Test case for get_ip

        optain server IP
        """
        response = self.client.open(
            '//server',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_ip(self):
        """Test case for post_ip

        send server ip to balancer
        """
        response = self.client.open(
            '//server',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
