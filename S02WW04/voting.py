
def readVotes():
    f = open("votes.txt", 'r')
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
   # zipVotes(mat)
        
    
        
def zipVotes(matrix):
    print("ZIPVOTES")
    for line in matrix:
        for number in line:
            number = int(number)
            print(number)
        print(type(line[0]))


readVotes()


# B 

