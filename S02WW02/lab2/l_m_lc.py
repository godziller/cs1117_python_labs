#question 1 
"""
programming_languages = ("php", "java", "python","c++", "c")

print(list(map(lambda x: (x,x), programming_languages)))

def tupleLower():
    print(tuple((x,x) for x in programming_languages))
tupleLower()
"""
#question 2 

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
newList = ['True' if word[0] == "A" else "False" for word in fruit] 
print(newList)