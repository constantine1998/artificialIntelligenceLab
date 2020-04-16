from sortPop import sortPopulation
import capableParents as cp
import geneAlteration as ga
from copy import deepcopy

def nextGeneration(population):
    sortedPopulation = sortPopulation(population)
    couples = cp.findParents(population,sortedPopulation)
    children = ga.mating(couples)
    children = ga.selectNextGen(children,sortedPopulation,population)
    children = ga.mutation(children)
    return children

def genetic(population,generations):
    sortedPopulation = sortPopulation(population)
    bestDistance = sortedPopulation[0][1]
    print(" First Route Distance :- {}".format(sortedPopulation[0][1]))
    for i in range(generations):
        currentDistance = deepcopy(sortedPopulation[0][1])
        if bestDistance > currentDistance:
            bestDistance = deepcopy(currentDistance)
            bestSortedPop = deepcopy(sortedPopulation)
            bestPop = deepcopy(population)
        print(" {} Route Distance :- {}".format(i+1,sortedPopulation[0][1]))
        population = nextGeneration(population)
        sortedPopulation = sortPopulation(population)
    if bestDistance < sortedPopulation[0][1]:
        return bestPop[bestSortedPop[0][0]]
    return population[sortedPopulation[0][0]]
