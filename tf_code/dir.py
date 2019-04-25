import os
path = '/home/pi/motion catch/code/data'
for dirpath,dirnames,filenames in os.walk(path):
    for file in filenames:
        fullpath=os.path.join(dirpath,file)
        print(fullpath)