import glob
from distutils.dir_util import copy_tree
import os.path
import os
import fileinput

extension = ".html"
pathName = "static/"
text_to_search = "http://localhost:2369/"
replacement_text = "https://deesblog.fyi/static/"


def replace_file(filename, text_to_search, replacement_text):
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace(text_to_search, replacement_text), end='')


for dirpath, dirnames, filenames in os.walk(pathName):
    for filename in [f for f in filenames if f.endswith(extension)]:
        tempFileName = os.path.join(dirpath, filename)
        replace_file(tempFileName, text_to_search, replacement_text)
        replace_file(tempFileName, "shortcut icon", "icon")
        replace_file(tempFileName, ".pngg", ".png")
        replace_file(tempFileName, ".pngng", ".png")
        replace_file(tempFileName, ".pngpng", ".png")
        replace_file(tempFileName, ".jpgg", ".jpg")
        replace_file(tempFileName, ".jpgpg", ".jpg")
        replace_file(tempFileName, ".jpgjpg", ".jpg")
        replace_file(tempFileName, ".JPGG", ".JPG")
        replace_file(tempFileName, ".JPGPG", ".JPG")
        replace_file(tempFileName, ".JPGJPG", ".JPG")
        print(tempFileName)


print(os.getcwd())
# copy subdirectory example
fromDirectory = os.getcwd() + "/content/images/2019"
toDirectory = os.getcwd() + "/static/content/images/2019"

copy_tree(fromDirectory, toDirectory)
