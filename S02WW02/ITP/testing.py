#a matrix is a list of lists 
#when referring to the matrix you are referring to the outer []
#[[],[],[]]
#each data point inside a matrix is a column -> [[0,0,1,1,0 (each is a row )]]
# print(cinema[0][2])
#           [row][column]


cinema = [[0,1,1,0,0], [1,1,1,1,1], [0,0,0,0,1]] 
"""""
for row in cinema:
    for seat in row:
        print(seat)
"""

for rowIndex in range (len(cinema)):
    rowScore = 0
    for colIndex in range(len(cinema[rowIndex])):
        rowScore += cinema[rowIndex][colIndex]