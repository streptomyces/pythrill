
import os
from collections import defaultdict

def bigdir_check(folder, size_limitKB = 1024):

    dir2size = {} #defaultdict(list)

    # Walk through all files and folders within directory
    # Just to make it simple we check the size of each file .. even with same md hashes
    for path, dirs, files in os.walk(folder):
       print("scanning {}".format(path))
       for filer in files:
            full_file_path = os.path.join(os.path.abspath(path), filer) # full path to file
            this_file_size = os.path.getsize(full_file_path)            #  size in KB
            if this_file_size > size_limitKB:                           # check if its bigger
               dir2size[full_file_path] = str(this_file_size)
    return dir2size


if __name__ == '__main__':

   ## big files check
   for hexa, bigfiles in bigdir_check(mydir,  size_limitKB = 1024).items():
       #if len(dupfiles) > 1:
       print (hexa, len(bigfiles), bigfiles)
