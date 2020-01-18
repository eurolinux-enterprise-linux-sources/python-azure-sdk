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


class RepositoryCredential(Model):
    """Credential information to connect to container repository.

    :param repository_user_name: The user name to connect to container
     repository.
    :type repository_user_name: str
    :param repository_password: The password for supplied username to connect
     to container repository.
    :type repository_password: str
    :param password_encrypted: Indicates that supplied container repository
     password is encrypted.
    :type password_encrypted: bool
    """ 

    _attribute_map = {
        'repository_user_name': {'key': 'RepositoryUserName', 'type': 'str'},
        'repository_password': {'key': 'RepositoryPassword', 'type': 'str'},
        'password_encrypted': {'key': 'PasswordEncrypted', 'type': 'bool'},
    }

    def __init__(self, repository_user_name=None, repository_password=None, password_encrypted=None):
        self.repository_user_name = repository_user_name
        self.repository_password = repository_password
        self.password_encrypted = password_encrypted
