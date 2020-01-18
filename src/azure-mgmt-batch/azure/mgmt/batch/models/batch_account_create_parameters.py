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


class BatchAccountCreateParameters(Model):
    """Parameters supplied to the Create operation.

    :param location: The region in which to create the account.
    :type location: str
    :param tags: The user-specified tags associated with the account.
    :type tags: dict
    :param auto_storage: The properties related to the auto-storage account.
    :type auto_storage: :class:`AutoStorageBaseProperties
     <azure.mgmt.batch.models.AutoStorageBaseProperties>`
    :param pool_allocation_mode: The allocation mode to use for creating pools
     in the Batch account. The pool allocation mode also affects how clients
     may authenticate to the Batch Service API. If the mode is BatchService,
     clients may authenticate using access keys or Azure Active Directory. If
     the mode is UserSubscription, clients must use Azure Active Directory. The
     default is BatchService. Possible values include: 'BatchService',
     'UserSubscription'
    :type pool_allocation_mode: str or :class:`PoolAllocationMode
     <azure.mgmt.batch.models.PoolAllocationMode>`
    :param key_vault_reference: A reference to the Azure key vault associated
     with the Batch account.
    :type key_vault_reference: :class:`KeyVaultReference
     <azure.mgmt.batch.models.KeyVaultReference>`
    """

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'auto_storage': {'key': 'properties.autoStorage', 'type': 'AutoStorageBaseProperties'},
        'pool_allocation_mode': {'key': 'properties.poolAllocationMode', 'type': 'PoolAllocationMode'},
        'key_vault_reference': {'key': 'properties.keyVaultReference', 'type': 'KeyVaultReference'},
    }

    def __init__(self, location, tags=None, auto_storage=None, pool_allocation_mode=None, key_vault_reference=None):
        self.location = location
        self.tags = tags
        self.auto_storage = auto_storage
        self.pool_allocation_mode = pool_allocation_mode
        self.key_vault_reference = key_vault_reference
