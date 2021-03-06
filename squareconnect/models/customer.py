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


class Customer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, created_at=None, updated_at=None, cards=None, given_name=None, family_name=None, nickname=None, company_name=None, email_address=None, address=None, phone_number=None, reference_id=None, note=None):
        """
        Customer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'created_at': 'str',
            'updated_at': 'str',
            'cards': 'list[Card]',
            'given_name': 'str',
            'family_name': 'str',
            'nickname': 'str',
            'company_name': 'str',
            'email_address': 'str',
            'address': 'Address',
            'phone_number': 'str',
            'reference_id': 'str',
            'note': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'cards': 'cards',
            'given_name': 'given_name',
            'family_name': 'family_name',
            'nickname': 'nickname',
            'company_name': 'company_name',
            'email_address': 'email_address',
            'address': 'address',
            'phone_number': 'phone_number',
            'reference_id': 'reference_id',
            'note': 'note'
        }

        self._id = id
        self._created_at = created_at
        self._updated_at = updated_at
        self._cards = cards
        self._given_name = given_name
        self._family_name = family_name
        self._nickname = nickname
        self._company_name = company_name
        self._email_address = email_address
        self._address = address
        self._phone_number = phone_number
        self._reference_id = reference_id
        self._note = note

    @property
    def id(self):
        """
        Gets the id of this Customer.
        The customer's unique ID.

        :return: The id of this Customer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Customer.
        The customer's unique ID.

        :param id: The id of this Customer.
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this Customer.
        The time when the customer was created, in RFC 3339 format.

        :return: The created_at of this Customer.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Customer.
        The time when the customer was created, in RFC 3339 format.

        :param created_at: The created_at of this Customer.
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Customer.
        The time when the customer was updated, in RFC 3339 format.

        :return: The updated_at of this Customer.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Customer.
        The time when the customer was updated, in RFC 3339 format.

        :param updated_at: The updated_at of this Customer.
        :type: str
        """

        self._updated_at = updated_at

    @property
    def cards(self):
        """
        Gets the cards of this Customer.
        Cards on file for the customer.

        :return: The cards of this Customer.
        :rtype: list[Card]
        """
        return self._cards

    @cards.setter
    def cards(self, cards):
        """
        Sets the cards of this Customer.
        Cards on file for the customer.

        :param cards: The cards of this Customer.
        :type: list[Card]
        """

        self._cards = cards

    @property
    def given_name(self):
        """
        Gets the given_name of this Customer.
        

        :return: The given_name of this Customer.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """
        Sets the given_name of this Customer.
        

        :param given_name: The given_name of this Customer.
        :type: str
        """

        self._given_name = given_name

    @property
    def family_name(self):
        """
        Gets the family_name of this Customer.
        

        :return: The family_name of this Customer.
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """
        Sets the family_name of this Customer.
        

        :param family_name: The family_name of this Customer.
        :type: str
        """

        self._family_name = family_name

    @property
    def nickname(self):
        """
        Gets the nickname of this Customer.
        

        :return: The nickname of this Customer.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """
        Sets the nickname of this Customer.
        

        :param nickname: The nickname of this Customer.
        :type: str
        """

        self._nickname = nickname

    @property
    def company_name(self):
        """
        Gets the company_name of this Customer.
        

        :return: The company_name of this Customer.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this Customer.
        

        :param company_name: The company_name of this Customer.
        :type: str
        """

        self._company_name = company_name

    @property
    def email_address(self):
        """
        Gets the email_address of this Customer.
        

        :return: The email_address of this Customer.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this Customer.
        

        :param email_address: The email_address of this Customer.
        :type: str
        """

        self._email_address = email_address

    @property
    def address(self):
        """
        Gets the address of this Customer.
        

        :return: The address of this Customer.
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Customer.
        

        :param address: The address of this Customer.
        :type: Address
        """

        self._address = address

    @property
    def phone_number(self):
        """
        Gets the phone_number of this Customer.
        

        :return: The phone_number of this Customer.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this Customer.
        

        :param phone_number: The phone_number of this Customer.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def reference_id(self):
        """
        Gets the reference_id of this Customer.
        

        :return: The reference_id of this Customer.
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """
        Sets the reference_id of this Customer.
        

        :param reference_id: The reference_id of this Customer.
        :type: str
        """

        self._reference_id = reference_id

    @property
    def note(self):
        """
        Gets the note of this Customer.
        

        :return: The note of this Customer.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this Customer.
        

        :param note: The note of this Customer.
        :type: str
        """

        self._note = note

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
