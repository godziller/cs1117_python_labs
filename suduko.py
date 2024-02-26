def readBoard (file):
    infile = open(file, "r")
    '''your code here'''
    b = [] # outer list 
    rows = infile.readlines()   #list of strings

    for row in rows:
        row = row.strip("\n").split()
        intRow = []
        intRow = [int(num) for num in row]
        b.append    
    infile.close()
    return b
def printBoard (SBoard):
#First Hint. You need to print every row. Think of % (modulus) and you would
#like to print the dividing sets of characters at the start, end and after every
#third row
#Second Hint: Within every row you would like to print every column in that
#row. The character '|' needs to go at the start, end and after every third column.
#If there's a zero a space should be printed.
    #'''code here'''
    for rowNum in range(len(SBoard)):       # do something 9 times
        if rowNum % 3 == 0:
            print ("+---------+---------+---------+")
        for colNo in range(len(SBoard[0])):
            if colNo % 3 == 0:
                print('|') #think of end character
            if SBoard[rowNum][colNo] == 0:
                print(" ")
            else:
                print(" " + str(SBoard[rowNum][colNo]) + " ", end="")
        print("|")
    print ("+---------+---------+---------+")

def solveBoard (b, row, col):
    result = False

    if row == 9: 
        return True, b
    
    else: 
        nextRow = row 
        nextCol = col + 1 
    
    if b[row][col] != 0 :
        result, b  = solveBoard(b, nextRow, nextCol)
        return result,b
    
    else: 
        for potentialNUm in range(1,len(b)+ 1):
            

#APPROXIMATE Pseudocode - This is provided as a guide. Further details were
#given in class.
#if: Have I reached row number 9. If I have, I've solved the board return
#True and return the filled out board.
#else (recursive case)
#if the current square is not equal to a '0' recursively call the
#function again passing in the next square . Sub question: what is the next row/col?
#else consider every possible combination of number
#is this a validNumber?
#update the square with the number
#if recursively calling the function again (next row next
#col) == true:
#return true and the board
#At the end of my loop, set the square back to zero, pass back false
#and the board
#return result, b
def isValidMove (b, row, col, number):
    valid = True

    for colNo in range(len(b)):
        if b[row][colNo] == number:
            return False

    startRow = row // 3 * 3
    startCol = col // 3 * 3         
    
    for rowNo in range(len(n[0])):
        if b[rowNo][col] ==  number:
            return False
        



#CHECK ROW
#e.g. imagine I'm the number 7 i.e. number = 7?
#check the the 9 columns in that row
#if the number at any given square equal to the variable number return false
#CHECK COLUMN
#same as above but column
#CHECK MINI GRID
#figure out what mini grid you're in
#to do this you need to get the starting square
##to do this e.g. 4 // 3 * 3 = 3 (row) and 1 //3 * 3 = 0 (column)
#once you have your starting point consider every column in that row, then
#consider the row and the next i.e.
#nested for loop, outer loop runs three times (for each row) and the inner
#loop runs 9 times (for each column)
    return valid
# Main Program
filename = "easyPuzzle.txt"
board = readBoard(filename)
    startRow = row // 3 * 3
    startCol = col // 3 * 3 
print("\nPROBLEM:")
printBoard(board)

result, solvedBoard = solveBoard(board, 0, 0)
if result == False:
    print("Solution does not exist")
else:
    print("\nSOLUTION:")
    printBoard(solvedBoard)
