import json
from ibm_cloud_sdk_core import ApiException
from ibm_continuous_delivery.cd_toolchain_v2 import CdToolchainV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = r'''
---

module: ibm_toolchain

short_description: This module interacts with IBM cloud devops creating a toolchain

version: "1.0.0"

description:
options:
  iam_api_key:
    description: IAM api key
    requeired: true
    type: str
  name:
    description: toolchain name
    required: true
    type: str
  description:
    description: The description of the toochain
    required: false
    type: str
  resource_group_id:
    description: resource group id in ibm cloud devops portal
    required: true
    type: str
  devops_service_url:
    description: toolchain service url
    required: true
    type: str
'''

EXAMPLE = r'''

- name: Create ibm devops toolchain pipeline
  fcp.plugins.ibm_toolchain:
    name: password-rotation
    iam_api_key: "{iam_api_key}"
    resource_group_id: "989hfewiu329834f"
    devops_service_url: "https://api.us-south.devops.cloud.ibm.com/toolchain/v2"
    description: "This is a test toolchain"

'''

class ToolchainCreator:

  def run_module():
    moduleArgs = {
      "iam_api_key": {"type": str, "required": True},
      "name": {"type": str, "required": True},
      "resource_group_id": {"type": str, "required": True},
      "devops_service_url": {"type": str, "required": True},
      "description": {"type": str, "required": True},
     }
    module = AnsibleModule(argument_spec=moduleArgs, supports_check_mode=False)
    result = ToolchainCreator.cd_toolchain_create(module)
    if result["status"] == -1:
        module.fail_json(msg=result["status_message"], **result)

    module.exit_json(**result)

  def __init__(self):

    self.name = "pipeline-alex-4"
    self.description = "this is some test"
    self.resource_group_id = "c40fa924adbe4a7a9bb978b1f9305dcc"
    self.iam_api_key = "{iam_api_key}"
    self.iam_auth = IAMAuthenticator(apikey=self.iam_api_key)
    self.cd_toolchain_v2 = CdToolchainV2(authenticator=self.iam_auth)
    self.devops_service_url = "https://api.us-south.devops.cloud.ibm.com/toolchain/v2"

  def cd_toolchain_create(self):

    try:
      service = self.cd_toolchain_v2
      service.set_service_url(self.devops_service_url)


      response = self.cd_toolchain_v2.create_toolchain(
          description = self.description,
          name = self.name,
          resource_group_id = self.resource_group_id
      )
      toolchain_post = response.get_result()
      print(json.dumps(toolchain_post, indent=2))

    except ApiException as e:
            print("Exception when calling ToolchainCreator.cd_create_toolchain: %s\n" % e)


if __name__ == '__main__':
  toolchain_creator = ToolchainCreator()
  toolchain_creator.cd_toolchain_create()

