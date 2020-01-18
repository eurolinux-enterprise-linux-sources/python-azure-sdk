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


class WebServiceProperties(Model):
    """The set of properties specific to the Azure ML web service resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param title: The title of the web service.
    :type title: str
    :param description: The description of the web service.
    :type description: str
    :ivar created_on: Read Only: The date and time when the web service was
     created.
    :vartype created_on: datetime
    :ivar modified_on: Read Only: The date and time when the web service was
     last modified.
    :vartype modified_on: datetime
    :ivar provisioning_state: Read Only: The provision state of the web
     service. Valid values are Unknown, Provisioning, Succeeded, and Failed.
     Possible values include: 'Unknown', 'Provisioning', 'Succeeded', 'Failed'
    :vartype provisioning_state: str or :class:`ProvisioningState
     <azure.mgmt.machinelearning.models.ProvisioningState>`
    :param keys: Contains the web service provisioning keys. If you do not
     specify provisioning keys, the Azure Machine Learning system generates
     them for you. Note: The keys are not returned from calls to GET
     operations.
    :type keys: :class:`WebServiceKeys
     <azure.mgmt.machinelearning.models.WebServiceKeys>`
    :param read_only: When set to true, indicates that the web service is
     read-only and can no longer be updated or patched, only removed. Default,
     is false. Note: Once set to true, you cannot change its value.
    :type read_only: bool
    :ivar swagger_location: Read Only: Contains the URI of the swagger spec
     associated with this web service.
    :vartype swagger_location: str
    :param expose_sample_data: When set to true, sample data is included in
     the web service's swagger definition. The default value is true.
    :type expose_sample_data: bool
    :param realtime_configuration: Contains the configuration settings for the
     web service endpoint.
    :type realtime_configuration: :class:`RealtimeConfiguration
     <azure.mgmt.machinelearning.models.RealtimeConfiguration>`
    :param diagnostics: Settings controlling the diagnostics traces collection
     for the web service.
    :type diagnostics: :class:`DiagnosticsConfiguration
     <azure.mgmt.machinelearning.models.DiagnosticsConfiguration>`
    :param storage_account: Specifies the storage account that Azure Machine
     Learning uses to store information about the web service. Only the name of
     the storage account is returned from calls to GET operations. When
     updating the storage account information, you must ensure that all
     necessary assets are available in the new storage account or calls to your
     web service will fail.
    :type storage_account: :class:`StorageAccount
     <azure.mgmt.machinelearning.models.StorageAccount>`
    :param machine_learning_workspace: Specifies the Machine Learning
     workspace containing the experiment that is source for the web service.
    :type machine_learning_workspace: :class:`MachineLearningWorkspace
     <azure.mgmt.machinelearning.models.MachineLearningWorkspace>`
    :param commitment_plan: Contains the commitment plan associated with this
     web service. Set at creation time. Once set, this value cannot be changed.
     Note: The commitment plan is not returned from calls to GET operations.
    :type commitment_plan: :class:`CommitmentPlan
     <azure.mgmt.machinelearning.models.CommitmentPlan>`
    :param input: Contains the Swagger 2.0 schema describing one or more of
     the web service's inputs. For more information, see the Swagger
     specification.
    :type input: :class:`ServiceInputOutputSpecification
     <azure.mgmt.machinelearning.models.ServiceInputOutputSpecification>`
    :param output: Contains the Swagger 2.0 schema describing one or more of
     the web service's outputs. For more information, see the Swagger
     specification.
    :type output: :class:`ServiceInputOutputSpecification
     <azure.mgmt.machinelearning.models.ServiceInputOutputSpecification>`
    :param example_request: Defines sample input data for one or more of the
     service's inputs.
    :type example_request: :class:`ExampleRequest
     <azure.mgmt.machinelearning.models.ExampleRequest>`
    :param assets: Contains user defined properties describing web service
     assets. Properties are expressed as Key/Value pairs.
    :type assets: dict
    :param parameters: The set of global parameters values defined for the web
     service, given as a global parameter name to default value map. If no
     default value is specified, the parameter is considered to be required.
    :type parameters: dict
    :param package_type: Polymorphic Discriminator
    :type package_type: str
    """

    _validation = {
        'created_on': {'readonly': True},
        'modified_on': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'swagger_location': {'readonly': True},
        'package_type': {'required': True},
    }

    _attribute_map = {
        'title': {'key': 'title', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'keys': {'key': 'keys', 'type': 'WebServiceKeys'},
        'read_only': {'key': 'readOnly', 'type': 'bool'},
        'swagger_location': {'key': 'swaggerLocation', 'type': 'str'},
        'expose_sample_data': {'key': 'exposeSampleData', 'type': 'bool'},
        'realtime_configuration': {'key': 'realtimeConfiguration', 'type': 'RealtimeConfiguration'},
        'diagnostics': {'key': 'diagnostics', 'type': 'DiagnosticsConfiguration'},
        'storage_account': {'key': 'storageAccount', 'type': 'StorageAccount'},
        'machine_learning_workspace': {'key': 'machineLearningWorkspace', 'type': 'MachineLearningWorkspace'},
        'commitment_plan': {'key': 'commitmentPlan', 'type': 'CommitmentPlan'},
        'input': {'key': 'input', 'type': 'ServiceInputOutputSpecification'},
        'output': {'key': 'output', 'type': 'ServiceInputOutputSpecification'},
        'example_request': {'key': 'exampleRequest', 'type': 'ExampleRequest'},
        'assets': {'key': 'assets', 'type': '{AssetItem}'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'package_type': {'key': 'packageType', 'type': 'str'},
    }

    _subtype_map = {
        'package_type': {'Graph': 'WebServicePropertiesForGraph'}
    }

    def __init__(self, title=None, description=None, keys=None, read_only=None, expose_sample_data=None, realtime_configuration=None, diagnostics=None, storage_account=None, machine_learning_workspace=None, commitment_plan=None, input=None, output=None, example_request=None, assets=None, parameters=None):
        self.title = title
        self.description = description
        self.created_on = None
        self.modified_on = None
        self.provisioning_state = None
        self.keys = keys
        self.read_only = read_only
        self.swagger_location = None
        self.expose_sample_data = expose_sample_data
        self.realtime_configuration = realtime_configuration
        self.diagnostics = diagnostics
        self.storage_account = storage_account
        self.machine_learning_workspace = machine_learning_workspace
        self.commitment_plan = commitment_plan
        self.input = input
        self.output = output
        self.example_request = example_request
        self.assets = assets
        self.parameters = parameters
        self.package_type = None
