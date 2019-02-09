class Graph:
	def __init__(self, gdict):
		if gdict is None:
			gdict=[]
		self.gdict= gdict

	#get the keys of the dictionary
	def getVertices(self):
		return list(self.gdict.keys())

	def getValues(self):
		return list(self.gdict.values())

	def getEdges(self):
		edges=[]
		for node in self.gdict:
			for neighbour in self.gdict[node]:
				edges.append((node, neighbour))
		return edges

	def printGraph(self):
		print(self.gdict)


file = open('graphText.txt','r')

array2d = [[int(value) for value in line.strip().split()] for line in file]
print(array2d)
dictionary=dict()
rowIndex=1
for x in array2d:
	values=[]
	columnIndex=1
	for y in x:
		if(y==1):
			values.append(columnIndex)
		columnIndex+=1
	dictionary[rowIndex]=values	
	rowIndex+=1
graph=Graph(dictionary)
print(graph.getVertices())
print(graph.getEdges())