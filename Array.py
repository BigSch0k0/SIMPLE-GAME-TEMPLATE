

from posixpath import split


def arraySplit(array, splitFactor):

    if len(array) % splitFactor != 0: return 


    arraySplit = []

    for i in range(splitFactor):
        arraySplit.append([])


    count = 0

    for i in range(len(array)):

        arraySplit[count].append(array[i])

        if count == splitFactor-1: count = 0
        else : count+=1

    return arraySplit


#testSet = [1,2,3,4,5,6,7,8,9,10,11,12]
#new = arraySplit(testSet, 4)
#print(new)
    

    
