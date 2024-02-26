'''
a) Write an iterative function HailstoneI that generates the hailstone sequence of a 
given positive number n and prints the sequence to the screen. 

The ‘hailstone’ sequence starts with a positive integer and defines the next number 
in the sequence as follows: if n is even, the next value is n/2. 
If n is odd, the next value is 3n + 1. 
The sequence will converge to 1 and should print DONE. 
For example, if we consider a starting value of 10, 
the sequence is 10, 5, 16, 8, 4, 2, 1, DONE. 

b) Write a recursive version of the function from part (a) called HailstoneR that also accepts a number n as an input parameter. 	
'''

#The iteration function
def HailstoneI(n):
    print(n, end=" ")
    # This is where we break out of the iteration. When we hit 1.
    while n != 1:
        if n % 2 == 0:
            # need to keep n an int, without the cast, it could be a float.
            n = int(n / 2)
        else:
            n = 3 * n + 1
        print(n, end=" ")

# Note - both these functions depends on us dealing with ints.
# Things mess up if we use floats.

#The Recursion function
def HailstoneR(n):
    print(n, end=" ")
    if n == 1:
        # This is where we break out of the recursion. When we hit 1.
        return
    # The even number case
    elif n % 2 == 0:
        # need to keep n an int, without the cast, it could be a float.
        HailstoneR(int(n/2))
    # else the odd number case
    else:
        HailstoneR(3 * n + 1)

# The main body - take in an integer and fire the 2 funcs.
num = int(input("Let it rain!!! - enter a positive integer: "))

if num <= 0:
    print("hey Thor, I said a positive number please: ")
else:
    print("Your Hailstone sequence via Iteration:")
    HailstoneI(num)
    print('')
    print("Your Hailstone sequence via Recursion:")
    HailstoneI(num)
    print('')
