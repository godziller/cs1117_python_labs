askedNumber = int(input("Enter Number: "))
numberIndex = 1
s = 'Number {} is {}'

while numberIndex in range(1,10):
    tableNumber = numberIndex * askedNumber 
    numberIndex = numberIndex + 1
    #print(f'Number {numberIndex} is: {tableNumber}') # f string method 
    #print('Number', numberIndex,' is:', tableNumber) # classic
   # print(s.format(numberIndex, tableNumber)) #format method
    print('Number %d is %d' % (numberIndex, tableNumber)) #placeholder 