from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

try:
    from ibm_cloud_sdk_core import get_authenticator_from_environment
    from ibm_cloud_sdk_core.authenticators import Authenticator, IAMAuthenticator
    from ibm_platform_services import ResourceControllerV2
except ImportError:
    raise


RESOURCE_CONTROLLER_SERVICE_NAME = 'resource_controller'


def get_authenticator(service_name: str) -> Authenticator:
    """Create and return an authenticator instance.

    1. Try to create an authenticator based on the service name and the environment variables
    2. If that wasn't successful try to get the `IC_API_KEY` from the environment and create an IAM authenticator
    3. If all the above have failed, return None.

    Args:
        service_name (str): name of the service

    Returns:
        Authenticator: the created authenticator or None
    """
    authenticator = get_authenticator_from_environment(service_name=service_name)
    if authenticator is None:
        apikey = os.getenv('IC_API_KEY', None)
        if apikey is None:
            return None

        authenticator = IAMAuthenticator(apikey=apikey)

    return authenticator