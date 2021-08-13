from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()

try:
    # optain server IP
    api_response = api_instance.get_results()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_results: %s\n" % e)