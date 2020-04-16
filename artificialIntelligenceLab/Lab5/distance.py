import inputData

def getTotalDist(currentOrder):
    noOfCities = inputData.noOfCities
    totalDistance  = 0
    cityDistance = inputData.cityDistance
    for i in range(noOfCities-1):
        totalDistance = totalDistance + cityDistance[currentOrder[i]][currentOrder[i+1]]
    return totalDistance