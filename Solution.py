"""
    In clasa asta bagam mancarurile.
"""
__author__ = 'cristiprg'


class Solution:
    x = 0
    y = 0

    def __init__(self, x=None, y=None):
        self.x = x or 0
        self.y = y or 0

    def __lt__(self, other):
        if isinstance(other, Solution):
            if self.x < other.x:
                return True
            elif self.x == other.x:
                if self.y < other.y:
                    return True
                else:
                    return False
        else:
            raise Exception("Class Soultion compared with other class.")

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

