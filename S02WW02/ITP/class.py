"""
MATRICES
"""

cinema = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

#matrix[row][col]
screens = []
for row in cinema:
    screens.append(cinema[1])



################### NB
    
cinema = []
numRows = 5
numSeats = 5

for rowNo in range(numRows):
    row = []
    for seatNo in range(numSeats):
        row.append(0)
    cinema.append(row)


##############  NB

cinema = []
numRows = 5
numSeats = 5

for rowNo in range(numRows):
    row = [0] * numSeats
    cinema.append(row)

##################### MODIFYING A MATRIX

cinema[2][2]

###################

for i in range(1,4):
    cinema[3,i] = 1 

###################
for i in range(len(cinema[0])):
    cinema[4][i] = 1


##################
    #bubble sort 

l = [5,8,2,9,7,3]
for numPasses in range (len(l)-1):
    for pairNo in range(len(l)-1):
        if l[pairNo] > l[pairNo+1]:
            #swap
            l[pairNo], l[pairNo+1] = l[pairNo+1], l[pairNo]


###################
            
L = [17,20,26,31,44,54,55,65,77,93]
numberTOFound = 54 

midpoint = (0 + len(L)-1)//2

if numberTOFound == L[midpoint]:
    print("Yippee we found the number to be found ", numberTOFound, "at position, ", midpoint)
    quit()
else:
    while numberTOFound != L[midpoint]:
        if numberTOFound < L[midpoint]:
            midpoint = L[:midpoint]
        else: 
            midpoint = L[midpoint]
        if numberTOFound == L[midpoint]:
            print("yippee")
            quit()
        else:
            print("i checked the number")



######################
            # LIST COMPREHENSION 
L = [20,30,40,50]
myList = []
for number in L:
    if number > 40:
        number = number * 2 
        myList.append(number)
        
#Alt method
        #expression iterator conditional
myList = [number * 2  for number in L if number > 40]

#################################

#   