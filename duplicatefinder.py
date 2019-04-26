import os
import hashlib
from collections import defaultdict


def hashfile(filer, chunk_size = 5000):
    """
    this digest the file and returns a md5 hash
    # print hashfile('test.txt')

    """
    hasher = hashlib.md5()
    with open(filer, 'rb') as f:
      buffer = f.read(chunk_size)
      while buffer:
        hasher.update(buffer)
        buffer = f.read(chunk_size)
    return hasher.hexdigest()

def dupcheck(folder):

    file2hash = defaultdict(list)

    # Walk through all files and folders within directory
    for path, dirs, files in os.walk(folder):
        for filer in files:
            full_file_path = os.path.join(os.path.abspath(path), filer)
            hex_string = hashfile(full_file_path, chunk_size = 5000)
            file2hash[hex_string].append(full_file_path)
    return file2hash


if __name__ == '__main__':

   for hexa, dupfiles in dupcheck(mydir).items():
       print ( hexa, len(dupfiles), dupfiles )
