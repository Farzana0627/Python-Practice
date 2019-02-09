# import collections


# class DeQueue:
# 	def __init__(self):
# 		if(self.list==None):
# 			self.list=[]
# 	def appendLeft(self, newVal):
# 		self.list.insert(0,newVal)

# 	def appendRight(self, newVal):
# 		self.list.append(newVal) 

# 	def popRight(self):
# 		if(len(self.list)>0):
# 			self.list.pop()

# 	def popLeft(self):
# 		if(len(self.list)>0):
# 			self.list.remove(self.list[0])

# class Graph:
# 	def __init__(self, gdict=None):
# 		if(self.gdict==None):
# 			self.gdict={}

# 		self.gdict= gdict

# 	def bfs(self, startNode):

import collections
class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    def getVertices(self):
    	return self.gdict.keys()
def bfs(graph, startnode,costDictionary):
# Track the visited and unvisited nodes using queue
        seen, queue = set([startnode]), collections.deque([startnode])
        while queue:
            vertex = queue.popleft()
            marked(vertex)
            for node in graph[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)
                    costDictionary[node]=costDictionary[vertex]+1

        print("cost:")

        print(costDictionary.keys())
        print(costDictionary.values())

def marked(n):
    print(n)

dictionary={
	
}


# The graph dictionary
gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }
graph= Graph(gdict)
for x in graph.getVertices():
	dictionary[x]=0
bfs(gdict, "a", dictionary)


