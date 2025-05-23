# -*- coding: utf-8 -*-

"""
sampleapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from sampleapi.api_helper import APIHelper


class Pricing6(object):

    """Implementation of the 'Pricing6' model.

    Attributes:
        installment (float): The model property of type float.
        payment_due (datetime): The model property of type datetime.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "installment": 'installment',
        "payment_due": 'paymentDue'
    }

    _optionals = [
        'installment',
        'payment_due',
    ]

    def __init__(self,
                 installment=APIHelper.SKIP,
                 payment_due=APIHelper.SKIP):
        """Constructor for the Pricing6 class"""

        # Initialize members of the class
        if installment is not APIHelper.SKIP:
            self.installment = installment 
        if payment_due is not APIHelper.SKIP:
            self.payment_due = APIHelper.apply_datetime_converter(payment_due, APIHelper.RFC3339DateTime) if payment_due else None 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        installment = dictionary.get("installment") if dictionary.get("installment") else APIHelper.SKIP
        payment_due = APIHelper.RFC3339DateTime.from_value(dictionary.get("paymentDue")).datetime if dictionary.get("paymentDue") else APIHelper.SKIP
        # Return an object of this model
        return cls(installment,
                   payment_due)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'installment={(self.installment if hasattr(self, "installment") else None)!r}, '
                f'payment_due={(self.payment_due if hasattr(self, "payment_due") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'installment={(self.installment if hasattr(self, "installment") else None)!s}, '
                f'payment_due={(self.payment_due if hasattr(self, "payment_due") else None)!s})')
