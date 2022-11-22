#with open closes the file automatically
try:
    # with open("C:\\Users\\91889\\OneDrive\\Desktop\\New folder\\Vijay CE.docx") as resume:
    with open("C:\\Users\\91889\\OneDrive\\Desktop\\New folder\\test.txt") as Testfile:
       print(Testfile.read())
except FileNotFoundError:
    print("This file does not exist")
print(Testfile.closed)