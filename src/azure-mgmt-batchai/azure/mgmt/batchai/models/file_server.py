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

from .proxy_resource import ProxyResource


class FileServer(ProxyResource):
    """Contains information about the File Server.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The ID of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param vm_size: The size of the virtual machine of the File Server. For
     information about available VM sizes for File Server from the Virtual
     Machines Marketplace, see Sizes for Virtual Machines (Linux).
    :type vm_size: str
    :param ssh_configuration: SSH settings for the File Server.
    :type ssh_configuration: ~azure.mgmt.batchai.models.SshConfiguration
    :param data_disks: Settings for the data disk which would be created for
     the File Server.
    :type data_disks: ~azure.mgmt.batchai.models.DataDisks
    :param subnet: Specifies the identifier of the subnet.
    :type subnet: ~azure.mgmt.batchai.models.ResourceId
    :ivar mount_settings: Details of the File Server.
    :vartype mount_settings: ~azure.mgmt.batchai.models.MountSettings
    :ivar provisioning_state_transition_time: Time when the status was
     changed.
    :vartype provisioning_state_transition_time: datetime
    :ivar creation_time: Time when the FileServer was created.
    :vartype creation_time: datetime
    :ivar provisioning_state: Specifies the provisioning state of the File
     Server. Possible values: creating - The File Server is getting created.
     updating - The File Server creation has been accepted and it is getting
     updated. deleting - The user has requested that the File Server be
     deleted, and it is in the process of being deleted. failed - The File
     Server creation has failed with the specified errorCode. Details about the
     error code are specified in the message field. succeeded - The File Server
     creation has succeeded. Possible values include: 'creating', 'updating',
     'deleting', 'succeeded', 'failed'
    :vartype provisioning_state: str or
     ~azure.mgmt.batchai.models.FileServerProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'mount_settings': {'readonly': True},
        'provisioning_state_transition_time': {'readonly': True},
        'creation_time': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'vm_size': {'key': 'properties.vmSize', 'type': 'str'},
        'ssh_configuration': {'key': 'properties.sshConfiguration', 'type': 'SshConfiguration'},
        'data_disks': {'key': 'properties.dataDisks', 'type': 'DataDisks'},
        'subnet': {'key': 'properties.subnet', 'type': 'ResourceId'},
        'mount_settings': {'key': 'properties.mountSettings', 'type': 'MountSettings'},
        'provisioning_state_transition_time': {'key': 'properties.provisioningStateTransitionTime', 'type': 'iso-8601'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(FileServer, self).__init__(**kwargs)
        self.vm_size = kwargs.get('vm_size', None)
        self.ssh_configuration = kwargs.get('ssh_configuration', None)
        self.data_disks = kwargs.get('data_disks', None)
        self.subnet = kwargs.get('subnet', None)
        self.mount_settings = None
        self.provisioning_state_transition_time = None
        self.creation_time = None
        self.provisioning_state = None
