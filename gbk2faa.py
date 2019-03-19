import argparse, sys
sys.path.append("./pythrill/py3lib")
import common as puc
#make a fasta file from genbank file
from Bio import SeqIO
#from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import argparse

# {{{ main
def main(gbkfn, faafn, dissect):
  gbkfh = open(gbkfn, "r") 
  faafh = open(faafn, "w")
  records = []
  sequences = SeqIO.parse(gbkfh, "genbank")
  count = 0
  for record in sequences:
    for feat in record.features:
      if feat.type == "CDS":
        tagd = feat.qualifiers
        #print(tagd)
        count +=1
        if "gene" in tagd:
                temp = tagd["gene"]
                faaid = temp[0]               # 0 is the first element of the tagd list
        else :
                faaid =  "CDS" + str(count) 
        product = "product for CDS" + str(count) 
        if "product" in tagd:
                temp = tagd["product"]
                product = ", ".join(temp)
        if "note" in tagd:
                temp = tagd["note"]
                note = ", ".join(temp)
        else:
                note = "no note"
        fex = feat.extract(record)
        puc.dissect(fex, "fex", "on line 35")
        #aaobj = fex.seq.translate(table="Bacterial", cds = True)
        aaobj = fex.seq.translate(table="Bacterial")
        print(type(aaobj.startswith))
        puc.dissect(aaobj, "aaobj")
        aarec = SeqRecord(aaobj)
        print(type(aarec.features))
        print(type(aarec.reverse_complement))
        aarec.id = faaid
        aarec.description = ", ".join([product, note])
        puc.dissect(aarec, "aarec")
        records.append(aarec)
        if dissect:
          puc.dissect(record, "record")
          puc.dissect(feat, "feat")
        break  
    break  
  SeqIO.write(records, faafh, "fasta")
  gbkfh.close()
  faafh.close()
# }}} end of main()


# {{{ argparse and call to main()
if __name__ == "__main__":
  aps = argparse.ArgumentParser()
  aps.add_argument('--infile', '-i', help = "Input file.")
  aps.add_argument('--outfile', '-o', help = "Output file.")
  aps.add_argument('--dissect', '-d', help = "Boolean", default = False, type = bool)
  args = aps.parse_args();
  main(gbkfn = args.infile, faafn = args.outfile, dissect = bool(args.dissect))
# }}}

'''
python3 pythrill/gbk2faa.py -i pythrill/example.gbk -o example.faa -d t
python3 pythrill/gbk2faa.py -i pythrill/example.gbk -o example.faa
'''

