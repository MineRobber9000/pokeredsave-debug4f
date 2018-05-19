#!/usr/bin/env python3
import argparse,sym
import rgbbin.objfile as rgbbin

def gopher(o):
	for s in o.sections:
		with open("{}.bin".format(s['name']),"wb") as f:
			f.write(s['data'])

parser = argparse.ArgumentParser(description="A linker for RGB6 object files. Uses RGBBIN.")
parser.add_argument("objfile",help="Object file to link.")
parser.add_argument("symfile",help="Symbol file")
args = parser.parse_args()

with rgbbin.ObjectFile(args.objfile) as o:
	o.parse_all()
	gopher(o)
	s = sym.SymFile(o)
	with open(args.symfile,"w") as f:
		sym = s.getSymFile()
		for i in 'ABD':
			sym = sym.replace("00:{}".format(i),"01:{}".format(i))
		f.write(sym)
