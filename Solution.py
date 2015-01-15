"""
    In clasa asta bagam mancarurile.
"""
__author__ = 'cristiprg'

import math
import random

def FUNCTIA(x, y):
    c1 = 20
    c2 = 0.2
    c3 = 2*math.pi

    return -c1 * math.exp(-c2 * math.sqrt(1/2 * (x**2 + y**2))) - \
        math.exp(1/2 * (math.cos(c3*x) + math.cos(c3*y))) + c1 + math.e


class Solution:
    """
    The bee.
    """
    def __init__(self, x=None, y=None):
        self.x = x or 0
        self.y = y or 0

        self.speedReductionFactor = 0.9  # S(t+1) = alpha * S(t), deci, intre 0 si 1 (pag 665)
        self.energyReductionAmount = 2  # E(t+1) = E(t) - gamma, deci intre 0 si 100? Gandim in procente aici?

        self.speed = 100  # ???
        self.energy = 100  # 100%???

        self.probabilityToMateDroneThreshold = 0.5

    def __lt__(self, other):
        if isinstance(other, Solution):
            return self.getFitness() < other.getFitness()
        else:
            raise Exception("Class Soultion compared with other class.")

    def getFitness(self):
        """
        :return:
            The fitness function of this solution.
            Acuma, o consideram diferenta fata de 0.
        """
        return abs(FUNCTIA(self.x, self.y))

    def probabilityToMateDrone(self, drone):
        """
        Computes to probability that this solution (the queen, hopefully) will pick
        the drone in the mating dance.
        :param drone:
        :return: a float in interval [0, 1] representing the probability.
        """
        if isinstance(drone, Solution):
            return math.exp(-abs(self.getFitness() - drone.getFitness()) / self.speed)
        else:
            raise Exception("Drone not of type Solution")

    def nextIteration(self):
        """
        Supposing this is the queen, the following parameters have to updated at each iteration:
            speed,
            energy
        :return:
        """
        self.speed *= self.speedReductionFactor
        self.energy -= self.energyReductionAmount

    def numberOfBroodsWithDrone(self, drone):
        """
        Computes the number of broods this queen makes with the drone based on:
            The queen's energy
            The drone's fitness value
            A random float number in interval [0, 1]
        :param drone:
        :return: An non-negative integer
        """
        return int(self.energy * drone.getFitness() * random.uniform(0, 1))

    def createBroods(self, drone):
        nr_broods = self.numberOfBroodsWithDrone(drone)
        print("Creating" + str(nr_broods) + " broods")



    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

