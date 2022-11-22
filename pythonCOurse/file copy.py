# copyfile() = copies the contents of the file
# copy       = copyfile() + permission mode + destination can be directory
# copy2      = copy() + copies metadata(Files creation and modification time)


import shutil

shutil.copy2("C:\\Users\\91889\\OneDrive\\Desktop\\New folder\\test.txt",
             "C:\\Users\\91889\\OneDrive\\Desktop\\New folder\\test1.txt")
#  same
#  shutil.copyfile("C:\\Users\\91889\\OneDrive\\Desktop\\New folder\\test.txt","C:\\Users\\91889\\OneDrive\\Desktop\\New folder\\test1.txt")
#  shutil.copy("C:\\Users\\91889\\OneDrive\\Desktop\\New folder\\test.txt","C:\\Users\\91889\\OneDrive\\Desktop\\New folder\\test1.txt"

# Can also copy the file within the project to locally
shutil.copy2("abc",
             "C:\\Users\\91889\\OneDrive\\Desktop\\New folder\\test2.txt")