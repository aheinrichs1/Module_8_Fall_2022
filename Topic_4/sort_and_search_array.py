"""
Program: sort_and_search_array.py
Author: Alex Heinrichs
Date: 10/17/2022

Hard-code a list that is passed to the functions sort_array()
and search_array()
"""
import array as arr


def search_array(input_array, user_value):
    """Searches an array for a value and returns
    index or -1 if value is not found"""
    input_list = input_array.tolist()

    for index in range(len(input_list)):
        if user_value == input_array[index]:
            return index
    return -1  # if item is not found


def sort_array(input_array):
    """Sorts an array and returns it"""
    sorted_list = input_array.tolist()
    sorted_list.sort()
    sorted_array = arr.array('i', sorted_list)
    return sorted_array
    # return statement was needed because the array had to be
    # converted to a list and back to a new array


if __name__ == '__main__':
    user_array = arr.array('i', [1, 4, 2, 6, 3])
    print('Index of value 6')
    print(str(search_array(user_array, 6)))
    print('Unsorted Array:')
    print(str(user_array))
    print('Sorted Array:')
    user_array = sort_array(user_array)
    print(str(user_array))
    print('New index of value 6')
    print(str(search_array(user_array, 6)))
    print('-1 should be returned for int not in index:')
    print(str(search_array(user_array, 9)))

