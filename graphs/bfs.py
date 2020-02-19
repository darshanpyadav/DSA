from pythonds import Graph, Vertex, Queue


def bfs(g, start):
    visited = []
    q = Queue()
    q.enqueue(start)
    visited.append(start)

    while not q.isEmpty():
        v = q.dequeue()
        for n in g.getVertex(v).getConnections():
            if n.id not in visited:
                q.enqueue(n.id)
                visited.append(n.id)

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
a = bfs(g, 1)
print(a)