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


class CreateManagementGroupChildInfo(Model):
    """The child information of a management group used during creation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: The type of child resource. The fully qualified resource type
     which includes provider namespace (e.g.
     /providers/Microsoft.Management/managementGroups). Possible values
     include: '/providers/Microsoft.Management/managementGroups',
     '/subscriptions'
    :vartype type: str or ~azure.mgmt.managementgroups.models.enum
    :ivar id: The fully qualified ID for the child resource (management group
     or subscription).  For example,
     /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
    :vartype id: str
    :ivar name: The name of the child entity.
    :vartype name: str
    :ivar display_name: The friendly name of the child resource.
    :vartype display_name: str
    :ivar roles: The roles definitions associated with the management group.
    :vartype roles: list[str]
    :ivar children: The list of children.
    :vartype children:
     list[~azure.mgmt.managementgroups.models.CreateManagementGroupChildInfo]
    """

    _validation = {
        'type': {'readonly': True},
        'id': {'readonly': True},
        'name': {'readonly': True},
        'display_name': {'readonly': True},
        'roles': {'readonly': True},
        'children': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'roles': {'key': 'roles', 'type': '[str]'},
        'children': {'key': 'children', 'type': '[CreateManagementGroupChildInfo]'},
    }

    def __init__(self, **kwargs) -> None:
        super(CreateManagementGroupChildInfo, self).__init__(**kwargs)
        self.type = None
        self.id = None
        self.name = None
        self.display_name = None
        self.roles = None
        self.children = None
