import os
import json
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_continuous_delivery.cd_toolchain_v2 import CdToolchainV2

class ToolchainCreator:

  def __init__(self):
    self.name = "pipeline-alex"
    self.description = "this is some test"
    self.resource_group_id = "c40fa924adbe4a7a9bb978b1f9305dcc"
    self.cd_toolchain_v2 = CdToolchainV2()

  def cd_toolchain_create(self):

    try:
      response = self.cd_toolchain_v2.create_toolchain(
          description = self.description,
          name = self.name,
          resource_group_id = self.resource_group_id
      )
      toolchain_post = response.get_result()
      print(json.dumps(toolchain_post, indent=2))

    except ApiException as e:
            print("Exception when calling CdToolchainV2.create_toolchain: %s\n" % e)


if __name__ == '__main__':
  toolchain_creator = ToolchainCreator()
  toolchain_creator.cd_toolchain_create()

