#Master script
import sys
import os
import re
import stat
import time
import hashlib
import magicfile as magic
import argparse
from colorama import Fore, Back, Style

from duplicatefinder import dupcheck
from oldfilefinder import access_check
from bigfilefinder  import bigdir_check
from bigfolderfinder import  detect_folder_with_number_files
from compressfinder import isCompressed


if __name__ == '__main__':

   ## using argparse to get user input
   parser = argparse.ArgumentParser()
   parser.add_argument('--dirname',     help='Please enter directory name ')
   parser.add_argument('--days',        help='Number of days last accessed ')
   parser.add_argument('--size',        help='File size in bytes ')
   parser.add_argument('--filelimit',   help='specify number of files above which a directory is bigDir')

   args = parser.parse_args()

   mydir = args.dirname
   time_limit_days = float(args.days)
   size = float(args.size) # bytes
   filelimit = int(args.filelimit)


   # input validation
   if os.path.exists(mydir):

      print ('target directory:', mydir)

      #known_files = set()

      with open('files_to_investigate.csv', 'w') as outf:

          # dup write
          outf.write(','.join( ['Duplicate files'] ) + '\n')
          dups_block = dupcheck(mydir).items()
          for hexa, dupfiles in dups_block:
              outf.write(','.join( [hexa] + [ str(len(dupfiles)) ] + dupfiles ) + '\n')
          outf.write('\n')
          outf.write('=======================================================================================')
          outf.write('\n')

          # old write
          outf.write(','.join(  ['Files with chosen last access time'] ) + '\n')
          oldFileStatus =  access_check(mydir, time_limit_days) ## set  time here
          for hexa, dupfiles in dups_block:
              outf.write(','.join( [hexa] + [ str(len(dupfiles)) ] + [ x + ' (old)' if x in oldFileStatus else  '' for x in  dupfiles ] ) + '\n')
          outf.write('\n')
          outf.write('=======================================================================================')
          outf.write('\n')

          # Big file  write
          outf.write(','.join(  ['Files bigger than chosen bytes'] ) + '\n')
          sizeFileStatus =  bigdir_check(mydir,  size_limitKB = size) ## set  byte size here
          #print     sizeFileStatus

          for hexa, dupfiles in dups_block:
              outf.write(','.join( [hexa] + [ str(len(dupfiles)) ] + [ x + ' (overBytes:' + sizeFileStatus[x] + ')'     if x in sizeFileStatus else  '' for x in  dupfiles ] ) + '\n')
          outf.write('\n')
          outf.write('=======================================================================================')
          outf.write('\n')

          # Big folder
          outf.write(','.join(  ['Big directories'] ) + '\n')
          FatFolderS = detect_folder_with_number_files(mydir, files_allowed = filelimit )##  if file
          for fold, times in FatFolderS.items():
              outf.write(','.join( [fold] + [ str(times) ]) + '\n')
          outf.write('\n')
          outf.write('=======================================================================================')
          outf.write('\n')

          # Compression check
          outf.write(','.join(  ['Uncompressed files'] ) + '\n')
          for filer, compo in isCompressed(mydir).items():
              outf.write(','.join( [filer] + [ str(compo) ]) + '\n')
          outf.write('\n')
          outf.write('=======================================================================================')
          outf.write('\n')
      print ( 'Investigation done, please look at the output file!')
   else:
      print(Fore.RED +  'Error: ' +  mydir + ' directory does not exist')
      print(Style.RESET_ALL)
      exit()
