#from ibm_continuous_delivery.cd_toolchain_v2 import CdToolchainV2
#from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import requests
import json


url = "https://api.us-south.devops.cloud.ibm.com/toolchain/v2/toolchains"
data = {"name": "TestToolchainV2", "resource_group_id": "c40fa924adbe4a7a9bb978b1f9305dcc", "description": "this is test description"}
headers = {
  'Authorization': 'Bearer ' + authToken,
  'Content-Type': 'application/json'
}

# Convert to json
data_json = json.dumps(data)

resp = requests.post(url, headers=headers, data=data_json)
resp_json = resp.json()
print(resp_json)
