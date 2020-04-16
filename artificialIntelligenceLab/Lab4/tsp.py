import anneal
import inputData
import FirstGenPop
import genetic
from distance import getTotalDist

if __name__ == '__main__':
    inputData.inputData()
    totalDistanceAnneal,pathAnneal = anneal.anneal()
    print("Stimulated Annealing Results - ")
    print("The path to be taken is:\n")
    print(pathAnneal)
    print("\nThe total distance covered will be: "+str(totalDistanceAnneal)+" units\n")
    
    population = []
    for i in range(inputData.popSize):
        population.append(FirstGenPop.FirstGen(inputData.cityCoord))
    
    pathGenetic = genetic.genetic(population,inputData.generations)
    path_Genetic = []
    for city in pathGenetic:
        path_Genetic.append(inputData.cityCoord.index(city))
    print("Genetic Algorithm Results - ")
    print("\nThe path to be taken is:")
    print(path_Genetic)
    print("\nThe total distance covered will be: "+str(getTotalDist(path_Genetic))+" units\n")