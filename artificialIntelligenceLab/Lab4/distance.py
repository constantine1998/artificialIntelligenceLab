import inputData

def getTotalDist(currentOrder):
    noOfCities = inputData.noOfCities
    totalDistance  = 0
    cityDistance = inputData.cityDistance
    for i in range(noOfCities-1):
        totalDistance = totalDistance + cityDistance[currentOrder[i]][currentOrder[i+1]]
    return totalDistance

def getTotalDist2(currentOrder):
    noOfCities = inputData.noOfCities
    totalDistance  = 0
    cityDistance = inputData.cityDistance
    for i in range(noOfCities-1):
        i1 = inputData.cityCoord.index(currentOrder[i])
        i2 = inputData.cityCoord.index(currentOrder[i+1])
        totalDistance = totalDistance + cityDistance[i1][i2]
    return totalDistance