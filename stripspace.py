#!/usr/bin/env python3
"""\
strip trailing whitespace from file
usage: stripspace.py <file>
code is placed into public domain 
"""

import sys

if len(sys.argv[1:]) != 1:
  sys.exit(__doc__)

content = ''
outsize = 0
inp = outp = sys.argv[1]
'''
Open file in read binary mode
Read all contents of the file.
'''
with open(inp, 'rb') as infile:
  content = infile.read()
with open(outp, 'wb') as output:
  for line in content.splitlines():
    newline = line.rstrip(" ")      #Remove space from each line
    outsize += len(newline) + 1
    output.write(newline + '\n')    #Add newline char to end of each line

print("Done. Stripped %s bytes." % (len(content)-outsize))