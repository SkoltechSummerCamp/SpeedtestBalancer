from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: server_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ServerApi(swagger_client.ApiClient(configuration))

try:
    # optain server IP
    api_response = api_instance.get_ip()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_ip: %s\n" % e)