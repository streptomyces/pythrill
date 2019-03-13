# {{{ imports and other global stuff.
import sys
sys.path.append("/home/lucia/py3lib")
from lg import common as lgc

### Often needed
import os, glob, re, argparse, tempfile, gzip, random

### Used at least once
# from ftplib import FTP
# from Bio import SeqIO
# from Bio import Entrez
# from Bio.Seq import Seq
# from Bio.SeqRecord import SeqRecord
# import subprocess
# from Bio.Blast.Applications import NcbiblastpCommandline
# from Bio.Blast import NCBIXML

### from datetime
from datetime import datetime

### from collections
from collections import Counter
from collections import deque
# }}}

def main():
    lgc.linelist(args.infile)
    lgc.linelist(args.outfile)
    ifh = open(args.infile, 'r')
    ofh = open(args.outfile, 'w')
    for line in ifh:
        line= line.strip()
        ll= re.split(r'\t', line)
        acc = ll[0]
        taxid = ll[5]
        sptaxid = ll[6]
        #lgc.tablist([acc, taxid, sptaxid])
        lgc.tablist([taxid], handle = ofh)
    ofh.close()
    ifh.close()

# {{{ argparse and call to main()
if __name__ == "__main__":

### argparse stuff
    aps = argparse.ArgumentParser()
    aps.add_argument('--infile', '-i', help = "Input file.")
    aps.add_argument('--outfile', '-o', help = "Output file.")

    args = aps.parse_args();
    main()
# }}}
