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

from .proxy_only_resource import ProxyOnlyResource


class AppServiceCertificatePatchResource(ProxyOnlyResource):
    """Key Vault container ARM resource for a certificate that is purchased
    through Azure.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param key_vault_id: Key Vault resource Id.
    :type key_vault_id: str
    :param key_vault_secret_name: Key Vault secret name.
    :type key_vault_secret_name: str
    :ivar provisioning_state: Status of the Key Vault secret. Possible values
     include: 'Initialized', 'WaitingOnCertificateOrder', 'Succeeded',
     'CertificateOrderFailed', 'OperationNotPermittedOnKeyVault',
     'AzureServiceUnauthorizedToAccessKeyVault', 'KeyVaultDoesNotExist',
     'KeyVaultSecretDoesNotExist', 'UnknownError', 'ExternalPrivateKey',
     'Unknown'
    :vartype provisioning_state: str or
     ~azure.mgmt.web.models.KeyVaultSecretStatus
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'key_vault_id': {'key': 'properties.keyVaultId', 'type': 'str'},
        'key_vault_secret_name': {'key': 'properties.keyVaultSecretName', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'KeyVaultSecretStatus'},
    }

    def __init__(self, kind=None, key_vault_id=None, key_vault_secret_name=None):
        super(AppServiceCertificatePatchResource, self).__init__(kind=kind)
        self.key_vault_id = key_vault_id
        self.key_vault_secret_name = key_vault_secret_name
        self.provisioning_state = None
