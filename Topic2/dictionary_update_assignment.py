"""
Program: dictionary_update_assignment.py
Author: Alex Heinrichs
Last date modified: 10/16/2022

Write a function get_test_scores()
Create an empty dictionary scores_dict = dict()
Prompt the user to input the number of test scores, store in num_scores
Write a loop to get each of the num_scores test scores
Prompt the user to input each test score and store in score. (Validate the input!)
Add score to scores_dict  # HINT: update the dictionary
Write a second function average_scores() that accepts the dictionary as the only parameter and returns the average scores
Use len() to determine your num_scores for calculation
Note a dictionary is a set of key, value pairs.
You can get the keys with .keys() function
You can access the value using a key variable scores_dict.get(k)
What about testing?
Write a main to test your functions
Unit Tests can also help test average_scores()
"""


def get_test_scores():
    """
    Asks user for number of input and then stores each input in a dictionary
    :return: A dict of inputted scores
    """
    scores_dict = dict()
    num_scores = int(input("Enter number of scores you'd like to input: "))
    for num in range(num_scores):
        temp_score = 'Score ' + str(num + 1)
        try:
            temp_input = int(input("Enter score " + str(num + 1) + ": "))
            scores_dict.update({temp_score: temp_input})
        except ValueError:
            print('invalid input (must be int)')
    return scores_dict


def average_scores(input_dict):
    """
    Averages the scores of a dictionary input
    :param input_dict: dictionary to be inputted
    :return: an int of the average
    """
    try:
        num_scores = len(input_dict)
        total_value = 0
        for key, value in input_dict.items():
            total_value += value
        return total_value / num_scores
    except Exception:
        raise ValueError


if __name__ == "__main__":
    user_dict = get_test_scores()
    print(user_dict)
    print("The average score of the inputs are " + str(average_scores(user_dict)))
