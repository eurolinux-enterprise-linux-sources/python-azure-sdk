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


class ResourceGroup(Model):
    """Resource group information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The ID of the resource group.
    :vartype id: str
    :param name: The name of the resource group.
    :type name: str
    :param properties:
    :type properties:
     ~azure.mgmt.resource.resources.v2016_09_01.models.ResourceGroupProperties
    :param location: Required. The location of the resource group. It cannot
     be changed after the resource group has been created. It muct be one of
     the supported Azure locations.
    :type location: str
    :param managed_by: The ID of the resource that manages this resource
     group.
    :type managed_by: str
    :param tags: The tags attached to the resource group.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ResourceGroupProperties'},
        'location': {'key': 'location', 'type': 'str'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(ResourceGroup, self).__init__(**kwargs)
        self.id = None
        self.name = kwargs.get('name', None)
        self.properties = kwargs.get('properties', None)
        self.location = kwargs.get('location', None)
        self.managed_by = kwargs.get('managed_by', None)
        self.tags = kwargs.get('tags', None)
