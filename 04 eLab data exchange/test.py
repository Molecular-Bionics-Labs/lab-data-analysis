import time
import datetime
import elabapi_python
from elabapi_python.rest import ApiException

#########################
#         CONFIG        #
#########################
API_HOST_URL = 'https://demo.elabftw.net/api/v2'
# replace with your api key
API_KEY = 'ypur key goes here'
#########################
#      END CONFIG       #
#########################

# Configure the api client
configuration = elabapi_python.Configuration()
configuration.api_key['api_key'] = API_KEY
configuration.api_key_prefix['api_key'] = 'Authorization'
configuration.host = API_HOST_URL
configuration.debug = False
configuration.verify_ssl = False

# create an instance of the API class
api_client = elabapi_python.ApiClient(configuration)
# fix issue with Authorization header not being properly set by the generated lib
api_client.set_default_header(header_name='Authorization', header_value=API_KEY)

# Load items api
itemsApi = elabapi_python.ItemsApi(api_client)
itemId = 180
itemsApi.patch_item(itemId, body={'title': 'The new title', 'body': 'Main content text', 'rating': 5})