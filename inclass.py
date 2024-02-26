def createBoard(n):
    board = []

    for numRows in range(n):
        row = [0]*n
    board.append(row)

def printBoard(SBoard):
    for row in SBoard:
        for col in row:
            print(SBoard[row][col], end=" ")
        print("\n")


def isValidMove(board,row,col):
    for colNo in range(col):
        if board[row][colNo] == 1:
            return False

    for r,c in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
        if board[r][c] == 1:
            return False
        

        for r,c in zip(range(row+1,len(board),1),range(col-1,-1,-1)):
            if board[r][c] == 1:
                return False
            
def solvedBoard(b, col):
    if col == n:
        return b,True
    else:
        for row in range(n)
        isValidMove(b,?,col)