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

from .resource import Resource


class HybridConnection(Resource):
    """Description of hybrid connection resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar created_at: The time the hybrid connection was created.
    :vartype created_at: datetime
    :ivar updated_at: The time the namespace was updated.
    :vartype updated_at: datetime
    :ivar listener_count: The number of listeners for this hybrid connection.
     Note that min : 1 and max:25 are supported.
    :vartype listener_count: int
    :param requires_client_authorization: Returns true if client authorization
     is needed for this hybrid connection; otherwise, false.
    :type requires_client_authorization: bool
    :param user_metadata: The usermetadata is a placeholder to store
     user-defined string data for the hybrid connection endpoint. For example,
     it can be used to store descriptive data, such as a list of teams and
     their contact information. Also, user-defined configuration settings can
     be stored.
    :type user_metadata: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'created_at': {'readonly': True},
        'updated_at': {'readonly': True},
        'listener_count': {'readonly': True, 'maximum': 25, 'minimum': 0},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
        'updated_at': {'key': 'properties.updatedAt', 'type': 'iso-8601'},
        'listener_count': {'key': 'properties.listenerCount', 'type': 'int'},
        'requires_client_authorization': {'key': 'properties.requiresClientAuthorization', 'type': 'bool'},
        'user_metadata': {'key': 'properties.userMetadata', 'type': 'str'},
    }

    def __init__(self, requires_client_authorization=None, user_metadata=None):
        super(HybridConnection, self).__init__()
        self.created_at = None
        self.updated_at = None
        self.listener_count = None
        self.requires_client_authorization = requires_client_authorization
        self.user_metadata = user_metadata
