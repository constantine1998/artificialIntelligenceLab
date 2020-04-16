import random
import inputData as iD
import sortPop

def geneExchange(parent1,parent2):
    child1 = []
    child2 = []
    rand1 = int(round(random.random() * iD.noOfCities))
    rand2 = int(round(random.random() * iD.noOfCities))
    
    firstDivider = min(rand1, rand2)
    secondDivider = max(rand1, rand2)

    for i in range(firstDivider, secondDivider):
        child1.append(parent1[i])
        child2.append(parent2[i])
    for i in parent2:
        if i not in child1:
            child1.append(i)
    for i in parent1:
        if i not in child2:
            child2.append(i)
    return child1,child2

def mating(couples):
    children = []
    couples = random.sample(couples, iD.popSize)
    for i in range(iD.popSize/2):
        child1,child2 = geneExchange(couples[i], couples[iD.popSize-i-1])
        children.append(child1)
        children.append(child2)
    return children
    
def selectNextGen(children,sortedPopulation,population):
    k = int(iD.popSize*0.1)
    selectedPop = []
    for i in range(k):
        selectedPop.append(population[sortedPopulation[i][0]])
    children = children+selectedPop
    return sortPop.sortNselect(children)
    
def mutation(children):
    mutatedChild = []
    for i in range(iD.popSize):
        if (random.uniform(0,100) < iD.mutRate):
            index1 = int(random.random()*iD.noOfCities)
            index2 = int(random.random()*iD.noOfCities)
            temp1 = children[i][index1]
            temp2 = children[i][index2]
            children[i][index2] = temp1
            children[i][index1] = temp2
        mutatedChild.append(children[i])
    return mutatedChild
    return