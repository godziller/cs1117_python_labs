
def readVotes():
    f = open("votes.txt", 'r')
    print("\n --Question 1-- \n")
    lineList = []
    for line in f.readlines():
        line = line.strip('\n').replace(',','').split()         #getting rid of any extra lines, commas and splitting up the words 
        lineList.append(line)
    
    f.close()
   # print(lineList)
    countAllVotes(lineList)

# Func to return full voting count across all voting precidences

def countAllVotes(mat):
    for line in mat:        #For each line (list) in our matrix of lists 
        rowAmount = 0       #variable used to store the value of each row for print
        for number in line:
            number = int(number)
            rowAmount = rowAmount + number
        print(rowAmount)
    zipVotes(mat)
        
    
        
def zipVotes(matrix):
    print("\n --Question 2-- \n")

    pointer = 0                         #a simple pointer to move along our while loop
    while pointer in range(0,4):        #while the pointer is in range of the amount of candidates we have 
        amount = 0
        for line in matrix:             # for each sublist in our matrix
            amount = amount + int(line[pointer])        # constructing a variable to act as a 'wallet' to store the sum of each number
        print(f"Candidate {pointer}: {amount}")         # print this as your candidate's sum of votes, then repeat until out of range, ie. no more candidates
        pointer += 1                    #inc pointer 


readVotes()


# B 

