#question4 
import math

number = float(input("Input your number: "))
numberTwo = float(input('Input your second number: '))

def checkNumber(One, Two):
    if One == Two:
        print("numbers are to be square rooted")
        squareRoot(One)

    elif One != Two:
        print("numbers are to be squared")
        squareNumber(One)

def squareRoot(One):
    newNumber = math.sqrt(One)
    print(int(newNumber))

def squareNumber(One):
    newNumberToSqaure = One ** 2
    print(int(newNumberToSqaure))


checkNumber(number, numberTwo)