"""
    Implementation of HBMO for minimizing a mathematical function with 2 parameters.
"""

from OrderedSet import OrderedSet
__author__ = 'cristiprg'

"""
    In clasa asta bagam mancarurile
"""
class Solution:
    x = 0
    y = 0

    def __init__(self, x=None, y=None):
        self.x = x or 0
        self.y = y or 0

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

SolutionsSet = OrderedSet()