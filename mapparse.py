import re
class MapFile:
	def __init__(self):
		with open("map") as f:
			self.locs = [l.rstrip() for l in f]
		self.locs = [re.sub("\t+","\t",l).split("\t") for l in self.locs]
		self.locs = {l[0]: int(l[1],16) for l in self.locs}
