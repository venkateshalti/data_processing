# let's explore sub-folders and files at a given location
# first we can get the location of where current python file is, then we can identify files and directories within

import os

print("current location is:", os.path.dirname(os.path.realpath(__file__)))
print("current working directory is:", os.getcwd())

curr_loc = os.path.dirname(os.path.realpath(__file__))  # location of current python script

# the os.walk will traverse everything including sub-folders
# hence, it is important to store files at a location with no sub-folders
for root, dirs, files in os.walk(curr_loc):  # location, sub-directories list and files list at current location
    print("root:", root, '\n', "dirs:", dirs, '\n', "files:", files)
    all_paths = []
    for file in files:
        #print("file:", file)
        print("filepath:", root+'\\'+file)
        all_paths.append(root+'\\'+file)

print(open(all_paths[5], 'r').read())