from pythonds import Graph, Vertex


def dfs(g, start, visited=None):
    if not visited:
        visited = []
    visited.append(start)
    print(start)

    for v in g.getVertex(start).getConnections():
        if v.id not in visited:
            dfs(g, v.id, visited)
    return visited


g = Graph()
for i in range(1, 7):
    g.addVertex(i)

g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(3,5)
g.addEdge(3,6)
a = dfs(g, 1)
print(a)
