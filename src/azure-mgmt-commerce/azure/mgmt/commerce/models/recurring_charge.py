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

from .offer_term_info import OfferTermInfo


class RecurringCharge(OfferTermInfo):
    """RecurringCharge.

    :param effective_date: Indicates the date from which the meter rate or
     offer term is effective.
    :type effective_date: datetime
    :param excluded_meter_ids: An array of meter ids that are excluded from
     the given offer terms.
    :type excluded_meter_ids: list of str
    :param Name: Polymorphic Discriminator
    :type Name: str
    :param recurring_charge: The amount of recurring charge as per the offer
     term.
    :type recurring_charge: int
    """ 

    _validation = {
        'Name': {'required': True},
    }

    _attribute_map = {
        'effective_date': {'key': 'EffectiveDate', 'type': 'iso-8601'},
        'excluded_meter_ids': {'key': 'ExcludedMeterIds', 'type': '[str]'},
        'Name': {'key': 'Name', 'type': 'str'},
        'recurring_charge': {'key': 'RecurringCharge', 'type': 'int'},
    }

    def __init__(self, effective_date=None, excluded_meter_ids=None, recurring_charge=None):
        super(RecurringCharge, self).__init__(effective_date=effective_date, excluded_meter_ids=excluded_meter_ids)
        self.recurring_charge = recurring_charge
        self.Name = 'Recurring Charge'
