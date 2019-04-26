#!/usr/bin/env python3
import warnings
warnings.filterwarnings("ignore")
import sys
from Bio import SeqIO

def main():
  donepairs = [];
  #print(sys.argv[1:])
  ifns = sys.argv[1:]
  for ifn in ifns:
    for ifn1 in ifns:
      if ifn != ifn1:
        p1 = "--".join([ifn, ifn1])
        p2 = "--".join([ifn1, ifn])
        if p1 not in donepairs and p2 not in donepairs:
          donepairs.append(p1)
          donepairs.append(p2)
          fqcomp([ifn, ifn1])
  #print(donepairs)

def fqcomp(inlist):
  f1 = inlist[0]
  f2 = inlist[1]
  for r1 in (SeqIO.parse(f1, "fastq")):
    #r1q = r1.letter_annotations["phred_quality"]
    r1qs = r1.format("qual")
    #r1qs = phred33(r1q)
    for r2 in (SeqIO.parse(f2, "fastq")):
      #r2q = r2.letter_annotations["phred_quality"]
      r2qs = r2.format("qual")
      #r2qs = phred33(r2q)
      if r1.seq == r2.seq and r1qs == r2qs:
        sq = r1.seq + r1qs
        if sq in retd:
          if (f1,r1.id) not in retd[sq]:
            retd[sq].append((f1, r1.id))
          if (f2,r2.id) not in retd[sq]:
            retd[sq].append((f2, r2.id))
        else:
          retd[sq] = [(f1, r1.id), (f2, r2.id)]


filecol = {}
cycle = 0
for f in sys.argv[1:]:
  filecol[f] = cycle
  cycle += 1
retd = {}


main()
print("\t".join(sys.argv[1:]))
for k,v in retd.items():
  #print("{}   {}\n".format(k, v))
  outlist=[]
  for i in sys.argv[1:]:
    outlist.append("-")
  for t in v:
    fcol = filecol[t[0]]
    seqid = t[1]
    outlist[fcol] =seqid
    #print("{}   {}".format(t[0], seqid))
  print("\t".join(outlist))
