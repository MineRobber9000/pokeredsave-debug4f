import sav,mapparse

m = mapparse.MapFile()

def insert(s,p):
	with open("{}.bin".format(p),"rb") as f:
		g = list(f.read())
		s[1][mainDataOffset(m.locs[p]):mainDataOffset(m.locs[p])+len(g)]=g

def checksum(s):
	s.mode = 0 # bank:address mode
	hl = 0x598
	bc = 0xf8d
	r = 0
	while bc > 0:
		r += s[1][hl]
		hl+=1
		r = (r%256)
		bc-=1
	s[1][0x1525] = r^0xFF

def mainDataOffset(addr):
	if addr<0xd2f7 or addr>=0xda80:
		raise Exception("Out of range address: {:04X}".format(addr))
	return 0x5a3+(addr-0xd2f7)

#print(hex(0xa000+mainDataOffset(0xd31d)))

s = sav.SAVFile("clean.sav")
s[1][mainDataOffset(0xd31d):mainDataOffset(0xd31d)+4]=[0x01,0x59,0x01,0xFF]
s[1][mainDataOffset(0xda44)]=0xff
for l in m.locs.keys():
	insert(s,l)
checksum(s)
s.output("mod.sav")
