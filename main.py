"""
    Implementation of HBMO for minimizing a mathematical function with 2 parameters.
    TODO: pune ca parametrii generici la intreg algoritmu':
        NR_INITAL_SOLUTIONS
        self.speedReductionFactor
        self.energyReductionAmount
        self.speed
        self.energy
        self.probabilityToMateDroneThreshold


"""

__author__ = 'cristiprg'

import InitialSolutionsGenerator
import Solution

solutions = InitialSolutionsGenerator.generateInitialSolutions()

"""
for i in solutions:
    print("f" + str(i) + "=", end=' ')
    print(Solution.FUNCTIA(i.x, i.y))
"""


queen = solutions[0]

print("f" + str(queen) + " = " + str(Solution.FUNCTIA(queen.x, queen.y)))

while queen.energy >= 0:
    for (index, drone) in enumerate(solutions):
        if index is 0:  # this the queen actually
            continue

        if queen.probabilityToMateDrone(drone) > queen.probabilityToMateDroneThreshold:
            broods = queen.createBroods(drone)
            # Improve broods here!
    queen.nextIteration()