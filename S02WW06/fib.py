def FibI(n):
    """
    When we have n = 0, 1 or 2 to start - then we don't need
    to do recursion. Its only good > 2
    """
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        """
        the while will walk up the list and add a 
        new element based on the last and 2nd last
        current elements
        that new element then will be used next time
        around
        """
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence

"""
this is the heart of the recursion function

 """
def recursion(n, sequence):                             # <-¬
    """
    bounce up and fill a list n elements long.
    n will not really change for this problem.
    but it does control when we stop.
    """
    if len(sequence) < n:                               #    |
                        # [-1] = last, [-2] 2nd last    #    |
        sequence.append(sequence[-1] + sequence[-2])    #    |
        recursion(n, sequence)                          #  >-^

def FibR(n):
    """
    When we have n = 0, 1 or 2 to start - then we don't need
    to do recursion. Its only good > 2
    """
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        # bootstrap the start of the fib sequence to allow
        # the recursion to work. - i.e. we need a [-1] and [-2]
        fib_sequence = [0, 1]
        recursion(n, fib_sequence)
        return fib_sequence


num = int(input("Enter a positive integer:  "))
sequence = FibI(num)
print("Fibonacci sequence iterated:")
print(sequence)

sequence = FibR(num)
print("Fibonacci sequence Recursive:")
print(sequence)
