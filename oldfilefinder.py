import os
import datetime
from collections import defaultdict


def access_check(folder, time_limit_days ):
    oldFiles = {}
    # Walk through all files and folders within directory
    # Just to make it simple we check the size of each file .. even with same md hashes
    for path, dirs, files in os.walk(folder):
       print("scanning {}".format(path))
       for filer in files:

            full_file_path = os.path.join(os.path.abspath(path), filer) # full path to file
            this_file_age  = os.path.getsize(full_file_path)            #  size in bytes

            atime     = datetime.datetime.fromtimestamp(os.stat(full_file_path).st_atime)  # access time
            time_limit_days_unit = datetime.timedelta(days = time_limit_days)

            age =  datetime.datetime.now() - atime
            if age > time_limit_days_unit:
               oldFiles[full_file_path] = age
    return oldFiles


if __name__ == '__main__':

   ## access files check
   for hexa, oldfiles in access_check(mydir, time_limit_days = 0.0).items():
       print  (hexa,  oldfiles)
