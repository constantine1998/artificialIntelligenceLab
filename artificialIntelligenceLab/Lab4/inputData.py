import random
import math

euc_nuec = ""
noOfCities = 0
cityCoord = []
cityDistance = []
popSize = 0
mutRate = 0
generations = 0

def inputData():
    global euc_neuc
    global noOfCities
    global cityCoord
    global cityDistance
    global popSize
    global mutRate
    global generations
    print("------------------Usage------------------\nInput 'Euclidian' or 'Non-Euclidian'\nThen input no. Of cities\nThen input city coordinates one by one seperated by space(like 2 3)\nLastly enter city distance seperated by space.")
    euc_nuec = raw_input()
    noOfCities = input()
    while(noOfCities<3):
        print("There is only one way to do that! Input a number greater than 2\n")
        noOfCities = input("No. of Cities\n")
    popSize = 200#input("Size of the population\n")
    mutRate = 10#input("Mutation Rate\n")
    #while(mutRate<0 or mutRate>100):
     #   print("Mutation Rate should be between 0 and 100\n")
     #   mutRate = input("Mutation Rate\n")
    generations = 200#input("No. of generations to do the mating\n")
    for i in range(noOfCities):
        temp = raw_input()
        nextCoord = tuple([float(i) for i in temp.split()])
        cityCoord.append(nextCoord)
    #[(int(random.uniform(0, 1000)), int(random.uniform(0, 1000))) for i in range(noOfCities)]
    for i in range(noOfCities):
        temp = raw_input()
        temp = [float(i) for i in temp.split()]
        cityDistance.append(temp)
    #[[0 for i in range(noOfCities)] for j in range(noOfCities)]
    #for i in range(noOfCities):
     #   for j in range(noOfCities):
      #      xDistance = cityCoord[i][0] - cityCoord[j][0]
       #     yDistance = cityCoord[i][1] - cityCoord[j][1]
        #    if xDistance == 0 and yDistance == 0:
         #       cityDistance[i][j] = float('inf')
          #  else:
           #     cityDistance[i][j] = math.sqrt(xDistance ** 2 + yDistance ** 2)
