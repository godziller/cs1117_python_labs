# corkCity = [['o','x','o','x','o'], ['o','o','o','x','x'], ['o','o','o','o','o']]
corkCity = [['o','o','o','o','o'], 
            ['o','o','x','o','o'], 
            ['o','o','x','o','o'],
            ['o','o','x','o','o'], 
            ['o','o','o','o','o']]



N = len(corkCity)
M = len(corkCity[0])
def isValidPos(proposedRow, proposedCol, N, M):
    return 0 <= proposedRow < N and 0 <= proposedCol < M

def getAdjacentCells(map, row, col):
    adjacentCells = []
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    for d in directions:
        adjRow = row + d[0]
        adjCol = col + d[1]
        if isValidPos(adjRow, adjCol, len(map), len(map[0])):
            adjacentCells.append(map[adjRow][adjCol])
    return adjacentCells

def createNewMap(N, M):
    return [['o' for _ in range(M)] for _ in range(N)]

def printNewMap(map):
    for row in map:
        print(' '.join(row))
    print()

def getMaps(filename):
    listOfMaps = []
    with open(filename, 'r') as file:
        for line in file:
            map = [list(x.strip()) for x in line.split()]
            # Skip empty lines
            if not map:
                continue
            # Check if all rows have the same length
            if len(set(len(row) for row in map)) != 1:
                print("Error: Inconsistent row lengths in map:", map)
                continue  # Skip this map and proceed with the next one
            listOfMaps.append(map)
    return listOfMaps
'''
def main():
    # Use the provided matrix corkCity
    map = corkCity
    N = len(map)
    M = len(map[0])
    newMap = createNewMap(N, M)
    for row in range(N):
        for col in range(M):
            if map[row][col] == 'x':
                newMap[row][col] = 'x'
            else:
                adjacentCells = getAdjacentCells(map, row, col)
                count = adjacentCells.count('x')
                newMap[row][col] = str(count)
    printNewMap(newMap)
'''
def main():
    maps = getMaps("maps.txt")
    combined_matrix_1 = []
    combined_matrix_2 = []

    for idx, map in enumerate(maps, start=1):
        N = len(map)
        M = len(map[0])
        newMap = createNewMap(N, M)
        for row in range(N):
            for col in range(M):
                if map[row][col] == 'x':
                    newMap[row][col] = 'x'
                else:
                    adjacentCells = getAdjacentCells(map, row, col)
                    count = adjacentCells.count('x')
                    newMap[row][col] = str(count)

        if idx <= 3:
            combined_matrix_1.extend(newMap)
        else:
            combined_matrix_2.extend(newMap)

    print("Matrix 1:")
    printNewMap(combined_matrix_1)  # Ensure this line is correct
    print("\nMatrix 2:")
    printNewMap(combined_matrix_2)


if __name__ == "__main__":
    main()

