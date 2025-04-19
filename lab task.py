#file handling in python
#f=open("demofile.txt","w")
#f.write("AI LAB 3")
#f.close()
#f=open("demofile.txt","rt")
#print(f.read())
#f.close()

#bfs code----traversal of graph

from collections import defaultdict
count=0
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)


    def bfs(self,s):
        visited = [False] * (len(self.graph))
        queue = [s]
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s,end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdge("home","product")
g.addEdge("home","About us")
g.addEdge("home","blog")
g.addEdge("home","contact")
g.addEdge("product","p1")
g.addEdge("product","p2")
g.addEdge("product","p3")
g.addEdge("About us","")
g.addEdge("contact","")
g.bfs("p1")

# time complexity
