import os, sys, stat, time,re
import hashlib
# import magicfile as magic

# {{{ def hasher(indir, fncnt). Cleaned up version of findDup().
# Argument 1 is directory to walk into
# Argument 2 in an empty dictionary in which keys will be
# directory names and values will be the number of files in
# them.
# Called as hasher(<path> <dictionary>)
# Return a dictionary in which keys are hashes and values
# are lists of file names
def hasher(indir, fncnt):
    hashd = {}
    for thisdir, sudirs, bns in os.walk(indir):
        dirbn = os.path.basename(thisdir)
        rem = re.match(r'^\.', dirbn)
        if rem:
            continue
        fncnt[thisdir] = len(bns)
        for bn in bns:
            fn = os.path.join(thisdir, bn)
            if os.path.islink(fn):
                continue
# Below does not work as expected. I think I know why
# but need time to fix. Basically, need to remove indir
# from the beginning of fn and then searching that with
# the RE below.
            #rem = re.search(r'\.[0-9A-Za-z]', fn)
            #if rem:
            #    continue
            fnhash = hashfile(fn)
            if fnhash in hashd:
                hashd[fnhash].append(fn)
            else:
                hashd[fnhash] = [fn]
    return(hashd)
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
hashd = hasher(sys.argv[1], nfn)

# hashd has hashes as keys and lists of files as values. These
# lists will have at least one member.

# Below we make a dictionary called copies in which the first
# filenames of the lists in hashd are keys and values are the 
# rest of the filenames separated by commas. These values are
# lists containing just one string. If there is no copy for a filename
# then the list contains "-".
copies = {};
for k in hashd:
    if len(hashd[k]) > 1:
        copies[hashd[k][0]] = [", ".join(hashd[k][1:])]
    else:
        copies[hashd[k][0]] = ["-"]


# Now we add some information about the files to the lists
# which are the values of the copies dictionary.
for prifn in copies:
    modified = int(daysMod(prifn))
    accessed = int(daysAcc(prifn))
    copies[prifn].append(accessed)
    copies[prifn].append(modified)
    copies[prifn].append(os.path.getsize(prifn))


print("#{}\t{}\t{}\t{}\t{}".format("File", "Copies", "AccDays",
                                         "ModDays", "Bytes"))


for k in copies:
    l = copies[k]
    print("{}\t{}\t{:d}\t{:d}\t{:d}".format(k, l[0], l[1], l[2], l[3]))


print()
# print("{}".format("### Number of files in directories ###"))
print("#{}\t{}".format("Directory", "NumFiles"))
for k in nfn:
    print("{}/\t{}".format(k, nfn[k]))



'''
python3 pythrill/ffi.py
'''






