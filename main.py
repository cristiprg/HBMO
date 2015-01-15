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

import cProfile
import InitialSolutionsGenerator
from Solution import Solution
from Solution import FUNCTIA

def runHBMO():

    # Generate the initial set of solutions.
    solutions = InitialSolutionsGenerator.generateInitialSolutions()

    # Select the queen.
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
                # Improve broods here, ca se blocheaza in minim local!
                if bestBrood.getFitness() < bestSolution.getFitness():
                    bestSolution = bestBrood
                    print("Found better!")
                    print(str(bestSolution) + " =  " + str(FUNCTIA(bestSolution.x, bestSolution.y)) +
                          "\nfitness = " + str(bestSolution.getFitness()))

            else:
                pass

        queen = bestSolution  # Cu asta se reseteaza si conditia de oprire!
        queen.nextIteration()

    print(str(bestSolution) + " =  " + str(FUNCTIA(bestSolution.x, bestSolution.y)) +
          "\nfitness = " + str(bestSolution.getFitness()))

cProfile.run('runHBMO()', sort='tottime')