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


class ResourceSkuRestrictions(Model):
    """Describes scaling information of a SKU.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: The type of restrictions. Possible values include: 'Location',
     'Zone'
    :vartype type: str or
     ~azure.mgmt.compute.v2017_09_01.models.ResourceSkuRestrictionsType
    :ivar values: The value of restrictions. If the restriction type is set to
     location. This would be different locations where the SKU is restricted.
    :vartype values: list[str]
    :ivar restriction_info: The information about the restriction where the
     SKU cannot be used.
    :vartype restriction_info:
     ~azure.mgmt.compute.v2017_09_01.models.ResourceSkuRestrictionInfo
    :ivar reason_code: The reason for restriction. Possible values include:
     'QuotaId', 'NotAvailableForSubscription'
    :vartype reason_code: str or
     ~azure.mgmt.compute.v2017_09_01.models.ResourceSkuRestrictionsReasonCode
    """

    _validation = {
        'type': {'readonly': True},
        'values': {'readonly': True},
        'restriction_info': {'readonly': True},
        'reason_code': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'ResourceSkuRestrictionsType'},
        'values': {'key': 'values', 'type': '[str]'},
        'restriction_info': {'key': 'restrictionInfo', 'type': 'ResourceSkuRestrictionInfo'},
        'reason_code': {'key': 'reasonCode', 'type': 'ResourceSkuRestrictionsReasonCode'},
    }

    def __init__(self, **kwargs) -> None:
        super(ResourceSkuRestrictions, self).__init__(**kwargs)
        self.type = None
        self.values = None
        self.restriction_info = None
        self.reason_code = None
