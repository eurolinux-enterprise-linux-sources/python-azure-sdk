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


class ValidateProbeOutput(Model):
    """Output of the validate probe API.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar is_valid: Indicates whether the probe URL is accepted or not.
    :vartype is_valid: bool
    :ivar error_code: Specifies the error code when the probe url is not
     accepted.
    :vartype error_code: str
    :ivar message: The detailed error message describing why the probe URL is
     not accepted.
    :vartype message: str
    """

    _validation = {
        'is_valid': {'readonly': True},
        'error_code': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'is_valid': {'key': 'isValid', 'type': 'bool'},
        'error_code': {'key': 'errorCode', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ValidateProbeOutput, self).__init__(**kwargs)
        self.is_valid = None
        self.error_code = None
        self.message = None
