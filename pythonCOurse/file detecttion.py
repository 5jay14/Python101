import os

#path ="C:\\Users\\91889\\OneDrive\\Desktop\\New folder\\test.txt.txt"
path ="C:\\Users\\91889\\OneDrive\\Desktop\\New folder\\Vijay CE.docx"

#path ="C:\\Users\\91889\\OneDrive\\Desktop\\New folder" # folder

if os.path.exists(path):
    print("That location exist")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a Directory")
else:
    print("That location does not exist")
