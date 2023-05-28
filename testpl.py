import os
import glob
import time
import string

numsong = 1

folder = r'/home/konstantinosthegreat/Music/YouTube Downloads/'
sortedlst = list(filter(os.path.isfile, glob.glob(folder +'*mp3')))
print (sortedlst)
#files = list(filter(os.path.isfile, glob.glob(folder +'*mp3')))
#files = glob.glob('*.mp3')
#filef = sorted(folder, key=os.path.getmtime)
#print(filef)
for file in os.listdir(folder) :
    print(file)
    #source = folder + file
    #destination = folder + str(numsong) + '_' + file
    #os.rename (source, destination)
    #numsong += 1
