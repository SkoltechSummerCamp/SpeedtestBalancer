# swagger_client.ServerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ip**](ServerApi.md#delete_ip) | **DELETE** /server | delete server IP
[**get_ip**](ServerApi.md#get_ip) | **GET** /server | optain server IP
[**post_ip**](ServerApi.md#post_ip) | **POST** /server | send server ip to balancer


# **delete_ip**
> list[Results] delete_ip()

delete server IP

Send by server during shutdown

### Example
```python
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
    # delete server IP
    api_response = api_instance.delete_ip()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->delete_ip: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Results]**](Results.md)

### Authorization

[server_auth](../README.md#server_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/Json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip**
> list[Results] get_ip()

optain server IP

Multiple status values can be provided with comma separated strings

### Example
```python
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
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Results]**](Results.md)

### Authorization

[server_auth](../README.md#server_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ip**
> list[Results] post_ip()

send server ip to balancer



### Example
```python
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
    # send server ip to balancer
    api_response = api_instance.post_ip()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->post_ip: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Results]**](Results.md)

### Authorization

[server_auth](../README.md#server_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

