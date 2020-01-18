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


class GalleryArtifactSource(Model):
    """The source of the gallery artifact.

    :param managed_image:
    :type managed_image:
     ~azure.mgmt.compute.v2018_06_01.models.ManagedArtifact
    """

    _attribute_map = {
        'managed_image': {'key': 'managedImage', 'type': 'ManagedArtifact'},
    }

    def __init__(self, **kwargs):
        super(GalleryArtifactSource, self).__init__(**kwargs)
        self.managed_image = kwargs.get('managed_image', None)
