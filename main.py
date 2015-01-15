"""
    Implementation of HBMO for minimizing a mathematical function with 2 parameters.
"""

__author__ = 'cristiprg'

import InitialSolutionsGenerator

solutions = InitialSolutionsGenerator.generateInitialSolutions()

for i in solutions:
    print(i)
