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


class AutomationRunbookReceiver(Model):
    """The Azure Automation Runbook notification receiver.

    All required parameters must be populated in order to send to Azure.

    :param automation_account_id: Required. The Azure automation account Id
     which holds this runbook and authenticate to Azure resource.
    :type automation_account_id: str
    :param runbook_name: Required. The name for this runbook.
    :type runbook_name: str
    :param webhook_resource_id: Required. The resource id for webhook linked
     to this runbook.
    :type webhook_resource_id: str
    :param is_global_runbook: Required. Indicates whether this instance is
     global runbook.
    :type is_global_runbook: bool
    :param name: Indicates name of the webhook.
    :type name: str
    :param service_uri: The URI where webhooks should be sent.
    :type service_uri: str
    """

    _validation = {
        'automation_account_id': {'required': True},
        'runbook_name': {'required': True},
        'webhook_resource_id': {'required': True},
        'is_global_runbook': {'required': True},
    }

    _attribute_map = {
        'automation_account_id': {'key': 'automationAccountId', 'type': 'str'},
        'runbook_name': {'key': 'runbookName', 'type': 'str'},
        'webhook_resource_id': {'key': 'webhookResourceId', 'type': 'str'},
        'is_global_runbook': {'key': 'isGlobalRunbook', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'service_uri': {'key': 'serviceUri', 'type': 'str'},
    }

    def __init__(self, *, automation_account_id: str, runbook_name: str, webhook_resource_id: str, is_global_runbook: bool, name: str=None, service_uri: str=None, **kwargs) -> None:
        super(AutomationRunbookReceiver, self).__init__(**kwargs)
        self.automation_account_id = automation_account_id
        self.runbook_name = runbook_name
        self.webhook_resource_id = webhook_resource_id
        self.is_global_runbook = is_global_runbook
        self.name = name
        self.service_uri = service_uri
