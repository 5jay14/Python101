import os
import shutil

# os.remove('delete file')
# local file == give the file location
# project file = just the name works
# shutil module is needed to delete a folder that contains a file

# other way, assign the loication to the variable and use the variable as an argument

# path = "delete file"
# path = "empty dir"
path = (".idea")

try:
    # os.remove(path) # delete file
    # os.rmdir(path)  # delete the empty folder
    shutil.rmtree(path)  # delete a directory containing files

except FileNotFoundError:
    print("file not found")
except:
    print("Task processed")
else:
    print(path + " was deleted")
