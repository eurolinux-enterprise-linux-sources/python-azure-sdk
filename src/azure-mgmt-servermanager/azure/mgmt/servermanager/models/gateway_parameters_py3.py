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


class GatewayParameters(Model):
    """Collection of parameters for operations on a gateway resource.

    :param location: Location of the resource.
    :type location: str
    :param tags: Resource tags.
    :type tags: object
    :param upgrade_mode: The upgradeMode property gives the flexibility to
     gateway to auto upgrade itself. If properties value not specified, then we
     assume upgradeMode = Automatic. Possible values include: 'Manual',
     'Automatic'
    :type upgrade_mode: str or ~azure.mgmt.servermanager.models.UpgradeMode
    """

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'object'},
        'upgrade_mode': {'key': 'properties.upgradeMode', 'type': 'UpgradeMode'},
    }

    def __init__(self, *, location: str=None, tags=None, upgrade_mode=None, **kwargs) -> None:
        super(GatewayParameters, self).__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.upgrade_mode = upgrade_mode
