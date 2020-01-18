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


class SearchSort(Model):
    """The sort parameters for search.

    :param name: The name of the field the search query is sorted on.
    :type name: str
    :param order: The sort order of the search. Possible values include:
     'asc', 'desc'
    :type order: str or ~azure.mgmt.loganalytics.models.SearchSortEnum
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'order': {'key': 'order', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SearchSort, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.order = kwargs.get('order', None)
