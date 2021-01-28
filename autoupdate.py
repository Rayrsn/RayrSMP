import urllib
from urllib.request import urlopen
link = "https://raw.githubusercontent.com/Rayrsn/RayrMC/main/version"
x = urlopen(link)
verfile = x.read()
str(verfile, encoding='utf-8')
print(verfile)
import os

#checks the current version
def check_cur_ver():
    path = os.environ['APPDATA']
    verfilepath = (path + '\.minecraft\mods')
    f = open(verfilepath + "\\" + 'version', 'rb')
    z = f.read()
    #reads the version file located in mods folder
    print(z)
    if z != verfile:
        print('not updated')
    else:
        print('updated')
##########

#writes version to mods folder
def write_to_file():
    path = os.environ['APPDATA']
    verfilepath = (path + '\.minecraft\mods')
    f = open(verfilepath + "\\" + 'version', 'wb')
    f.write(verfile)
###########

check_cur_ver()
