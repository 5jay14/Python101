#everytime we run the program, text keeps getting added
# with open function can take second arguments, open, read/write.
# by default it is in read
# w =overwrites
# a = appends

#text = "this is a comment entered from python\nusing backward slash followed by n goes to next line"
text1 = "\ni am appendng some strings"
with open("C:\\Users\\91889\\OneDrive\\Desktop\\New folder\\test.txt", "a") as TestFile:
    TestFile.write(text1)

with open ("C:\\Users\\91889\\OneDrive\\Desktop\\New folder\\test.txt") as TestFile:
    print(TestFile.read())