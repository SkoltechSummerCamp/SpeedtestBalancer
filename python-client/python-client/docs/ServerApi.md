# swagger_client.ServerApi

All URIs are relative to *https://localhost/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**do_action**](ServerApi.md#do_action) | **POST** /server | send server ip to server
[**get_results**](ServerApi.md#get_results) | **GET** /server | optain server IP


# **do_action**
> do_action()

send server ip to server



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
    # send server ip to server
    api_instance.do_action()
except ApiException as e:
    print("Exception when calling ServerApi->do_action: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_results**
> list[Results] get_results()

optain server IP

Multiple status values can be provided with comma separated strings

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
    # optain server IP
    api_response = api_instance.get_results()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_results: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Results]**](Results.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

