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
          donepairs.append(p1)
          donepairs.append(p2)
          fqcomp([ifn, ifn1])
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

# {{{ fqcomp. Compare two fq files. Common (on seq AND qual) ones
# are output as fastq to sys.stdout
def fqcomp(inlist):
  f1 = inlist[0]
  f2 = inlist[1]
  for r1 in (SeqIO.parse(f1, "fastq")):
    r1q = r1.letter_annotations["phred_quality"]
    r1qs = phred33(r1q)
    for r2 in (SeqIO.parse(f2, "fastq")):
      r2q = r2.letter_annotations["phred_quality"]
      r2qs = phred33(r2q)
      if r1.seq == r2.seq and r1qs == r2qs:
        sq = r1.seq + r1qs
        if sq in retd:
          if (f1,r1.id) not in retd[sq]:
            retd[sq].append((f1, r1.id))
          if (f2,r2.id) not in retd[sq]:
            retd[sq].append((f2, r2.id))
        else:
          retd[sq] = [(f1, r1.id), (f2, r2.id)]
        # SeqIO.write([r1], sys.stdout, "fastq")
        #print("{}\n{}\n{}".format(r1.id, r1.seq, r1qs))

# }}}


# {{{ def twofiles() # hardcoded filenames inside this function.
def twofiles(fn):
  fh = []
  for f in fn:
    fh.append(open(f, "wt"))

  srl = []
  for snum in range(1, 3+1):
    seq = randnt(100)
    qual = randqual(100)
    sname = "{}_{}".format("c", snum);
    srl.append(SeqRecord(seq, id = sname, name = sname, description = "",
                         letter_annotations = {"phred_quality" : qual}))

  for ha in fh:
    SeqIO.write(srl, ha, "fastq");

  for ha in fh:
    srl = []
    for snum in range(1, 100+1):
      seq = randnt(100)
      qual = randqual(100)
      sname = "{}_{}".format("one", snum);
      srl.append(SeqRecord(seq, id = sname, name = sname, description = "",
                           letter_annotations = {"phred_quality" : qual}))

    SeqIO.write(srl, ha, "fastq");

  for ha in fh:
    ha.close()

# }}}

# main()

#twofiles(sys.argv[1:])
# fqcomp(sys.argv[1:])

filecol = {}
cycle = 0
for f in sys.argv[1:]:
  filecol[f] = cycle
  cycle += 1
#print(filecol)

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




'''
To test run as

python3 pythrill/allvsall.py one.fq two.fq

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
