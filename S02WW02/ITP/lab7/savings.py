initialBalance = float(input('input initial Balance: '))
percentInterest = float(input('Input annual interest: '))
desiredOutput = float(input('Input desired output amount: '))

def checkYear(output, balance):
    counter = 0
    while balance <= output:
        withInt = balance * percentInterest
        balance = balance + withInt  
        print(round(balance,2))
        counter = counter + 1
    else: 
        print(f'{counter} years to reach goal.')
        
checkYear(desiredOutput, initialBalance)