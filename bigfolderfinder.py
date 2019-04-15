import os

def detect_folder_with_number_files(mydir ='data/', files_allowed = 3 ):
   """
   Check if a folder is big or not
   Example if files_allowed = 100,
   The folder containing 100 or more files will be a big folder
   """
   bigfolders = {} #defaultdict(int)
   for path, dirs, files in os.walk(mydir):
       dirname = os.path.abspath(path)
       bigfolders[dirname] =  len(files)
   return bigfolders



if __name__ == '__main__':

   ## big directory check
   bigfolders = detect_folder_with_number_files(mydir , files_allowed = 5 )##  if file
   for bigfold, numFiles in bigfolders.items():
       print (bigfold, numFiles)
