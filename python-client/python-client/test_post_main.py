from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()

try:
    # send server ip to server
    api_instance.do_action()
except ApiException as e:
    print("Exception when calling ServerApi->do_action: %s\n" % e)