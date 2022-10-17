"""
Program: test_average_scores.py
Author: Alex Heinrichs
Date Created: 10/16/2022

Contains a series of tests to ensure the average_scores
function works properly
"""

import unittest
from Topic2.dictionary_update_assignment import average_scores


class MyTestCase(unittest.TestCase):
    """
    Class for testing
    """
    def test_average(self):
        """Tests for average"""
        # Arrange
        self.scores_dict = {"Test 1": 31, "Test 2": 34, "Test 3": 54}
        expected = 39.66666666  # 7 decimal places, remove one and see the test fail
        # Act
        actual = average_scores(self.scores_dict)
        # Assert
        self.assertAlmostEqual(expected, actual)

    def test_average_five(self):
        """Tests for average with a 5 size dictionary"""
        # Arrange
        self.scores_dict = {"Test 1": 0, "Test 2": 43,
                            "Test 3": 64, "Test 4": 83, "Test 5": 99}
        expected = 57.8
        # Act
        actual = average_scores(self.scores_dict)
        # Assert
        self.assertAlmostEqual(expected, actual)

    def test_average_zero(self):
        """Tests for ValueError for a dictionary with zero size"""
        # Arrange
        self.scores_dict = {}
        # Assert
        with self.assertRaises(ValueError):
            average_scores(self.scores_dict)

    if __name__ == '__main__':
        test_average()
        test_average_five()
        test_average_zero()
