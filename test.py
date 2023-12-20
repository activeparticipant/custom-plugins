from ibm_continuous_delivery.cd_toolchain_v2 import CdToolchainV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import requests

authenticator = IAMAuthenticator('XXX')
service = CdToolchainV2(authenticator=authenticator)
responce = requests.get('https://api.us-south.devops.cloud.ibm.com/toolchain/v2')
responce.json()
