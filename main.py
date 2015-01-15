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
from Solution import Solution

solutions = InitialSolutionsGenerator.generateInitialSolutions()

queen = solutions[0]
print(str(queen) + ".fitness = " + str(queen.getFitness()))

bestSolution = Solution()
while queen.energy >= 0:
    for (index, drone) in enumerate(solutions):
        if index is 0:  # this the queen actually
            continue

        if queen.probabilityToMateDrone(drone) > queen.probabilityToMateDroneThreshold:
            broods = queen.createBroods(drone)
            if len(broods) is 0:
                continue

            bestBrood = broods[0]
            # Improve broods here!
            if bestBrood.getFitness() < bestSolution.getFitness():
                bestSolution = bestBrood
                print("Found better!")
                print(str(bestSolution) + "\nfitness = " + str(bestSolution.getFitness()))

        else:
            pass

    queen.nextIteration()

print("best solution:" + str(bestSolution) + "\nfitness = " + str(bestSolution.getFitness()))
