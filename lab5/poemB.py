import os 
inFile = open('debanks.txt', 'r')
lineCounter = 1 
#B
lyrics = inFile.read
lyrics = str(lyrics).strip('\n')
for lyrics in inFile:
    lineCounter = lineCounter + 1
    print(f'LINE: {lineCounter}')
    if lyrics != '':
        print(lyrics)
