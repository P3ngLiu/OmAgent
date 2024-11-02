import pprint
import re  # noqa: F401

import six


class EventHandler(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'event': 'str',
        'condition': 'str',
        'actions': 'list[Action]',
        'active': 'bool',
        'evaluator_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'event': 'event',
        'condition': 'condition',
        'actions': 'actions',
        'active': 'active',
        'evaluator_type': 'evaluatorType'
    }

    def __init__(self, name=None, event=None, condition=None, actions=None, active=None,
                 evaluator_type=None):  # noqa: E501
        """EventHandler - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._event = None
        self._condition = None
        self._actions = None
        self._active = None
        self._evaluator_type = None
        self.discriminator = None
        self.name = name
        self.event = event
        if condition is not None:
            self.condition = condition
        self.actions = actions
        if active is not None:
            self.active = active
        if evaluator_type is not None:
            self.evaluator_type = evaluator_type

    @property
    def name(self):
        """Gets the name of this EventHandler.  # noqa: E501


        :return: The name of this EventHandler.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventHandler.


        :param name: The name of this EventHandler.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def event(self):
        """Gets the event of this EventHandler.  # noqa: E501


        :return: The event of this EventHandler.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this EventHandler.


        :param event: The event of this EventHandler.  # noqa: E501
        :type: str
        """
        self._event = event

    @property
    def condition(self):
        """Gets the condition of this EventHandler.  # noqa: E501


        :return: The condition of this EventHandler.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this EventHandler.


        :param condition: The condition of this EventHandler.  # noqa: E501
        :type: str
        """

        self._condition = condition

    @property
    def actions(self):
        """Gets the actions of this EventHandler.  # noqa: E501


        :return: The actions of this EventHandler.  # noqa: E501
        :rtype: list[Action]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this EventHandler.


        :param actions: The actions of this EventHandler.  # noqa: E501
        :type: list[Action]
        """
        self._actions = actions

    @property
    def active(self):
        """Gets the active of this EventHandler.  # noqa: E501


        :return: The active of this EventHandler.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this EventHandler.


        :param active: The active of this EventHandler.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def evaluator_type(self):
        """Gets the evaluator_type of this EventHandler.  # noqa: E501


        :return: The evaluator_type of this EventHandler.  # noqa: E501
        :rtype: str
        """
        return self._evaluator_type

    @evaluator_type.setter
    def evaluator_type(self, evaluator_type):
        """Sets the evaluator_type of this EventHandler.


        :param evaluator_type: The evaluator_type of this EventHandler.  # noqa: E501
        :type: str
        """

        self._evaluator_type = evaluator_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(EventHandler, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventHandler):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
