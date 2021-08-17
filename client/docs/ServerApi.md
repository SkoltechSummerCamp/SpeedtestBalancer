# swagger_client.ServerApi

All URIs are relative to *https://localhost/Skoltech_OpenRAN_5G/iperf_load_balancer/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**server_delete_ip**](ServerApi.md#server_delete_ip) | **DELETE** /addr | delete server IP
[**server_post_ip**](ServerApi.md#server_post_ip) | **POST** /addr | post self ip to balancer

# **server_delete_ip**
> list[ServerAddr] server_delete_ip()

delete server IP

Send by server during shutdown

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()

try:
    # delete server IP
    api_response = api_instance.server_delete_ip()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->server_delete_ip: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ServerAddr]**](ServerAddr.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/Json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_post_ip**
> server_post_ip(body=body)

post self ip to balancer

When server makes free, post ip to balancer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
body = swagger_client.ServerAddr() # ServerAddr | port of iperf server. Ip and time could be emply (optional)

try:
    # post self ip to balancer
    api_instance.server_post_ip(body=body)
except ApiException as e:
    print("Exception when calling ServerApi->server_post_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServerAddr**](ServerAddr.md)| port of iperf server. Ip and time could be emply | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

