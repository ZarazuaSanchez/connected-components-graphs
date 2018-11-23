
def vertIsIntOrStr(v):
	return type(v) == int or type(v) == str

class UndirectedGraph:

	def __init__(self, *args):
		self.vertices = set()
		self.edges = []
		self.addEdges(*args)
	
	def __pairUpArgs(self, arglist):
		if (len(arglist) % 2) > 0:
			arglist.pop(-1)
		return arglist
	
	def addEdge(self, u, v):
		if vertIsIntOrStr(u) and vertIsIntOrStr(v):
			if u not in vertices:
				self.vertices.add(u)
			if v not in vertices:
				self.vertices.add(v)
			if {u, v} not in list:
				self.edges.append({u, v})

	def addEdges(self, *args):
	
		if type(args[0]) == int or type(args[0]) == 'str':
			
			args = list(args)
			args = self.__pairUpArgs(args)
			
			for i in range(0, len(args), 2):
				self.addEdges( args[i], args[i + 1] )
				
		elif type(args[0]) == set:
			
			for a in args:
				if type(a) == set:
					if len(a) == 2:
						if a not in self.edges:
							self.addVertices(*list(a))
							self.edges.append(a)
							
	def removeEdge(self, u, v):
		if {u, v} in edges:
			self.edges.remove({u, v})
			
	def removeEdges(self, *args):
		
		if type(args[0]) == int or type(args[0]) == str:
			args = list(args)
			args = self.__pairUpArgs(args)
			
			for i in range(0, len(args), 2):
				self.removeEdge(args[i], args[i + 1])
				
		elif type(args[0]) == set:
			
			for a in args:
				if type(a) == set:
					if len(a) == 2:
						if a in self.edges:
							self.edges.remove(a)
		
				
	def addVertices(self, *args):
		for a in args:
			if a not in self.vertices:
				if vertIsIntOrStr(a):
					self.vertices.add(a)
	
	def removeVertices(self, *args):
		for a in args:
			if a in self.vertices:
				self.vertices.remove(a)
				for v in self.vertices:
					if {a, v} in self.edges:
						edges.remove({a, v})

