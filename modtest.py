import argparse, sys
sys.path.append("./code/py3lib")
import common as puc

def main():
  stringa = "one"
  stringb = "two"
  stringc = "three"
  xl = [stringa, stringb]
  puc.tablist(xl)
  print(args.infile)
  cla = type(args)
  print(cla)







if __name__ == "__main__":
  aps = argparse.ArgumentParser()
  aps.add_argument('--infile', '-i', help = "Input file.")
  aps.add_argument('--outfile', '-o', help = "Output file.")
  args = aps.parse_args();
  main()



