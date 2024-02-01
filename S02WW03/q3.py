#zipWith = map(lambda n1, n2: n1 – n2, [7,8,9], [3,2,1])

# Zip with is just our varible 
#there is an error to this as the bracket is unclosed so there will be an error for the output 

#part b

def zip_with(iterable1, iterable2, func):
    result = []
    for n1, n2 in zip(iterable1, iterable2):
        result.append(func(n1, n2))
    return result

# Example invocation
list1 = [7, 8, 9]
list2 = [3, 2, 1]

result = zip_with(list1, list2, lambda n1, n2: n1 - n2)
print(result)


#part c

def loop():
    for n in range(17):
        if n > 10:
            print("summation")

summation = loop()