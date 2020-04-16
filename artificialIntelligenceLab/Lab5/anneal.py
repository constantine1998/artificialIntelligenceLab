from distance import getTotalDist
import pathGen as pg
import random
import math
from copy import deepcopy
import time

def anneal():

    temperature = 100000.0
    deltaDist = 0
    coolingRate = 0.9999
    absoluteTemp = 0.00001

    currentOrder = pg.getFirstOrder()
    distance = getTotalDist(currentOrder)

    startTime = time.time()
    TIME_OUT = 295
    while (temperature > absoluteTemp):
        nextOrder = pg.getNextOrder(currentOrder)
    
        deltaDist = getTotalDist(nextOrder) - distance
    
        if ((deltaDist < 0) or (distance > 0 and ((1/(1 + math.exp(-deltaDist / temperature))) < random.uniform(0.0,1.0)))):
            currentOrder = deepcopy(nextOrder)

            distance = deltaDist + distance
    
        temperature = temperature * coolingRate
        print("Next Chosen Distance: "+str(distance))
        if(time.time() > startTime + TIME_OUT):
            return distance,currentOrder

    shortestDistance = distance
    
    return shortestDistance,currentOrder
