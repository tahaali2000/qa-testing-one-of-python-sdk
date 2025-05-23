# -*- coding: utf-8 -*-

"""
sampleapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from sampleapi.api_helper import APIHelper


class Pricing5(object):

    """Implementation of the 'Pricing5' model.

    Attributes:
        service_charge (float): The model property of type float.
        description (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "service_charge": 'serviceCharge',
        "description": 'description'
    }

    _optionals = [
        'service_charge',
        'description',
    ]

    def __init__(self,
                 service_charge=APIHelper.SKIP,
                 description=APIHelper.SKIP):
        """Constructor for the Pricing5 class"""

        # Initialize members of the class
        if service_charge is not APIHelper.SKIP:
            self.service_charge = service_charge 
        if description is not APIHelper.SKIP:
            self.description = description 

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
        service_charge = dictionary.get("serviceCharge") if dictionary.get("serviceCharge") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        # Return an object of this model
        return cls(service_charge,
                   description)

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
                f'service_charge={(self.service_charge if hasattr(self, "service_charge") else None)!r}, '
                f'description={(self.description if hasattr(self, "description") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'service_charge={(self.service_charge if hasattr(self, "service_charge") else None)!s}, '
                f'description={(self.description if hasattr(self, "description") else None)!s})')
