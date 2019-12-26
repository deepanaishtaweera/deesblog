import fileinput

extension = ".html"
pathName = "static/"
text_to_search = "http://localhost:2369/"
replacement_text = "https://deesblog.fyi/static/"

def replace_file(filename,text_to_search,replacement_text):
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace(text_to_search, replacement_text),end='')

import glob
import os
import os.path

for dirpath, dirnames, filenames in os.walk(pathName):
    for filename in [f for f in filenames if f.endswith(extension)]:
        tempFileName = os.path.join(dirpath, filename)
        replace_file(tempFileName,text_to_search,replacement_text)
        print(tempFileName)