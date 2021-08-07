import os
from mutagen.mp3 import MP3

def Directory():
    os.system("cls")
    directory = input(r"Input the location of the directory containing your music: ")
    if os.path.isdir(directory):
        os.chdir(directory)
        lengthGetter()
    else:
        os.system('cls')
        print("That location does not exist, try again")
        Directory()

def lengthGetter():
    totalLength = 0
    for files in os.listdir():
        fileName, fileExtension = os.path.splitext(files)
        if fileExtension == ".mp3":
            totalLength += MP3(files).info.length
    totalLength /= 60
    minutes = totalLength - (totalLength % 1)
    seconds = 300 * (totalLength % 1) / 5
    print (f"{int(minutes)} minutes {round(seconds,2)} seconds")
    input("Press enter to exit: ")

Directory()
