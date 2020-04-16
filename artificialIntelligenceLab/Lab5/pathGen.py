import random
import inputData

def getFirstOrder():
    noOfCities = inputData.noOfCities
    cities = [i for i in range(noOfCities)]
    curNode = random.choice(cities)
    solution = [curNode]

    free_nodes = set(cities)
    free_nodes.remove(curNode)
    while free_nodes:
        next_node = min(free_nodes, key=lambda x: inputData.cityDistance[curNode][x])
        free_nodes.remove(next_node)
        solution.append(next_node)
        curNode = next_node
    
    return solution

def getNextOrder(currentOrder):
    candidate = list(currentOrder)
    l = random.randint(2, len(currentOrder) - 1)
    i = random.randint(0, len(currentOrder) - l)
    candidate[i : (i + l)] = reversed(candidate[i : (i + l)])
    return candidate

def final(currentOrder):
    free_nodes = set(currentOrder)
    firstNode = currentOrder[0]
    free_nodes.remove(firstNode)
    