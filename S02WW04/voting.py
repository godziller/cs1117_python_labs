
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
        amount = 0                      #the sum of each candidates score (initalized to 0)
        for line in matrix:                             # for each sublist in our matrix
            amount = amount + int(line[pointer])
        #print("total amount", subFunction_TotalAmountVotes(matrix))
        candidatePercentage = round((amount / subFunction_TotalAmountVotes(matrix)) * 100, 2)
        candidatePercentageList.append(candidatePercentage)
        print(f"{candidateDict[pointer]}: {amount} \n Vote Percentage {candidatePercentage}% \n")         # print this as your candidate's sum of votes, then repeat until out of range, ie. no more candidates
        
        pointer += 1                                    #inc pointer 


##################################################################################################################################3
        # Question 3 and  

def overFifty():
    for percentile in candidatePercentageList:
        if percentile >= 50:
            print('WE HAVE A WINNER')
   
    candidatePercentageList.sort()
    print(candidatePercentageList[len(candidatePercentageList)-1])

matrix = readVotes()
candidatePercentageList = []
candidateDict = {0: "Candidate A", 1:"Candidate B" , 2:"Candidate C", 3:"Candidate D" }

countAllVotes(matrix)
zipVotes(matrix)
overFifty()
# B 

