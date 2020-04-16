import distance
from operator import itemgetter
import inputData as iD
def sortPopulation(population):
    fitnessScores = {}
    for i in range(len(population)):
        fitnessScores[i] = distance.getTotalDist2(population[i])
    fitnessScores = sorted(fitnessScores.items(),key = lambda x: x[1])
    return fitnessScores

def sortNselect(children):
    toSort=[]
    #print(children)
    for i in range(len(children)):
        score = (children[i],distance.getTotalDist2(children[i]))
        toSort.append(score)
    toSort = sorted(toSort,key=itemgetter(1))
    del children[:]
    for i in range(iD.popSize):
        children.append(toSort[i][0])
    return children