counter = int(input('Input a number of  bottles: '))

def blastOff(c):

    while c != 0:
        print(c)
        c = c - 1
        #only using this because question does not ask to use counter variable later, i am aware it
        #resets the base value each time which could otherwise been seen as destructive or bad.
    if c == 0:
        print('BLAST OFF')

blastOff(counter)


