numeralDict = {
    1:'I',
    2:'II',
    3:'III',
    4:'IV',
    5:'V',
    6:'VI',
    7:'VII',
    8:'VIII',
    9:'IX',
    10:'X'
}

imputedNumber = int(input('What number do you want: '))

def romanNumeral():
    if imputedNumber in numeralDict:
      print(numeralDict[imputedNumber])
    
    else:
       print('Error, Was not found, Outside range')

romanNumeral()

#assuming i have the freedom to stray away from the list idea and use a dictionary