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

    euc_nuec = raw_input()
    noOfCities = input()
    while(noOfCities<3):
        print("There is only one way to do that! Input a number greater than 2\n")
        noOfCities = input("No. of Cities\n")
    for i in range(noOfCities):
        temp = raw_input()
        nextCoord = tuple([float(i) for i in temp.split()])
        cityCoord.append(nextCoord)
    
    for i in range(noOfCities):
        temp = raw_input()
        temp = [float(i) for i in temp.split()]
        cityDistance.append(temp)
