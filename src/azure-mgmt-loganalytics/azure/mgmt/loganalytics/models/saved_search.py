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


class SavedSearch(Model):
    """Value object for saved search results.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The id of the saved search.
    :vartype id: str
    :ivar name: The name of the saved search.
    :vartype name: str
    :ivar type: The type of the saved search.
    :vartype type: str
    :param e_tag: The etag of the saved search.
    :type e_tag: str
    :param category: Required. The category of the saved search. This helps
     the user to find a saved search faster.
    :type category: str
    :param display_name: Required. Saved search display name.
    :type display_name: str
    :param query: Required. The query expression for the saved search. Please
     see
     https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-search-reference
     for reference.
    :type query: str
    :param version: Required. The version number of the query lanuage. Only
     verion 1 is allowed here.
    :type version: long
    :param tags: The tags attached to the saved search.
    :type tags: list[~azure.mgmt.loganalytics.models.Tag]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'category': {'required': True},
        'display_name': {'required': True},
        'query': {'required': True},
        'version': {'required': True, 'maximum': 1, 'minimum': 1},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'category': {'key': 'properties.category', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'query': {'key': 'properties.query', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'long'},
        'tags': {'key': 'properties.tags', 'type': '[Tag]'},
    }

    def __init__(self, **kwargs):
        super(SavedSearch, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.e_tag = kwargs.get('e_tag', None)
        self.category = kwargs.get('category', None)
        self.display_name = kwargs.get('display_name', None)
        self.query = kwargs.get('query', None)
        self.version = kwargs.get('version', None)
        self.tags = kwargs.get('tags', None)
