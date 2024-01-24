inputNumber = int(input('Insert a odd or even int: '))

def oddOrEven(inNum):
    if inNum % 2 == 0:
        print('The number is Even')
    else:
        print('The number is odd')

oddOrEven(inputNumber)