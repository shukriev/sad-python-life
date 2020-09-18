from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.resource import ResourceManagementClient


resource_client = get_client_from_cli_profile(ResourceManagementClient)

resource_client.resource_groups.delete("PythonAzureExample-Storage-rg")
