
#module to find all connected components of a graph

def findConnectedComps(G):

	all_djsets = dict()

	def makeSet(x):
		all_djsets[x] = list()
	
	def findSet(x):

		if x in all_djsets.keys():
			return x
		else:
			for rep, adjlist in all_djsets.items():
				if x in adjlist:
					return rep

	def union(x, y):
	
		xrep = findSet(x)
		yrep = findSet(y)
	
		if all_djsets[xrep] >= all_djsets[yrep]:
			ylist = all_djsets.pop(yrep)
			all_djsets[xrep].append(yrep)
			for k in ylist:
				all_djsets[xrep].append(k)
		else:
			xlist = all_djsets.pop(xrep)
			all_djsets[yrep].append(xrep)
			for k in xlist:
				all_djsets[yrep].append(k)
	
	for v in G.vertices:
		makeSet(v)
	
	for e in G.edges:
		u, v = tuple(e)
		if findSet(u) != findSet(v):
			union(u, v)

	return all_djsets
