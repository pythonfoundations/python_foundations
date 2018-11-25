from PIL import Image
from PIL.ExifTags import TAGS
import os, sys, shutil, copy
print("This program can do 2 actions \n1st: change the name of the photos in the folder to the date they were created"
      "\n2nd: create copies of all photos in the folder.\nTo make 1st action input 'replace'.\nTo make 2nd"
      "action input 'copy'")


def get_meta_data (dir):
    l = ["replace", "copy"]
    action = input("input your action ")
    if action not in l:
        return get_meta_data(dir)
    files = os.listdir(dir)
    calculate = 0
    for i in files:
        calculate = calculate + 1
        pic = Image.open(dir + "/"+ i)
        info = pic._getexif()
        date = info.get(306)
        pic_0 = dir + "/"+ str(i)
        pic_1 = dir + "/"+ str(date) + ".jpg"
        if action == "replace":
            replace(pic_0, pic_1)
        elif action == "copy":
            copy_photo(pic_0, dir, i,  calculate)


def replace (name_1, name_2):
    os.rename(name_1, name_2)

def copy_photo (pic_0, dir, i,  calculate):
    pic_2 = dir + "/" + i + "__" + str(calculate) + ".jpg"
    shutil.copyfile(pic_0, pic_2)

get_meta_data(input("Input way to your directory"))