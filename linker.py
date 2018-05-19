#!/usr/bin/env python3
import argparse
import rgbbin.objfile as rgbbin

def gopher(o):
	for s in o.sections:
		with open("{}.bin".format(s['name']),"wb") as f:
			f.write(s['data'])

parser = argparse.ArgumentParser(description="A linker for RGB6 object files. Uses RGBBIN.")
parser.add_argument("objfile",help="Object file to link.")
args = parser.parse_args()

with rgbbin.ObjectFile(args.objfile) as o:
	o.parse_all()
	gopher(o)
