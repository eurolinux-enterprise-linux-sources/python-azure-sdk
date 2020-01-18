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


class WorkflowRunTrigger(Model):
    """The workflow run trigger.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Gets the name.
    :vartype name: str
    :ivar inputs: Gets the inputs.
    :vartype inputs: object
    :ivar inputs_link: Gets the link to inputs.
    :vartype inputs_link: :class:`ContentLink
     <azure.mgmt.logic.models.ContentLink>`
    :ivar outputs: Gets the outputs.
    :vartype outputs: object
    :ivar outputs_link: Gets the link to outputs.
    :vartype outputs_link: :class:`ContentLink
     <azure.mgmt.logic.models.ContentLink>`
    :ivar start_time: Gets the start time.
    :vartype start_time: datetime
    :ivar end_time: Gets the end time.
    :vartype end_time: datetime
    :ivar tracking_id: Gets the tracking id.
    :vartype tracking_id: str
    :param correlation: The run correlation.
    :type correlation: :class:`Correlation
     <azure.mgmt.logic.models.Correlation>`
    :ivar code: Gets the code.
    :vartype code: str
    :ivar status: Gets the status. Possible values include: 'NotSpecified',
     'Paused', 'Running', 'Waiting', 'Succeeded', 'Skipped', 'Suspended',
     'Cancelled', 'Failed', 'Faulted', 'TimedOut', 'Aborted', 'Ignored'
    :vartype status: str or :class:`WorkflowStatus
     <azure.mgmt.logic.models.WorkflowStatus>`
    :ivar error: Gets the error.
    :vartype error: object
    :ivar tracked_properties: Gets the tracked properties.
    :vartype tracked_properties: object
    """

    _validation = {
        'name': {'readonly': True},
        'inputs': {'readonly': True},
        'inputs_link': {'readonly': True},
        'outputs': {'readonly': True},
        'outputs_link': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'tracking_id': {'readonly': True},
        'code': {'readonly': True},
        'status': {'readonly': True},
        'error': {'readonly': True},
        'tracked_properties': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': 'object'},
        'inputs_link': {'key': 'inputsLink', 'type': 'ContentLink'},
        'outputs': {'key': 'outputs', 'type': 'object'},
        'outputs_link': {'key': 'outputsLink', 'type': 'ContentLink'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'tracking_id': {'key': 'trackingId', 'type': 'str'},
        'correlation': {'key': 'correlation', 'type': 'Correlation'},
        'code': {'key': 'code', 'type': 'str'},
        'status': {'key': 'status', 'type': 'WorkflowStatus'},
        'error': {'key': 'error', 'type': 'object'},
        'tracked_properties': {'key': 'trackedProperties', 'type': 'object'},
    }

    def __init__(self, correlation=None):
        self.name = None
        self.inputs = None
        self.inputs_link = None
        self.outputs = None
        self.outputs_link = None
        self.start_time = None
        self.end_time = None
        self.tracking_id = None
        self.correlation = correlation
        self.code = None
        self.status = None
        self.error = None
        self.tracked_properties = None
