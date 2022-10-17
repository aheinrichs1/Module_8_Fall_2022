"""
Program: assign_level.py
Author: Alex Heinrichs
Last Date Modified: 10/17/2022

Implement a switch/case with a dictionary.
You will assign points for attaining a level in a video game.
Levels are named N (for novice), B (for beginner), E (for experienced)
and A (for advanced). For novice, 50 points is assigned
to get the player started. For attaining beginner, 150 points are received.
Experienced players receive 300 points while Advanced players 500
"""

def switch_level(level):
    """
    Determines level and returns int of the points for level
    """
    if level == 'N':
        return 50
    elif level == 'B':
        return 150
    elif level == 'E':
        return 300
    elif level == 'A':
        return 500
    else:
        raise ValueError


if __name__ == '__main__':
    print(switch_level('N'))
    print(switch_level('B'))
    print(switch_level('E'))
    print(switch_level('A'))
    print(switch_level('S'))

# is this the assignment? Seemed waay easier than what you made it out
# to be in the video,, too easy
