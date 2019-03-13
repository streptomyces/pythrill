import os, re, sys, argparse

def main():
  print("This is a collection of functions.")
  print("There is no point in running it.")


# {{{ func commalist
def commalist(incoming, handle = "stdout"):
  if (handle == "stdout"):
    ofh = sys.stdout
  elif handle == "stderr":
    ofh = sys.stderr
  else:
    ofh = handle
  if (isinstance(incoming, str)
    or isinstance(incoming, int)
    or isinstance(incoming, float)):
    ofh.write(str(incoming) + "\n")
  elif isinstance(incoming, list):
    temp = [];
    for el in incoming:
      temp.append(str(el))
    temp1 = ", ".join(temp)
    ofh.write(temp1 + "\n")
# }}}

# {{{ func linelist
def linelist(incoming, handle = "stdout", inclint = False):
  if (handle == "stdout"):
    ofh = sys.stdout
  elif handle == "stderr":
    ofh = sys.stderr
  else:
    ofh = handle
  if (isinstance(incoming, str)
    or isinstance(incoming, int)
    or isinstance(incoming, float)):
    ofh.write(str(incoming) + "\n")
  elif isinstance(incoming, list):
    for el in incoming:
      if((not inclint) and re.match(r'__', str(el))):
        continue
      ofh.write('{}\n'.format(str(el)))
# }}}

# {{{ func nlinelist
def nlinelist(incoming, handle = "stdout"):
  if (handle == "stdout"):
    ofh = sys.stdout
  elif handle == "stderr":
    ofh = sys.stderr
  else:
    ofh = handle
  if (isinstance(incoming, str)
    or isinstance(incoming, int)
    or isinstance(incoming, float)):
    ofh.write(str(incoming) + "\n")
  elif isinstance(incoming, list):
    for el in incoming:
      ofh.write('{}\n'.format(el))
# }}}

# {{{ func tablist    
def tablist(incoming, handle = "stdout"):
  if (handle == "stdout"):
    ofh = sys.stdout
  elif handle == "stderr":
    ofh = sys.stderr
  else:
    ofh = handle
  if (isinstance(incoming, str)
    or isinstance(incoming, int)
    or isinstance(incoming, float)):
    ofh.write(str(incoming) + "\n")
  elif (isinstance(incoming, list)
    or isinstance(incoming, set)
    or isinstance(incoming, tuple)):
    temp = [];
    for el in incoming:
      temp.append(str(el))
    temp1 = "\t".join(temp)
    ofh.write('{}\n'.format(temp1))
# }}}

# {{{ func tabdict    
def tabdict(incoming, handle = "stdout"):
  if (handle == "stdout"):
    ofh = sys.stdout
  elif handle == "stderr":
    ofh = sys.stderr
  else:
    ofh = handle
  if (isinstance(incoming, dict)):
    for (key, val) in incoming.items():
      outstr = str(key) + "\t" + str(val) + "\n"
      ofh.write('{}\t{}\n'.format(key, val))
  else:
    sys.stderr.write("This functions is only for dicts" + "\n");
    return(False)
# }}}

# {{{ func pathparse
def pathparse(incoming):
  tbn=os.path.basename(incoming)
  dirname=os.path.dirname(incoming)
  ext = re.findall(r'\.[^.]*$', tbn)
  bn = re.sub(r'\.[^.]*$', '', tbn)
  return(dict(bn=bn, dn=dirname, ex=ext[0]))
# }}}
  
# {{{ argparse and call to main()
if __name__ == "__main__":

### argparse stuff
  aps = argparse.ArgumentParser()
  aps.add_argument('--infile', '-i', help = "Input file.")
  aps.add_argument('--outfile', '-o', help = "Output file.")

  args = aps.parse_args();
  main()
# }}}

