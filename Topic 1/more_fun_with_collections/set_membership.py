"""
Program: set_membership.py
Author: Alex Heinrichs
Last date modified: 10/16/2022

Contains a function in_set() that accepts a set and a value and
returns a boolean values stating if the element is in the set.
Contains a main function that initializes a test set and a test value,
calls in_set() and print a message
"""


def in_set(param_set, param_value):
    """
    Accepts a set and a value and tests if value is within set
    :param param_set: set to be tested for
    :param param_value: value to test if within the set
    :return: boolean value of if param_value is in param_set
    """
    return param_value in param_set


if __name__ == "__main__":
    user_set = {'banana', 'apple', 'cherry'}
    test_value_1 = 'apple'
    test_value_2 = '5'
    if in_set(user_set, test_value_1):
        print("The value '" + test_value_1 + "' is in the set " + str(user_set))
    else:
        print("The value '" + test_value_1 + "' is not in the set " + str(user_set))
    if in_set(user_set, test_value_2):
        print("The value '" + test_value_2 + "' is in the set " + str(user_set))
    else:
        print("The value '" + test_value_2 + "' is not in the set " + str(user_set))
