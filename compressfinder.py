import os
import magicfile as magic


def compStatus(fn):
    f = magic.Magic(uncompress=True)
    file_status = f.from_file(fn)
    if not 'compressed' in  file_status:
        return True

def isCompressed(mydir ='data/'):
   """
   Compression check
   """

   compresseD = {} #defaultdict(list)

   # Walk through all files and folders within directory
   # Just to make it simple we check the size of each file .. even with same md hashes
   for path, dirs, files in os.walk(mydir):
       print("scanning {}".format(path))
       for filer in files:
            full_file_path = os.path.join(os.path.abspath(path), filer) # full path to file
            if compStatus(full_file_path):                           # check if its bigger
               compresseD[full_file_path] =  "Uncompressed"
   return compresseD



if __name__ == '__main__':

   ## big directory check

   for bigfold, numFiles in isCompressed(mydir).items():
       print (bigfold, numFiles)
