# coding: utf-8

"""
    Square Connect API


    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Error(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, category=None, code=None, detail=None, field=None):
        """
        Error - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'category': 'str',
            'code': 'str',
            'detail': 'str',
            'field': 'str'
        }

        self.attribute_map = {
            'category': 'category',
            'code': 'code',
            'detail': 'detail',
            'field': 'field'
        }

        self._category = category
        self._code = code
        self._detail = detail
        self._field = field

    @property
    def category(self):
        """
        Gets the category of this Error.
        

        :return: The category of this Error.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this Error.
        

        :param category: The category of this Error.
        :type: str
        """
        allowed_values = ["API_ERROR", "AUTHENTICATION_ERROR", "INVALID_REQUEST_ERROR", "RATE_LIMIT_ERROR", "PAYMENT_METHOD_ERROR", "REFUND_ERROR"]
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def code(self):
        """
        Gets the code of this Error.
        

        :return: The code of this Error.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Error.
        

        :param code: The code of this Error.
        :type: str
        """
        allowed_values = ["INTERNAL_SERVER_ERROR", "UNAUTHORIZED", "ACCESS_TOKEN_EXPIRED", "ACCESS_TOKEN_REVOKED", "FORBIDDEN", "INSUFFICIENT_SCOPES", "APPLICATION_DISABLED", "V1_APPLICATION", "V1_ACCESS_TOKEN", "CARD_PROCESSING_NOT_ENABLED", "BAD_REQUEST", "MISSING_REQUIRED_PARAMETER", "INCORRECT_TYPE", "INVALID_TIME", "INVALID_TIME_RANGE", "INVALID_VALUE", "INVALID_CURSOR", "UNKNOWN_QUERY_PARAMETER", "CONFLICTING_PARAMETERS", "EXPECTED_JSON_BODY", "INVALID_SORT_ORDER", "VALUE_TOO_LONG", "VALUE_TOO_LOW", "EXPECTED_BOOLEAN", "EXPECTED_INTEGER", "EXPECTED_FLOAT", "EXPECTED_STRING", "EXPECTED_OBJECT", "EXPECTED_ARRAY", "INVALID_ARRAY_VALUE", "INVALID_ENUM_VALUE", "INVALID_CONTENT_TYPE", "INVALID_FORM_VALUE", "ONE_INSTRUMENT_EXPECTED", "NO_FIELDS_SET", "CARD_DECLINED", "CARD_EXPIRED", "VERIFY_CVV_FAILURE", "VERIFY_AVS_FAILURE", "INVALID_EXPIRATION", "INVALID_EXPIRATION_YEAR", "INVALID_EXPIRATION_DATE", "INVALID_CARD", "DELAYED_TRANSACTION_EXPIRED", "DELAYED_TRANSACTION_CANCELED", "DELAYED_TRANSACTION_CAPTURED", "DELAYED_TRANSACTION_FAILED", "CARD_TOKEN_EXPIRED", "CARD_TOKEN_USED", "AMOUNT_TOO_HIGH", "UNSUPPORTED_INSTRUMENT_TYPE", "REFUND_AMOUNT_INVALID", "REFUND_ALREADY_PENDING", "PAYMENT_NOT_REFUNDABLE", "INVALID_CARD_DATA", "NOT_FOUND", "REQUEST_TIMEOUT", "REQUEST_ENTITY_TOO_LARGE", "UNSUPPORTED_MEDIA_TYPE", "RATE_LIMITED", "NOT_IMPLEMENTED", "SERVICE_UNAVAILABLE"]
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def detail(self):
        """
        Gets the detail of this Error.
        

        :return: The detail of this Error.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """
        Sets the detail of this Error.
        

        :param detail: The detail of this Error.
        :type: str
        """

        self._detail = detail

    @property
    def field(self):
        """
        Gets the field of this Error.
        

        :return: The field of this Error.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this Error.
        

        :param field: The field of this Error.
        :type: str
        """

        self._field = field

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other