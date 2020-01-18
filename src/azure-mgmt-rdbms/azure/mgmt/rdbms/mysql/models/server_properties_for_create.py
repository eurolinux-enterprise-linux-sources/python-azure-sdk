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


class ServerPropertiesForCreate(Model):
    """The properties used to create a new server.

    :param storage_mb: The maximum storage allowed for a server.
    :type storage_mb: long
    :param version: Server version. Possible values include: '5.6', '5.7'
    :type version: str or :class:`ServerVersion
     <azure.mgmt.rdbms.mysql.models.ServerVersion>`
    :param ssl_enforcement: Enable ssl enforcement or not when connect to
     server. Possible values include: 'Enabled', 'Disabled'
    :type ssl_enforcement: str or :class:`SslEnforcementEnum
     <azure.mgmt.rdbms.mysql.models.SslEnforcementEnum>`
    :param create_mode: Polymorphic Discriminator
    :type create_mode: str
    """

    _validation = {
        'storage_mb': {'minimum': 1024},
        'create_mode': {'required': True},
    }

    _attribute_map = {
        'storage_mb': {'key': 'storageMB', 'type': 'long'},
        'version': {'key': 'version', 'type': 'str'},
        'ssl_enforcement': {'key': 'sslEnforcement', 'type': 'SslEnforcementEnum'},
        'create_mode': {'key': 'createMode', 'type': 'str'},
    }

    _subtype_map = {
        'create_mode': {'Default': 'ServerPropertiesForDefaultCreate', 'PointInTimeRestore': 'ServerPropertiesForRestore'}
    }

    def __init__(self, storage_mb=None, version=None, ssl_enforcement=None):
        self.storage_mb = storage_mb
        self.version = version
        self.ssl_enforcement = ssl_enforcement
        self.create_mode = None
