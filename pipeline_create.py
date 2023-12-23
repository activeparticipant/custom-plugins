from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import json
import ibm_cloud_sdk_core
from ibm_continuous_delivery.cd_toolchain_v2 import CdToolchainV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

name = None
description = None
resource_group_id = None

def cd_toolchain_create():

  name = "pipeline-alex"
  description = "this is some test"
  resource_group_id = "c40fa924adbe4a7a9bb978b1f9305dcc"

  response = cd_toolchain_create.create_toolchain(
      description = description,
      name = name,
      resource_group_id = resource_group_id
  )

  toolchain_post = response.get_result()
  print(json.dumps(toolchain_post, indent=2))

if __name__ == '__main__':
    cd_toolchain_create()
