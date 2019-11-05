#!usr/bin/python

import os, shutil, glob

dir = 'E:/BeatSaberSongs'

#for filename in os.listdir(dir)   
#        if file.endswith(".egg"):
 #           oldbase = os.path.splitext(filename)
 #           newname = 
            
l = os.listdir(dir) #With Extension
l = [x.lower() for x in l]
li = [x.split('.')[0] for x in l] #With No Extension

for filename in glob.iglob(os.path.join(dir, '*.egg')):     
    print(filename)
    fname2 = filename.split('.')[0] 
    fname2 = filename.split('\\')[1][:-4] + '.ogg'
    fname = filename.split('\\')[1]
    print(fname + ' Should be .egg')
    print(fname2 + ' Should be .ogg')
    print(l)
    if fname2.lower() in l:
        print('Already an ogg')        
        os.remove(filename[:-4] + '.ogg')
        os.rename(filename, filename[:-4] + '.ogg')
        continue

    elif fname2.lower() not in l:
        print('No ogg, renaming...')
        #os.remove(fname + '.ogg')
        os.rename(filename, filename[:-4] + '.ogg')