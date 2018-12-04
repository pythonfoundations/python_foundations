from urllib import request
import requests

from bs4 import BeautifulSoup

name_dir =  input("input name of directory")


name_link = "https://football.ua/"
site = requests.get(name_link).content
soup = BeautifulSoup(site, features="lxml")
link = soup.findAll("img")
n = 0
for i  in link:
    try:
        n = n + 1
        name_dir_1 = name_dir + "/" + str(n) + ".jpg"
        request.urlretrieve(i["src"], name_dir_1)
    except ValueError:
        pass
        print("Invalid link = ", i["src"] )
print("Imeges was loaded at" + name_dir)