#!/usr/bin/python

import os   
import shutil
import random
from shutil import copyfile
from shutil import copy2

sourcedir = 'E:/SteamGames/steamapps/common/Beat Saber/Beat Saber_Data/CustomLevels'
newdir = 'E:/BeatSaberSongs'

#os.mkdir(newdir);

for path, dirs, files in os.walk(sourcedir):
    for file in files:
        if file.endswith(".egg"):
            copy2(os.path.join(path, file), newdir)
        elif file.endswith(".ogg"):
            copy2(os.path.join(path, file), newdir)