MASK = "*"
import string

def generate_banned_words():
    bannedWords = []
    file = open("bannedWords.txt", "r")
    for word in file.read().split():
        bannedWords.append(word)
    file.close()
    return bannedWords


def censor_file(filename):
    censoredFile = open(filename, "r")
    cleanFile = open('cleanText.txt', "w")
    
    totalPara = ''
            
    for line in censoredFile.readlines():
        for word in line.split(): 
            for bleep in bannedList:
                if bleep in word.lower():
                    for letter in word:
                        if letter in string.ascii_letters:
                            word = word.replace(letter, MASK)

            totalPara = totalPara + word + ' '
        cleanFile.write(totalPara + '\n')
        print(totalPara )
        totalPara = ''
    
    cleanFile.close()
    censoredFile.close()
    
generate_banned_words()
bannedList = generate_banned_words()
censor_file("someText.txt")
