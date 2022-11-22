import os

source = "a move file"  ## local file within the project
destination ="C:\\Users\\91889\\OneDrive\\Desktop\\test.txt"

# moving folder has the same steps as moving the file, just that folder does not end with extensions
#  can move files or folders within the project > local system,  local system > project , local system > local system (different location)


try:
    if os.path.exists(destination):
        print("there is already a file")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print("source file not found")