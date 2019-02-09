dictionary={}
class Graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    def getVertices(self):
        return self.gdict.keys()

# Check for the visisted and unvisited nodes
def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        temp=dictionary[start]+1
        if(dictionary[next]>temp):
            dictionary[next]=dictionary[start]+1
        dfs(graph, next, visited)
    return visited

gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }
g=Graph(gdict)
for x in g.getVertices():
    dictionary[x]=9999
dictionary['a']=0
dfs(gdict, 'a')
for x,y in zip(dictionary.keys(), dictionary.values()):
    print(x," ",y)

