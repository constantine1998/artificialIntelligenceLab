import random
import numpy as np
import inputData as iD

def selection(sortedPopulation):
    #Selection method is Roulette Wheel
    selectedIndex = []
    tempS = np.array(sortedPopulation)
    totalSum = 0
    for i in range(iD.popSize):
        totalSum = totalSum + 1/tempS[i][1]
        

    for i in range(iD.popSize):
        tempS[i][1] = ((1/tempS[i][1])/totalSum)
        
    tempS[0][1] = tempS[0][1]*360
    for i in range(iD.popSize-1):
        tempS[i+1][1] = tempS[i+1][1]*360 + tempS[i][1]
        
    
    for i in range(iD.popSize):
        pick = random.uniform(0,360)
        for j in range(iD.popSize):
            if (tempS[j-1][1] < pick <= tempS[j][1]) and j!=0:
                selectedIndex.append(sortedPopulation[i][0])
                break
            if (0 < pick <= tempS[j][1]) and j==0:
                selectedIndex.append(sortedPopulation[j][0])
                break
                
    return selectedIndex

def findParents(population,sortedPopulation):
    selectedIndex = selection(sortedPopulation)
    parentsToMate = []
    for i in range(iD.popSize):
        parentsToMate.append(population[selectedIndex[i]])
    return parentsToMate