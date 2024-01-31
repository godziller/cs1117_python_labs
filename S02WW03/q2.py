# Without using lambdas
def starts_with_A(s):
    return s[0] == "A"
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(starts_with_A, fruit)
print(list(map_object))


# Using List comprehension

print("Using List Comprehension - same?")
newList = [True if word[0] == "A" else False for word in fruit] 
print(newList)
