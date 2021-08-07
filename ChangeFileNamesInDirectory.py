import os

def Directory():
    directory = input(r"Input the location of the directory containing the files you want to be renamed: ")
    if os.path.isdir(directory):
        os.chdir(directory)
        print(os.getcwd())
        NewName()
    else:
        print("That location does not exist, try again")
        Directory()

def NewName():
    fileName = input("What name would you like the files to have? ")
    if "yes" in input(f"Are you certain that you want to rename all files in {os.getcwd()} to {fileName}? "):
        Rename(fileName)
    else:
        Directory()

def Rename(fileName):
    count = 1
    for files in os.listdir():
        file_name, file_extension = os.path.splitext(files)
        file_name = fileName + str(count)
        count += 1

        newName = file_name + file_extension
        os.rename(files,newName)

    if "yes" in input("Would you like to rename more files? "):
        Directory()
    else:
        quit()

Directory()



