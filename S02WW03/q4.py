# lsms = [[4,9,2],
#         [3,5,7],
#         [8,1,6]]

lsms = []

inFile = open("lsms.txt", "r")

lines = inFile.readlines()
for line in lines:
    line = line.strip("\n")
    line = line.split(" ")
    for i in range(len(line)):
        line[i] = int(line[i])
    lsms.append(line)

inFile.close()


def check_lsms(lsms):
    
    colSums = []
    for colNo in range(len(lsms[0])):
        colSum = 0
        for rowNo in range(len(lsms)):
            colSum += lsms[rowNo][colNo]
        colSums.append(colSum)

    rowSums = []
    for rowNo in range(len(lsms[0])):
        rowSum = 0
        for colNo in range(len(lsms)):
            rowSum += lsms[rowNo][colNo]
        rowSums.append(rowSum)

    diagonalSumLeft = 0
    for i in range(len(lsms[0])):
        diagonalSumLeft += lsms[i][i]

    diagonalSumRight = 0
    for i in range(len(lsms[0])-1,-1,-1):
        diagonalSumRight += lsms[i][i]


    if rowSums == colSums and diagonalSumRight == diagonalSumLeft and diagonalSumLeft in rowSums:
        return True
    else:
        return False

            
answer = check_lsms(lsms)
print(answer)