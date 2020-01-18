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


class Sku(Model):
    """Sku for the resource.

    :param name: The sku name.
    :type name: str
    :param tier: The sku tier.
    :type tier: str
    :param size: The sku size.
    :type size: str
    :param family: The sku family.
    :type family: str
    :param model: The sku model.
    :type model: str
    :param capacity: The sku capacity.
    :type capacity: int
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'size': {'key': 'size', 'type': 'str'},
        'family': {'key': 'family', 'type': 'str'},
        'model': {'key': 'model', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(self, name=None, tier=None, size=None, family=None, model=None, capacity=None):
        self.name = name
        self.tier = tier
        self.size = size
        self.family = family
        self.model = model
        self.capacity = capacity
