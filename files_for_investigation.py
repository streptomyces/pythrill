import os, sys, stat, time,re
import hashlib
import magicfile as magic

def findDup(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print(str(len(fileList)) + "\t" +  dirName)
        dotstart = (os.path.basename(os.path.normpath(dirName)))
        #if dirName.startswith('.'): #ignore dirnames with dotstart
            #continue
        #print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            if os.path.islink(path) : #or path.startswith('.'): #irnore sym links and files starting with dot
                continue
            curtime = time.time()
            accessTimesinceEpoc = os.path.getmtime(path)
            difftime = curtime - accessTimesinceEpoc
            daysMod = difftime/(60*60*24)
            filesizeInBytes = os.path.getsize(path)
            f = magic.Magic(mime=True, uncompress=True) #Only look for uncompressed files
            file_status = f.from_file(path)
            print (path + "\t" + str(accessTimesinceEpoc) + "\t" + str(curtime) + "\t" + str(difftime)
            + "\t" + str(daysMod) + "\t" + str(filesizeInBytes) + "\t" + file_status)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups


# Joins two dictionaries
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]


def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def printResults(dict1):
    total_dir_size = 0
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results) > 0:
        #print('Duplicates Found:')
        #print('The following files are identical. The name could differ, but the content is identical')
        print("Duplicated Filename\tLast access time \t Filesize (bytes)\t Dirsize (bytes)")
        print('___________________')
        for result in results:
            for subresult in result:
                accessTimesinceEpoc = os.path.getatime(subresult)
                accessTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(accessTimesinceEpoc))
                filesizeInBytes = os.path.getsize(subresult)
                #print('%s' % subresult + "\t" + accessTime + "\t" + str(filesizeInBytes))
                #print('%s' % subresult + "\t" + str(total_dir_size))
            print('___________________')

    else:
        print('No duplicate files found.')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        dups = {}
        folders = sys.argv[1:]
        for i in folders:
            # Iterate the folders given
            if os.path.exists(i):
                # Find the duplicated files and append them to the dups
                joinDicts(dups, findDup(i))
            else:
                print('%s is not a valid path, please verify' % i)
                continue
                #sys.exit()
        printResults(dups)
    else:
        print('Usage:\npython3 '
              +  sys.argv[0] +
              ' folder\nor\npython3 '
              + sys.argv[0] +
              ' folder1 folder2 folder3')
