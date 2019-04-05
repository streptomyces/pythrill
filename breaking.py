import sys
from os import path
def ritefile():
    for fn in sys.argv[1:]:
        fh = open(fn, "wt")
        noex, ext = path.splitext(path.basename(fn))
        for i in range (1, 101):
            fh.write("{}_{:d}\n".format(noex, i))
        fh.close()





def findcommon(fn1, fn2):
    fh1 = open(fn1, "rt")
    fh2 = open(fn2, "rt")
    lc1 = int(0)
    for line1 in fh1:
        line1 = line1.strip()
        lc1 += 1;
        fh2.seek(0,0)
        lc2 = int(0)
        for line2 in fh2:
            line2 = line2.strip()
            lc2 += 1
            if line2 == line1:
                print("{:d} {} {} --- {:d} {} {}\n".format(
                lc1, fn1, line1, lc2, fn2, line2))
                #break

# ritefile()

findcommon(sys.argv[1], sys.argv[2])


