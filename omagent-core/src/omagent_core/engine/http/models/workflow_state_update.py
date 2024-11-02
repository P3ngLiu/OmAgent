import pprint
import re  # noqa: F401

import six

from omagent_core.engine.http.models import TaskResult


class WorkflowStateUpdate(object):
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
        'task_reference_name': 'str',
        'task_result': 'TaskResult',
        'variables': 'dict(str, object)'
    }

    attribute_map = {
        'task_reference_name': 'taskReferenceName',
        'task_result': 'taskResult',
        'variables': 'variables'
    }

    def __init__(self, task_reference_name: str = None, task_result: TaskResult = None,
                 variables: dict[str, object] = None):  # noqa: E501
        """WorkflowStateUpdate - a model defined in Swagger"""  # noqa: E501
        self._task_reference_name = None
        self._task_result = None
        self._variables = None
        if task_reference_name is not None:
            self.task_reference_name = task_reference_name
        if task_result is not None:
            self.task_result = task_result
        if variables is not None:
            self.variables = variables

    @property
    def task_reference_name(self) -> str:
        """Gets the task_reference_name of this WorkflowStateUpdate.  # noqa: E501


        :return: The task_reference_name of this WorkflowStateUpdate.  # noqa: E501
        :rtype: str
        """
        return self._task_reference_name

    @task_reference_name.setter
    def task_reference_name(self, task_reference_name: str):
        """Sets the task_reference_name of this WorkflowStateUpdate.


        :param task_reference_name: The task_reference_name of this WorkflowStateUpdate.  # noqa: E501
        :type: str
        """

        self._task_reference_name = task_reference_name

    @property
    def task_result(self) -> TaskResult:
        """Gets the task_result of this WorkflowStateUpdate.  # noqa: E501


        :return: The task_result of this WorkflowStateUpdate.  # noqa: E501
        :rtype: TaskResult
        """
        return self._task_result

    @task_result.setter
    def task_result(self, task_result: TaskResult):
        """Sets the task_result of this WorkflowStateUpdate.


        :param task_result: The task_result of this WorkflowStateUpdate.  # noqa: E501
        :type: TaskResult
        """

        self._task_result = task_result

    @property
    def variables(self) -> dict[str, object]:
        """Gets the variables of this WorkflowStateUpdate.  # noqa: E501


        :return: The variables of this WorkflowStateUpdate.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._variables

    @variables.setter
    def variables(self, variables: dict[str, object]):
        """Sets the variables of this WorkflowStateUpdate.


        :param variables: The variables of this WorkflowStateUpdate.  # noqa: E501
        :type: dict(str, object)
        """

        self._variables = variables

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
        if issubclass(WorkflowStateUpdate, dict):
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
        if not isinstance(other, WorkflowStateUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
