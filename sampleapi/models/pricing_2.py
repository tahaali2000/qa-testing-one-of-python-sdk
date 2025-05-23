# -*- coding: utf-8 -*-

"""
sampleapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from sampleapi.api_helper import APIHelper


class Pricing2(object):

    """Implementation of the 'Pricing2' model.

    Attributes:
        tax (float): The model property of type float.
        tax_rate (float): The model property of type float.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tax": 'tax',
        "tax_rate": 'taxRate'
    }

    _optionals = [
        'tax',
        'tax_rate',
    ]

    def __init__(self,
                 tax=APIHelper.SKIP,
                 tax_rate=APIHelper.SKIP):
        """Constructor for the Pricing2 class"""

        # Initialize members of the class
        if tax is not APIHelper.SKIP:
            self.tax = tax 
        if tax_rate is not APIHelper.SKIP:
            self.tax_rate = tax_rate 

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
        tax = dictionary.get("tax") if dictionary.get("tax") else APIHelper.SKIP
        tax_rate = dictionary.get("taxRate") if dictionary.get("taxRate") else APIHelper.SKIP
        # Return an object of this model
        return cls(tax,
                   tax_rate)

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
                f'tax={(self.tax if hasattr(self, "tax") else None)!r}, '
                f'tax_rate={(self.tax_rate if hasattr(self, "tax_rate") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'tax={(self.tax if hasattr(self, "tax") else None)!s}, '
                f'tax_rate={(self.tax_rate if hasattr(self, "tax_rate") else None)!s})')
