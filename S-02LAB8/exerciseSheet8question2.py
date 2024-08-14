heightMatrix = [[0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1]]

testingMatrix2 = [[0, 1, 0, 0],[0, 1, 0, 0],[0, 1, 1, 0],[1, 1, 1, 1]]

def getBuildingHeight(mat):
    tally = 0
    counter = 0
    while counter in range(len(mat)+1):
        for list in mat:
            tally = tally + list[counter]
        storageList.append(tally)
        tally = 0
        counter += 1
    print(storageList)

storageList = []

def determineElevations():
    sortedSunList = sorted(storageList)
    print(f"building {sortedSunList[len(sortedSunList)-1]} gets the most sun")




getBuildingHeight(heightMatrix)
determineElevations()
#getBuildingHeight(testingMatrix2)




