import os

def Directory():
    os.system('cls')
    directory = input(r"Input the location of the directory containing the files you want deleted: ")
    file_type = input(r"Input the file extension for the files you wish to delete: ")
    if os.path.isdir(directory):
        os.chdir(directory)
        print(os.getcwd())
        Deleting(file_type)
    else:
        print("That location does not exist, try again")
        Directory()

def Deleting(file_type):
    for files in os.listdir():
        file_name, file_extension = os.path.splitext(files)
        if file_extension == file_type:
            
            os.remove(file_name + file_extension)
        

Directory()