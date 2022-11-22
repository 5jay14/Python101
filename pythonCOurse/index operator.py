# index operator [] = gives access to a sequence's element (str,list,tuple)

name = "vijay Kumar!"

if name[0].islower():
    name = name.capitalize()
    print(name)

firstName = name[0:5].upper()
lastName = name[6:].lower()
lastCharacter = name[-1]

print(firstName)
print(lastName)
print(lastCharacter)
