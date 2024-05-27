import fileinput
import re
import csv
import os
import shutil
from shutil import copyfile
import datetime
'''
The OS module 
Python’s OS module, or the miscellaneous operating system interface, is very useful for file operations, directories, and permissions. 
Let’s take a look at each.
File operations
File names can be thought of as two names separated by a dot. 
For example, helloworld.txt is the file name and the extension defines the file type. OS provides functions to create, read, update, and delete files. 
Some of the basic functions include:

Opening and closing files
Reading from and writing to files
Appending to files

Directories

OS also provides functions to create, read, update, and delete directories, as well as change directories and list files. 
Knowing how to use these functions is key to working with files. For example, os.listdir( path ) returns a list of all files and subdirectories in a directory.
Permissions

Having the ability to update file permissions is an important aspect of making installations from a terminal window. 
The os.chmod() provides the ability to create, read, and update permissions for individuals or groups.
Things to keep in mind  

One thing to be aware of is that Python treats text and binary files differently. Because Python is cross-platform, 
it tries to automatically handle different ASCII line endings. If you’re processing a binary file, 
make sure to open it in binary mode so Python doesnt try to “fix” newlines in a binary file.

A best practice is to always close() a file when you’re done reading or writing to it. 
Even though Python usually closes them for you, it’s a good signal to other people reading your code that you’re done with that file.
Make sure to catch any potential errors from filesystem calls, such as permission denied, file not found, and so on. 
Generally, you wrap them in try/except to handle those errors.
Key takeaways

There are several ways to manage files and directories in Python. 
One way is to use low-level functions in the OS and SYS modules that closely mimic standard Linux commands. 
Another way is to utilize the Pathlib module, which provides an object-oriented interface to working with the file systems. 



'''

#print(os.environ.get('PATH'))
#print(os.getcwd())
#os.chdir("..")
#print(os.getcwd())

#print (os.path.abspath(os.getcwd()))

def FileOperator(rootDir, operation, destDir):
    file_counter = 0
    folder_size = 0
    folder_counter = 0

    file_counter2 = 0
    folder_size2 = 0
    folder_counter2 = 0

    if operation == "delete tree":
        print ("Removing all files and folders in " + rootDir)
        shutil.rmtree(rootDir)

    elif operation == "archive":
        print("Archiving folder " + rootDir)
        shutil.make_archive(rootDir, 'zip', rootDir)

    elif operation == "copy-paste":
        print("Copy pasting from " + rootDir + "to " + destDir)

    elif operation == "delete empty folders":
        for dirName, subListDirList, fileList in os.walk(rootDir, topdown=False):
            for d_name in subListDirList:
                print("Deleting subdir: " + d_name)
                os.rmdir(os.path.join(dirName, d_name))
        print ("Deleting root dir: ")
        os.rmdir(rootDir)

    elif operation == "get absolute path":
        print("absolute path is " + os.path.abspath(rootDir))

    elif operation == "list subdirs and files":
        '''
        for each_name in os.listdir(rootDir):
            fullname = os.path.join(each_name, rootDir)
            if os.path.isdir(fullname):
                print("{} is a directory ".format(fullname))
            else:
                print("{} is a file ".format(fullname))
'''

        print(".".join(str(x) for x in os.listdir(rootDir)))





def create_python_script(filename):
    comments = "# Start of a new Python program"
    my_file = os.path.join(os.getcwd(), filename)
    with open(my_file , 'w') as new_file:
        new_file.write(comments)
        new_file.close()
    return(os.path.getsize(my_file))

print(create_python_script("program.py"))


def parent_directory():
    relative_parent = os.path.join(os.getcwd(), os.pardir)
    return os.path.abspath(relative_parent)


def file_date(filename):
        # Create the file in the current directory
        with open(filename, 'w') as file:
            pass
        timestamp = os.path.getmtime(filename)
        # Convert the timestamp into a readable format, then into a string
        date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
        # Return just the date portion
        # Hint: how many characters are in “yyyy-mm-dd”?
        return ("{}".format(date))

    # Return the absolute path of the parent directory


  # Return the absolute path of the parent directory

def main():
    FileOperator(os.getcwd(),"get absolute path", "N/A")
    FileOperator(os.getcwd(), "list subdirs and files", "N/A")
   # FileOperator(os.chdir(".."), "list subdirs and files", "N/A")
    print(parent_directory())

if __name__ == "__main__":
    main()






