# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OutputFileBlobContainerDestination(Model):
    """Specifies a file upload destination within an Azure blob storage container.

    :param path: The destination blob or virtual directory within the Azure
     Storage container. If filePattern refers to a specific file (i.e. contains
     no wildcards), then path is the name of the blob to which to upload that
     file. If filePattern contains one or more wildcards (and therefore may
     match multiple files), then path is the name of the blob virtual directory
     (which is prepended to each blob name) to which to upload the file(s). If
     omitted, file(s) are uploaded to the root of the container with a blob
     name matching their file name.
    :type path: str
    :param container_url: The URL of the container within Azure Blob Storage
     to which to upload the file(s). The URL must include a Shared Access
     Signature (SAS) granting write permissions to the container.
    :type container_url: str
    """

    _validation = {
        'container_url': {'required': True},
    }

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'container_url': {'key': 'containerUrl', 'type': 'str'},
    }

    def __init__(self, container_url, path=None):
        self.path = path
        self.container_url = container_url
