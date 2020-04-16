import anneal
import inputData

if __name__ == '__main__':
    inputData.inputData()
    totalDistanceAnneal,pathAnneal = anneal.anneal()
    #print("Stimulated Annealing Results - ")
    #print("The path to be taken is:\n")
    print(" ".join(str(x) for x in pathAnneal))
    #print("\nThe total distance covered will be: "+str(totalDistanceAnneal)+" units\n")
