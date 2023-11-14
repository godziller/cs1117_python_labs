import os 

#a

lineCount = 1
inFile = open('debanks.txt','r')
lyrics = inFile.readlines()
lyric = str(lyrics).strip('\n')


for lyric in lyrics:
    print(lyric)
    lineCount = lineCount + 1
    print(f'LINE: {lineCount}')

inFile.close


