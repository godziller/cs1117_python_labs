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
list = (list(map(lambda x: (x), fruit)))
for fruits in fruit:
    if "a" or "A" in fruits[0]:
        print("True")
    else:
        print("false")