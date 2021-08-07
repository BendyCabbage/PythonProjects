from __future__ import unicode_literals
import youtube_dl
from pydub import AudioSegment
import os

url = input("Input a Youtube URL: ")
options = {
    "format" : "bestaudio/best",
    "forcefilename" : True,
    "restrictfilenames" : True,
    "postprocessors" : [{
        'key' : "FFmpegExtractAudio",
         
    }]
}
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([url])

os.chdir(r"F:\Downloads")
for i in os.getcwd():
    filename, fileExtension = os.path.splitext(i)
    if fileExtension == ".webm":
        AudioSegment.from_file(i).export(filename + ".mp3", format = "mp3")


