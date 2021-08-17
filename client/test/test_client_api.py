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
from swagger_client.api.client_api import ClientApi  # noqa: E501
from swagger_client.rest import ApiException


class TestClientApi(unittest.TestCase):
    """ClientApi unit test stubs"""

    def setUp(self):
        self.api = ClientApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_client_optain_ip(self):
        """Test case for client_optain_ip

        optain iperf server ip list to connect to  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
