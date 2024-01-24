
"""
#qestion 1 a) 

def getSquareColor(x,y):
    if y <= 7 and x <= 7:
        if y % 2 == 0 and x % 2 == 0:
            print('white')
        elif y % 2 != 0 and x % 2 == 0:
            print('black')
        elif y % 2 == 0 and x % 2 != 0:
            print('black')
        elif y % 2 != 0 and x % 2 != 0:
            print('white')
    else:
        print('invalid')

row = int(input("please enter row number: "))
col = int(input('please enter col number: '))
getSquareColor(row, col)

"""


"""
#question 1 b) 

def convertToUpper(word):
    for letter in word:
        biggerWord = str(letter).upper().strip()
        completeWord = biggerWord[len(biggerWord) - 1]
        print(completeWord, end='')
    

ourWord = input('input a word you would like converted: ')
convertToUpper(ourWord)    
"""

"""
#question 1 c i) 

def getWordLengths(sentence):
   splitSent = str(sentence).split(' ')
   for word in splitSent:
      print(len(word))

ourSentence = input('enter your words: ')
getWordLengths(ourSentence)
"""

'''
#question 1 c ii) 
ourList = []
def getWordLengths(sentence):
   ourList.append(str(sentence).split(' ')) 
   for word in ourList:
      print(list(map(lambda s: len(s), word)))



ourSentence = input('enter your words: ')
getWordLengths(ourSentence)
'''

'''
# question1 part d) 

def buildWordUpandDown(word):
    counter = 0
    while counter <= len(word):
        print(word[:counter])
        counter = counter + 1
    if counter > len(word):
        while counter != 0:
            print(word[:counter])
            counter -= 1

ourWord = input('enter your word please: ')
buildWordUpandDown(ourWord)
'''

#question2 a) 


#question2 a) 

punctuation = ['!','.', ',', ';', ':', '?']

def checkingWords(sentence, list):
    for words in sentence:
        print(words)
        for letters in words:
            if str(letters) in list: 
                str(words).strip(letters)
                print(sentence)
ourSentence = input('input your sentence: ')
checkingWords(ourSentence, punctuation)