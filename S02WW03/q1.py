import string


programming_languages = ('php','java','python','c++','c')

print (programming_languages)

# Working on lambda first

capFn = lambda lang: string.upper(lang)

for lang in programming_languages:
    print(capFn(lang))

# Now with map function added

print ("Running the map funciton now")    
capped_programming_langs = map(capFn, programming_languages)

for lang in capped_programming_langs:
    print (lang)
# As a single line

print ("Trying as a single line")    
print (map(lambda lang: string.upper(lang),programming_languages))
