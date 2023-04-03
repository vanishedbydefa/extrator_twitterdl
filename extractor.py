import os
from zipfile import ZipFile
import time

tw_path = "PATH TO FOLDER WHERE THE ZIPS ARE"
tw_folder = os.listdir(tw_path)

def extract(zip_file,extr_location):
    with ZipFile(zip_file, 'r') as zObject:
        zObject.extractall(path=extr_location)

zip_folder = []
for files in tw_folder:
    if str(files[-4:]) == ".zip": 
        zip_folder.append(files)
        print(files)
        
        tw_folder_name = files.split("-",1)[0]
        

        to_extr_location = tw_path + "\\" + tw_folder_name
        if os.path.isdir(to_extr_location):
            extract(tw_path + "\\" + files, to_extr_location)
        else:
            os.makedirs(to_extr_location)
            extract(tw_path + "\\" + files, to_extr_location)

        os.rename(tw_path + "\\" + files, tw_path + "\\" + tw_folder_name + "\\" + files)

