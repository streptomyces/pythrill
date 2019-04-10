import os, sys, stat, time,re
import hashlib
# import magicfile as magic

# {{{ def hasher(indir, fncnt) my replacement for findDup
def hasher(indir, fncnt):
    hashd = {}
    for thisdir, sudirs, bns in os.walk(indir):
        fncnt[thisdir] = len(bns)
        for bn in bns:
            fn = os.path.join(thisdir, bn)
            # if os.path.islink(fn):
            #     continue
            fnhash = hashfile(fn)
            if fnhash in hashd:
                hashd[fnhash].append(fn)
            else:
                hashd[fnhash] = [fn]
    return(hashd)
# }}}

# {{{ def findDup(parentFolder):
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
# }}}

# {{{ def daysMod(fn):
def daysMod(fn):
    curtime = time.time()
    timesinceEpoc = os.path.getmtime(fn)
    difftime = curtime - timesinceEpoc
    ndays = difftime/(60*60*24)
    return(ndays)
# }}}

# {{{ def daysAcc(fn):
def daysAcc(fn):
    curtime = time.time()
    timesinceEpoc = os.path.getatime(fn)
    difftime = curtime - timesinceEpoc
    ndays = difftime/(60*60*24)
    return(ndays)
# }}}

# {{{ def hashfile(path, blocksize = 65536):
def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
# }}}

# {{{ if __name__ == '__main__': Commented out for now
# if __name__ == '__main__':
#     if len(sys.argv) > 1:
#         dups = {}
#         folders = sys.argv[1:]
#         for i in folders:
#             # Iterate the folders given
#             if os.path.exists(i):
#                 # Find the duplicated files and append them to the dups
#                 joinDicts(dups, findDup(i))
#             else:
#                 print('%s is not a valid path, please verify' % i)
#                 continue
#                 #sys.exit()
#         printResults(dups)
#     else:
#         print('Usage:\npython3 '
#               +  sys.argv[0] +
#               ' folder\nor\npython3 '
#               + sys.argv[0] +
#               ' folder1 folder2 folder3')
# }}}

nfn = {}
hashd = hasher("data", nfn)


copies = {};
for k in hashd:
    if len(hashd[k]) > 1:
        copies[hashd[k][0]] = [", ".join(hashd[k][1:])]
    else:
        copies[hashd[k][0]] = ["-"]

# for k in copies:
#     print("{}, {}\n".format(k, copies[k]))


for prifn in copies:
    modified = int(daysMod(prifn))
    accessed = int(daysAcc(prifn))
    copies[prifn].append(accessed)
    copies[prifn].append(modified)
    copies[prifn].append(os.path.getsize(prifn))


for k in copies:
    l = copies[k]
    print("{}\t{}\t{:d}\t{:d}\t{:d}".format(k, l[0], l[1], l[2], l[3]))

print("{}".format("==================================="));
for k in nfn:
    print("{}/\t{}".format(k, nfn[k]))



'''
python3 pythrill/ffi.py
'''






