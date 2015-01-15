"""
    Generate the initial solutions.
"""

__author__ = 'cristiprg'

from sortedcontainers import SortedSet  # http://www.grantjenks.com/docs/sortedcontainers/sortedset.html
from Solution import Solution
import random

MIN = -9999
MAX = 9999


def generateInitialSolutions():
    """
        Aicia vine Honey Bee Colony in actiune.
        Deocamdata facem random
    :return:
        A SortedSet filled with random solutions
    """
    solutions = SortedSet()
    for i in range(999):
        x = random.uniform(MIN, MAX)
        y = random.uniform(MIN, MAX)
        solutions.add(Solution(x, y))
    return solutions


def getSolutions():
    return generateInitialSolutions()