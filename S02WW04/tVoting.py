names = ['Candidate 1',
         'Candidate 2',
         'Candidate 3',
         'Candidate 4']

def readVotes(filename):
    f = open(filename, 'r')
    lineList = []
    for line in f.readlines():
        line = line.strip('\n').replace(',','').split()         #getting rid of any extra lines, commas and splitting up the words 
        lineList.append(line)
    
    f.close()
    #print(lineList)
    return lineList

# Func to return full voting count across all voting precidences

def countAllVotes(mat):
    totalCount = 0 
    for line in mat:        #For each line (list) in our matrix of lists 
        for number in line:
            number = int(number)
            totalCount = totalCount + number
    return totalCount

# Take in a 2d matrix and squash it into 1 list - the list being a list of the sum of the columns
# squashed = [Candidate 1 Total, Candidate 2 Total, etc...]
def squashMatrix(matrix):
    squashed = matrix[0]
    for row in range(1, len(matrix)):
        squashed = map(lambda x, y: int(x)+int(y), matrix[row], squashed)
    return squashed

# Take in a list of raw numbers, plus a denominator. Return a list of percentages
def countToPercent(candidateTotalsList, totalCount):
    return map(lambda x: round(float(x)*100/totalCount, 2), candidateTotalsList)

#  I have 3 seperate lists - want to put them into a 2d matrix - reason is I want to keep the names associated with the results.
# which will be important when I buble sort later to reorder list in order of each candidates success.
#       pretty = [ [Candidate 1, rawCount, percentage],
#                  [Candidate 2, rawCount, percentate],
#                   [etc...]
#                 ]
def prettyPrint(Titles, rawCount, percentResults):
    pretty = zip(Titles, rawCount, percentResults)
    return pretty

# my bubble sort - take in an unorded 2d list and return that list ordered from most to least votes
# using vote count to sort, but could have done with percentage result too 
def sortByCount(results):
    n = len(results)
    voteCountIndex = 1 
   
    for i in range (n):
        for j in range (0, n-i-1):
            if int(results[j][voteCountIndex]) < int(results[i][voteCountIndex]):
                results[j], results[j+1] = results[j+1], results[j]
    return results


# This answers c and d - checks for >50% first, if that fails, prints top 2 candidates
# taking advange here of having a sorted list passed in
def printFinalResults(sortedResults):
    nameIndex = 0
    percentIndex = 2

    # First entry in list will always be highest - so check if 50% reached.
    if sortedResults[0][percentIndex] > 50:
        print("Outright Winner is: " + sortedResults[0][nameIndex])
    # 50% not reached - so print out top 2 candidates for a run off.
    else:
        print("We have a run off between:")
        print(sortedResults[0][nameIndex])
        print(sortedResults[1][nameIndex])


# This allows me to return results for any/multiple input files.
def tallyMaster(matrix, filename):
    print("=============================================")
    print("Tally results from Filename:  " + filename)
    print("=============================================")
    print("Answer to Question A")
    print("-------------------------")
    print (matrix)

    totalCount = countAllVotes(matrix)

    CandidatesTally = squashMatrix(matrix)
    CandidatesPercentage = countToPercent(CandidatesTally, totalCount)

    prettyPrintMatrix = prettyPrint(names, CandidatesTally, CandidatesPercentage)
    prettyPrintSorted = sortByCount(list(prettyPrintMatrix))

    print("-------------------------")
    print("Answer to Question B - Note List is sorted")
    print("-------------------------")
    print(prettyPrintSorted)

    print("-------------------------")
    print("Answer to Question C & D")
    print("-------------------------")
    printFinalResults(prettyPrintSorted)

# MAIN PROGRAM LOOP
matrix = readVotes("votes.txt")
tallyMaster(matrix, "votes.txt")

# for more /different input vote files:
matrix = readVotes("votesV2.txt")
tallyMaster(matrix, "votesV2.txt")


