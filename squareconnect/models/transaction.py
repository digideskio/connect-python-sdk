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


class Transaction(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, location_id=None, created_at=None, tenders=None, refunds=None, reference_id=None, product=None):
        """
        Transaction - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'location_id': 'str',
            'created_at': 'str',
            'tenders': 'list[Tender]',
            'refunds': 'list[Refund]',
            'reference_id': 'str',
            'product': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'location_id': 'location_id',
            'created_at': 'created_at',
            'tenders': 'tenders',
            'refunds': 'refunds',
            'reference_id': 'reference_id',
            'product': 'product'
        }

        self._id = id
        self._location_id = location_id
        self._created_at = created_at
        self._tenders = tenders
        self._refunds = refunds
        self._reference_id = reference_id
        self._product = product

    @property
    def id(self):
        """
        Gets the id of this Transaction.
        The transaction's unique ID.

        :return: The id of this Transaction.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Transaction.
        The transaction's unique ID.

        :param id: The id of this Transaction.
        :type: str
        """

        self._id = id

    @property
    def location_id(self):
        """
        Gets the location_id of this Transaction.
        The ID of the transaction's associated location.

        :return: The location_id of this Transaction.
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """
        Sets the location_id of this Transaction.
        The ID of the transaction's associated location.

        :param location_id: The location_id of this Transaction.
        :type: str
        """

        self._location_id = location_id

    @property
    def created_at(self):
        """
        Gets the created_at of this Transaction.
        The time when the transaction was created, in RFC 3339 format.

        :return: The created_at of this Transaction.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Transaction.
        The time when the transaction was created, in RFC 3339 format.

        :param created_at: The created_at of this Transaction.
        :type: str
        """

        self._created_at = created_at

    @property
    def tenders(self):
        """
        Gets the tenders of this Transaction.
        Descriptions of the tenders used to pay for the transaction.

        :return: The tenders of this Transaction.
        :rtype: list[Tender]
        """
        return self._tenders

    @tenders.setter
    def tenders(self, tenders):
        """
        Sets the tenders of this Transaction.
        Descriptions of the tenders used to pay for the transaction.

        :param tenders: The tenders of this Transaction.
        :type: list[Tender]
        """

        self._tenders = tenders

    @property
    def refunds(self):
        """
        Gets the refunds of this Transaction.
        An array of any refunds associated with the transaction.

        :return: The refunds of this Transaction.
        :rtype: list[Refund]
        """
        return self._refunds

    @refunds.setter
    def refunds(self, refunds):
        """
        Sets the refunds of this Transaction.
        An array of any refunds associated with the transaction.

        :param refunds: The refunds of this Transaction.
        :type: list[Refund]
        """

        self._refunds = refunds

    @property
    def reference_id(self):
        """
        Gets the reference_id of this Transaction.
        If the transaction was created with the **Charge** endpoint, this value is the same as the value provided as the `reference_id` parameter in the request to that endpoint.

        :return: The reference_id of this Transaction.
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """
        Sets the reference_id of this Transaction.
        If the transaction was created with the **Charge** endpoint, this value is the same as the value provided as the `reference_id` parameter in the request to that endpoint.

        :param reference_id: The reference_id of this Transaction.
        :type: str
        """

        self._reference_id = reference_id

    @property
    def product(self):
        """
        Gets the product of this Transaction.
        The product that processed the transaction.

        :return: The product of this Transaction.
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this Transaction.
        The product that processed the transaction.

        :param product: The product of this Transaction.
        :type: str
        """
        allowed_values = ["REGISTER", "EXTERNAL_API", "BILLING", "APPOINTMENTS", "INVOICES", "ONLINE_STORE", "PAYROLL", "OTHER"]
        if product not in allowed_values:
            raise ValueError(
                "Invalid value for `product` ({0}), must be one of {1}"
                .format(product, allowed_values)
            )

        self._product = product

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