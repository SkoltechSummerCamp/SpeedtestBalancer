# coding: utf-8

"""
    Balancer

    Simple iperf load balancer  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    Contact: vinogradov.alek@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.server_api import ServerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestServerApi(unittest.TestCase):
    """ServerApi unit test stubs"""

    def setUp(self):
        self.api = ServerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_server_delete_ip(self):
        """Test case for server_delete_ip

        delete server IP  # noqa: E501
        """
        pass

    def test_server_post_ip(self):
        """Test case for server_post_ip

        post self ip to balancer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
