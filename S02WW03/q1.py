import string


programming_languages = ('php','java','python','c++','c')

print (programming_languages)

# Working on lambda first

capFn = lambda lang: string.upper(lang)

for lang in programming_languages:
    print(capFn(lang))


