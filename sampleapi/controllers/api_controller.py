# -*- coding: utf-8 -*-

"""
sampleapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from sampleapi.api_helper import APIHelper
from sampleapi.configuration import Server
from sampleapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from sampleapi.http.http_method_enum import HttpMethodEnum
from sampleapi.models.items_response import ItemsResponse


class APIController(BaseController):

    """A Controller to access Endpoints in the sampleapi API."""
    def __init__(self, config):
        super(APIController, self).__init__(config)

    def get_a_list_of_items(self):
        """Does a GET request to /items.

        Returns:
            ItemsResponse: Response from the API. A list of items

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/items')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ItemsResponse.from_dictionary)
        ).execute()

    def create_a_new_item(self,
                          body):
        """Does a POST request to /items.

        Args:
            body (ItemsRequest): The request body parameter.

        Returns:
            void: Response from the API. Item created successfully

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/items')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .body_serializer(APIHelper.json_serialize)
        ).execute()
