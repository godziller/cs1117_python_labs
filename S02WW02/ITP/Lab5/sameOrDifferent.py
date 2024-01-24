input1 = input('Input number one: ')
input2  = input('Input number two: ')
input3 = input('INput number three:  ')

def sameOrDifferent(num1,num2,num3):
    if num1 == num2 == num3: 
        print('They are the same')
        return True 
    else: 
        print('They dont match')
        return False

sameOrDifferent(input1, input2, input3)