import sys
from Bio import SeqIO
from random import sample
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def main():
  donepairs = [];
  print(sys.argv[1:])
  ifns = sys.argv[1:]
  for ifn in ifns:
    for ifn1 in ifns:
      if ifn != ifn1:
        p1 = "--".join([ifn, ifn1])
        p2 = "--".join([ifn1, ifn])
        if p1 not in donepairs and p2 not in donepairs:
          donepairs = donepairs + [p1, p2]
          print(ifn + " vs " + ifn1)
  print(donepairs)

# def qualstr(r):

# {{{ randnt and randqual
# Both take just one argument the length of sequence or quality
# to generate.
def randnt(l):
  blist = []
  for i in range(0, l):
    nt = sample(["a", "c", "g", "t"], 1)
    blist.append("".join(nt))
  retseq = Seq("".join(blist), "generic_dna")
  return(retseq);

def randqual(l):
  blist = []
  for i in range(0, l):
    q = sample(range(30,39), 1)
    blist.append(q[0])
  return(blist)
# }}}

# {{{ phred33
# Given a list of integers, returns a quality string as it is
# written in fastq files.
def phred33(ql):
  retlist = []
  for q in ql:
    ph = 33 + q
    pc = chr(ph)
    retlist.append(pc)
  retstr = "".join(retlist)
  return(retstr)
# }}}



# main()
seq = randnt(20)
print(type(seq))
print(seq)

qual = randqual(20)
print(qual)

sr = SeqRecord(seq, id = "stuff", name = "stuff", description = "",
               letter_annotations = {"phred_quality" : qual}) 

print(type(sr))
print(sr)
print(phred33(sr.letter_annotations["phred_quality"]))

SeqIO.write([sr], "stuff.fq", "fastq");

'''
To test run as

python3 pythrill/allvsall.py

Note that main() is not being called at this time.  We are only interested in
generating random sequence and quality strings at this time which we can put in
fastq files to make a test data seq where we will know before hand how many
duplicate reads there are.

Right now, just try to make sense of the functions randnt(), randqual() and
phred33(). Also how to make a Bio.SeqRecord object. Please pay attention to
each and every function call making sure to understand exactly what is
happening. Once you have done this figure out how to write the sequence to a
fastq file.

'''


