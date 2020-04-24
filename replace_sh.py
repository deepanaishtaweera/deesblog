import glob
from distutils.dir_util import copy_tree
import os.path
import os
import fileinput

extension = ".html"
pathName = "docs/"
text_to_search = "http://localhost:2369/"
replacement_text = "https://deesblog.fyi/"


def replace_file(filename, text_to_search, replacement_text):
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace(text_to_search, replacement_text), end='')

def add_missing_tags(filename):
    start_text = '<!DOCTYPE html> \n<html lang="en"> \n'
    end_text = "</html>"
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            if file.isfirstline():
                if "html" not in line:
                    print(start_text, end='')
            if end_text not in line:
                print(line, end='')
            if "</body>" in line:
                print(end_text, end = '')


for dirpath, dirnames, filenames in os.walk(pathName):
    for filename in [f for f in filenames if f.endswith(extension)]:
        tempFileName = os.path.join(dirpath, filename)
        replace_file(tempFileName, text_to_search, replacement_text)
        # replace_file(tempFileName, "shortcut icon", "icon")
        replace_file(tempFileName, ".pngg", ".png")
        replace_file(tempFileName, ".pngng", ".png")
        replace_file(tempFileName, ".pngpng", ".png")
        replace_file(tempFileName, ".jpgg", ".jpg")
        replace_file(tempFileName, ".jpgpg", ".jpg")
        replace_file(tempFileName, ".jpgjpg", ".jpg")
        replace_file(tempFileName, ".JPGG", ".JPG")
        replace_file(tempFileName, ".JPGPG", ".JPG")
        replace_file(tempFileName, ".JPGJPG", ".JPG")
        add_missing_tags(tempFileName)
        print(tempFileName)


print(os.getcwd())
# copy subdirectory example
# fromDirectory = os.getcwd() + "/content/images/"
# toDirectory = os.getcwd() + "/docs/content/images/"

# copy_tree(fromDirectory, toDirectory)

# fromDirectory = os.getcwd() + "/content/images/2019"
# toDirectory = os.getcwd() + "/docs/content/images/2019"

# copy_tree(fromDirectory, toDirectory)

# fromDirectory = os.getcwd() + "/content/images/2020"
# toDirectory = os.getcwd() + "/docs/content/images/2020"

# copy_tree(fromDirectory, toDirectory)