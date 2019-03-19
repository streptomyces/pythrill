import argparse, sys
def silly(first, *second, **third):
  print(first)
  print(second)
  print(third)
  print(type(third))


def main():
  f = "FirstArgument"
  s = ["second1", "second2"]
  t = {"a" : "d1", "b" : "d2"}
  print(type(t))
  silret = silly(f, "stuff", "more", "andmore", a = 3, b = 4, c = 5)
  # silret = silly(f, "stuff", "more", "andmore", t)

if __name__ == "__main__":
  aps = argparse.ArgumentParser()
  aps.add_argument('--infile', '-i', help = "Input file.")
  aps.add_argument('--outfile', '-o', help = "Output file.")
  args = aps.parse_args();
  main()

'''
python3 pythrill/exploders.py
'''
