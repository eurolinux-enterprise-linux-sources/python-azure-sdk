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


class NetworkInterfaceAssociation(Model):
    """Network interface and its custom security rules.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Network interface ID.
    :vartype id: str
    :param security_rules: Collection of custom security rules.
    :type security_rules:
     list[~azure.mgmt.network.v2018_01_01.models.SecurityRule]
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'security_rules': {'key': 'securityRules', 'type': '[SecurityRule]'},
    }

    def __init__(self, *, security_rules=None, **kwargs) -> None:
        super(NetworkInterfaceAssociation, self).__init__(**kwargs)
        self.id = None
        self.security_rules = security_rules
