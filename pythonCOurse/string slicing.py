# Slicing = create a substring by extracting elements from another string
# Functions = Indexing operator [] or slice()
# Arguments = [start:stop:step]

name = "Vijay Kumar"
FirstName = name[0:5]
LastName = name[6:]
FunkyName = name[0:11:2]  # prints every 2 char
ReversedName = name[::-1]

print(FirstName)
print(LastName)
print(FunkyName)
print(ReversedName)

#  FirstName = name[:5]  # Does the same function as above, python considers the starting index since it is left empty
#  LastName = name[6:]  # Does the same function as above, python considers the ending index since it is left empty


#  Slicing

WebSite1 = "http://google.com"
WebSite2 = "http://wikipedia.com"
WebSite3 = "http://instgram.com"

slice = slice(7, -4)
#  Here instead of using colan we are using comma, negative index starts from the end of the sentence,
#  so -4 implies that we are ignoring the last 4 char of the sentence

print(WebSite1[slice])
print(WebSite2[slice])
print(WebSite3[slice])