total = 0

#Function definition
def getSquare (lo_shu_square):
    file = open('lo_shu_square.txt', 'r')
    print(file)
    value_to_compare_against = sum (lo_shu_square[0])
    file.close()

"""

    #1. add every row
    #code here
    for row in lo_shu_square:
        total = sum(row)            ``
        print(total)

    if total != value_to_compare_against:
            return False
    
    file.close()
``
    #2. add every column
    #code here
    file = open(lo_shu_square, 'r').readlines
    for row in lo_shu_square:
        #total = zip(file.readlines[0],file.readlines[1], file.readlines[2])

    if total != value_to_compare_against:
        return False
    file.close()
    

    #3. Add the left Diagonal
    #code here
    if total != value_to_compare_against:
        return False
    

    #4. Add the right Diagonal
    #code here
    if total != value_to_compare_against:
        return False
    return True
    
#function invocation


result = getSquare([[4, 9, 2], [3, 5, 7], [8, 1, 6]])
if result == False:
    print("not a lo shu magic square")
else:
    print("Is a lo shu magic square")
"""

getSquare('lo_shu_square.txt')