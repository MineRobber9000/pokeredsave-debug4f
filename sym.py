import rgbbin.objfile as rgbbin

class SymFile:
	def __init__(self,obj):
		self.obj = obj
	def getSymbolLine(self,id):
		sym = self.obj.symbols[id]
		sect = self.obj.sections[sym['sectid']]
		return "00:{:04X} {}".format((sect['origin']+sym['value']),sym['name'])
	def getSymFileRaw(self):
		for i in range(self.size):
			yield self.getSymbolLine(i)
	def getSymFileLines(self):
		return list(self.getSymFileRaw())
	def getSymFile(self):
		return "\n".join(self.getSymFileRaw())

	@property
	def size(self):
		return len(self.obj.symbols)
