

def readVotes():
    f = open("votes.txt", 'r')
    print("\n --Question 1-- \n")                               #Very important base script for finding the matrix 
    lineList = []
    for line in f.readlines():
        line = line.strip('\n').replace(',','').split()         #getting rid of any extra lines, commas and splitting up the words 
        lineList.append(line)
    
    f.close()
    return lineList

# Func to return full voting count across all voting precidences

def countAllVotes(mat):
    for line in mat:        #For each line (list) in our matrix of lists 
        rowAmount = 0       #variable used to store the value of each row for print
        for number in line:
            number = int(number)
            rowAmount = rowAmount + number
        print(rowAmount)

    
############################################################################################################################3
    


def subFunction_TotalAmountVotes(matrix):         # creating this as a precaution as i feel i may need to find the total in later questions
    amount = 0
    for line in matrix:                           #simply getting each list in the matrix, number in those lists, and adding it to a grand
        for number in line:
            amount = amount + int(number)
    return amount
    
        
def zipVotes(matrix):
    print("\n --Question 2-- \n")

    pointer = 0                         #a simple pointer to move along our while loop
    while pointer in range(0,4):        #while the pointer is in range of the amount of candidates we have 
        amount = 0                      #the sum of each candidates score (initialized to 0)
        for line in matrix:                             # for each sublist in our matrix
            amount = amount + int(line[pointer])

        candidatePercentage = round((amount / subFunction_TotalAmountVotes(matrix)) * 100, 2)
        #print(candidatePercentageList)
        candidatePercentageList.append(candidatePercentage)
        individualList = [candidatePercentage, numberToCharacterDict[pointer]]
        cAndPMatrix.append(individualList)
        #print(cAndPMatrix)

        print(f"candidate {pointer}: {amount} \n Vote Percentage {candidatePercentage}% \n")         # print this as your candidate's sum of votes, then repeat until out of range, ie. no more candidates
        
        pointer += 1                                    #inc pointer 


##################################################################################################################################3
        # Question 3 and  

def overFifty():
    for lists in cAndPMatrix:
        np.
   
matrix = readVotes()
candidatePercentageList = []
numberToCharacterDict = {0:'A',1:"B",2:'C',3:'D'}
cAndPMatrix = []
countAllVotes(matrix)
zipVotes(matrix)
overFifty()
# B 

