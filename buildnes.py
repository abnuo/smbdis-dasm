import sys

def pad(d,l):
  while len(d)<l:
    d = d+b"\x00"
  return d

usage = "USAGE: buildnes.py [infile] [outfile] [chrfile] [mapper]"
try:
  fn = sys.argv[1]
except:
  sys.exit(usage)

try:
  out = sys.argv[2]
except:
  sys.exit(usage)

try:
  chrfile = sys.argv[3]
except:
  sys.exit(usage)

try:
  mapper = int(sys.argv[4])
except:
  sys.exit(usage)

with open(fn,"rb") as f:
  prgdata = f.read()
with open(chrfile,"rb") as f:
  chrdata = f.read()
prgsize = int(len(prgdata)/1000)
chrsize = int(len(chrdata)/1000)
mapperhex = hex(mapper)[2:].zfill(2)
data = b"NES\x1a"
print("PRG:",prgsize,"\tCHR:",chrsize)
data = data+bytes([int(prgsize/16),int(chrsize/8)])
data = data+bytes([int(bin(int(mapperhex[1],16))[2:]+"0001",2),int(bin(int(mapperhex[0],16))[2:]+"0000",2)])
data = data+(b"\x00"*3)
data = data+(b"\x00"*5)
print(data,len(data))
data = data+pad(prgdata,16384*int(prgsize/16))
data = data+pad(chrdata,8192*int(chrsize/16))
with open(out,"wb") as f:
  f.write(data)
