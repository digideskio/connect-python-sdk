# coding: utf-8

"""
Copyright 2016 Square, Inc.

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


class ListTransactionsRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, begin_time=None, end_time=None, sort_order=None, cursor=None):
        """
        ListTransactionsRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'begin_time': 'str',
            'end_time': 'str',
            'sort_order': 'str',
            'cursor': 'str'
        }

        self.attribute_map = {
            'begin_time': 'begin_time',
            'end_time': 'end_time',
            'sort_order': 'sort_order',
            'cursor': 'cursor'
        }

        self._begin_time = begin_time
        self._end_time = end_time
        self._sort_order = sort_order
        self._cursor = cursor

    @property
    def begin_time(self):
        """
        Gets the begin_time of this ListTransactionsRequest.
        The beginning of the requested reporting period, in RFC 3339 format.

        :return: The begin_time of this ListTransactionsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """
        Sets the begin_time of this ListTransactionsRequest.
        The beginning of the requested reporting period, in RFC 3339 format.

        :param begin_time: The begin_time of this ListTransactionsRequest.
        :type: str
        """

        self._begin_time = begin_time

    @property
    def end_time(self):
        """
        Gets the end_time of this ListTransactionsRequest.
        The end of the requested reporting period, in RFC 3339 format.

        :return: The end_time of this ListTransactionsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this ListTransactionsRequest.
        The end of the requested reporting period, in RFC 3339 format.

        :param end_time: The end_time of this ListTransactionsRequest.
        :type: str
        """

        self._end_time = end_time

    @property
    def sort_order(self):
        """
        Gets the sort_order of this ListTransactionsRequest.
        The order in which results are listed in the response (`ASC` for chronological, `DESC` for reverse-chronological).

        :return: The sort_order of this ListTransactionsRequest.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """
        Sets the sort_order of this ListTransactionsRequest.
        The order in which results are listed in the response (`ASC` for chronological, `DESC` for reverse-chronological).

        :param sort_order: The sort_order of this ListTransactionsRequest.
        :type: str
        """
        allowed_values = ["DESC", "ASC"]
        if sort_order not in allowed_values:
            raise ValueError(
                "Invalid value for `sort_order` ({0}), must be one of {1}"
                .format(sort_order, allowed_values)
            )

        self._sort_order = sort_order

    @property
    def cursor(self):
        """
        Gets the cursor of this ListTransactionsRequest.
        A pagination cursor to retrieve the next set of results for your original query to the endpoint.

        :return: The cursor of this ListTransactionsRequest.
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """
        Sets the cursor of this ListTransactionsRequest.
        A pagination cursor to retrieve the next set of results for your original query to the endpoint.

        :param cursor: The cursor of this ListTransactionsRequest.
        :type: str
        """

        self._cursor = cursor

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
