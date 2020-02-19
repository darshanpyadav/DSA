from pythonds import Graph, Vertex


def dfs_modified(g, start, visited, s):
    visited.append(start)

    for v in g.getVertex(start).getConnections():
        if v.id not in visited:
            dfs_modified(g, v.id, visited, s)
    s.append(start)


def topological_sort(g, n):
    visited = []
    s = []
    for i in range(n):
        if i not in visited:
            dfs_modified(g, i, visited, s)
    print(s[::-1])


g = Graph()
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

topological_sort(g, 6)

