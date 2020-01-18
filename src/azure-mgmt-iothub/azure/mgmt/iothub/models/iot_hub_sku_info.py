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


class IotHubSkuInfo(Model):
    """Information about the SKU of the IoT hub.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the SKU. Possible values include: 'F1',
     'S1', 'S2', 'S3', 'B1', 'B2', 'B3'
    :type name: str or ~azure.mgmt.iothub.models.IotHubSku
    :ivar tier: The billing tier for the IoT hub. Possible values include:
     'Free', 'Standard', 'Basic'
    :vartype tier: str or ~azure.mgmt.iothub.models.IotHubSkuTier
    :param capacity: The number of provisioned IoT Hub units. See:
     https://docs.microsoft.com/azure/azure-subscription-service-limits#iot-hub-limits.
    :type capacity: long
    """

    _validation = {
        'name': {'required': True},
        'tier': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'IotHubSkuTier'},
        'capacity': {'key': 'capacity', 'type': 'long'},
    }

    def __init__(self, **kwargs):
        super(IotHubSkuInfo, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.tier = None
        self.capacity = kwargs.get('capacity', None)
