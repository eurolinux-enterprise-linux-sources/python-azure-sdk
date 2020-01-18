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


class StorageAccountCreateParameters(Model):
    """The parameters used when creating a storage account.

    :param sku: Required. Gets or sets the sku name.
    :type sku: :class:`Sku <azure.mgmt.storage.v2016_12_01.models.Sku>`
    :param kind: Required. Indicates the type of storage account. Possible
     values include: 'Storage', 'BlobStorage'
    :type kind: str or :class:`Kind
     <azure.mgmt.storage.v2016_12_01.models.Kind>`
    :param location: Required. Gets or sets the location of the resource. This
     will be one of the supported and registered Azure Geo Regions (e.g. West
     US, East US, Southeast Asia, etc.). The geo region of a resource cannot be
     changed once it is created, but if an identical geo region is specified on
     update, the request will succeed.
    :type location: str
    :param tags: Gets or sets a list of key value pairs that describe the
     resource. These tags can be used for viewing and grouping this resource
     (across resource groups). A maximum of 15 tags can be provided for a
     resource. Each tag must have a key with a length no greater than 128
     characters and a value with a length no greater than 256 characters.
    :type tags: dict
    :param custom_domain: User domain assigned to the storage account. Name is
     the CNAME source. Only one custom domain is supported per storage account
     at this time. To clear the existing custom domain, use an empty string for
     the custom domain name property.
    :type custom_domain: :class:`CustomDomain
     <azure.mgmt.storage.v2016_12_01.models.CustomDomain>`
    :param encryption: Provides the encryption settings on the account. If
     left unspecified the account encryption settings will remain the same. The
     default setting is unencrypted.
    :type encryption: :class:`Encryption
     <azure.mgmt.storage.v2016_12_01.models.Encryption>`
    :param access_tier: Required for storage accounts where kind =
     BlobStorage. The access tier used for billing. Possible values include:
     'Hot', 'Cool'
    :type access_tier: str or :class:`AccessTier
     <azure.mgmt.storage.v2016_12_01.models.AccessTier>`
    """

    _validation = {
        'sku': {'required': True},
        'kind': {'required': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'Sku'},
        'kind': {'key': 'kind', 'type': 'Kind'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'custom_domain': {'key': 'properties.customDomain', 'type': 'CustomDomain'},
        'encryption': {'key': 'properties.encryption', 'type': 'Encryption'},
        'access_tier': {'key': 'properties.accessTier', 'type': 'AccessTier'},
    }

    def __init__(self, sku, kind, location, tags=None, custom_domain=None, encryption=None, access_tier=None):
        self.sku = sku
        self.kind = kind
        self.location = location
        self.tags = tags
        self.custom_domain = custom_domain
        self.encryption = encryption
        self.access_tier = access_tier
