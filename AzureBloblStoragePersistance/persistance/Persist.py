import os
import uuid

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


class Persist:
    def __init__(self, function):
        self.function = function

    def __call__(self, file):
        self.function(file)
        print("Uploading file to Azure Blob storage v" + __version__)

        try:
            file_path = file.name
            file_name = os.path.basename(file_path)

            connection_str = os.environ['AZURE_CONNECTION_STRING']

            blob_service_client = BlobServiceClient.from_connection_string(connection_str)

            container_name = str(uuid.uuid4())

            container_client = blob_service_client.create_container(container_name)

            blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

            print("\nUploading to Azure Storage as blob:\n\t" + file_name)

            # Upload the created file
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data)

        except Exception as ex:
            print('Exception:')
            print(ex)

