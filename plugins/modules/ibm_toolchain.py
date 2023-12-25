#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: fcp.ibm_cloud_devops.toolchain

short_description: Interacts with IBM Cloud DevOps to create a toolchain.

version_added: "1.0.0"

description:
  - This module facilitates the creation of toolchains in IBM Cloud DevOps.
  - It allows you to define toolchain properties such as name, IAM API key, description, resource group ID, and DevOps service URL.

options:
  iam_api_key:
    description: IAM API key for authentication.
    required: true
    type: str
  name:
    description: Name of the toolchain to be created.
    required: true
    type: str
  description:
    description: Description of the toolchain (optional).
    required: false
    type: str
  resource_group_id:
    description: Resource group ID in the IBM Cloud DevOps portal.
    required: true
    type: str
  devops_service_url:
    description: Toolchain service URL.
    required: true
    type: str

extends_documentation_fragment:
  - fcp.ibm_cloud_devops.common_doc_fragment

author:
  - Alexander Zolotukhin (isaac_levitan@main.ru)
'''

EXAMPLE = r'''
---
- name: Create IBM DevOps Toolchain Pipeline
  fcp.ibm_cloud_devops.toolchain:
    name: my-password-toolchain
    iam_api_key: "{{ my_iam_api_key }}"
    resource_group_id: "my_resource_group_id"
    devops_service_url: "https://api.us-south.devops.cloud.ibm.com/toolchain/v2"
    description: "This is a custom toolchain for managing passwords"
'''

RETURN = r'''
# These are examples of possible return values. Use relevant names and descriptions for actual return values.
---
toolchain:
    description: Details of the created toolchain.
    type: dict
    returned: success
    sample:
        id: "toolchain_id"
        name: "my-password-toolchain"
        description: "This is a custom toolchain for managing passwords"
        resource_group_id: "my_resource_group_id"
        devops_service_url: "https://api.us-south.devops.cloud.ibm.com/toolchain/v2"

message:
    description: Message indicating the status of the toolchain creation.
    type: str
    returned: always
    sample: 'Toolchain created successfully.'

error_message:
    description: Error message if toolchain creation fails.
    type: str
    returned: failure
    sample: 'Failed to create the toolchain. Check the parameters and try again.'
'''

import json
from ibm_cloud_sdk_core import ApiException
from ibm_continuous_delivery.cd_toolchain_v2 import CdToolchainV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ansible.module_utils.basic import AnsibleModule

def run_module():
  moduleArgs = {
    "iam_api_key": {"type": str, "required": True},
    "name": {"type": str, "required": True},
    "resource_group_id": {"type": str, "required": True},
    "devops_service_url": {"type": str, "required": True},
    "description": {"type": str, "required": False},
    }

  result = {
        'changed': False,
        'original_message':'',
        'message':''
    }

  module = AnsibleModule(argument_spec=moduleArgs, supports_check_mode=False)
  result = cd_toolchain_create(module)
  if result["status"] == -1:
      module.fail_json(msg=result["status_message"], **result)

  module.exit_json(**result)

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

def main():
  run_module()

if __name__ == '__main__':
  main()

