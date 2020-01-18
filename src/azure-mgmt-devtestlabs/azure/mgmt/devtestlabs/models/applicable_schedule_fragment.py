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


class ApplicableScheduleFragment(Resource):
    """Schedules applicable to a virtual machine. The schedules may have been
    defined on a VM or on lab level.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The identifier of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict
    :param lab_vms_shutdown: The auto-shutdown schedule, if one has been set
     at the lab or lab resource level.
    :type lab_vms_shutdown: :class:`ScheduleFragment
     <azure.mgmt.devtestlabs.models.ScheduleFragment>`
    :param lab_vms_startup: The auto-startup schedule, if one has been set at
     the lab or lab resource level.
    :type lab_vms_startup: :class:`ScheduleFragment
     <azure.mgmt.devtestlabs.models.ScheduleFragment>`
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'lab_vms_shutdown': {'key': 'properties.labVmsShutdown', 'type': 'ScheduleFragment'},
        'lab_vms_startup': {'key': 'properties.labVmsStartup', 'type': 'ScheduleFragment'},
    }

    def __init__(self, location=None, tags=None, lab_vms_shutdown=None, lab_vms_startup=None):
        super(ApplicableScheduleFragment, self).__init__(location=location, tags=tags)
        self.lab_vms_shutdown = lab_vms_shutdown
        self.lab_vms_startup = lab_vms_startup
