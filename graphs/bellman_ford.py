from pythonds import Graph


#  Works only for directed ones
def bellman_ford(g, start):
    distance = dict.fromkeys(g, float('inf'))
    distance[start] = 0

    """Return distance where distance[v] is min distance from source to v.
 
    This will return a dictionary distance.
 
    g is a Graph object which can have negative edge weights.
    source is a Vertex object in g.
    """

    for v in g:
        for n in v.getConnections():
            distance[n] = min(distance[n], distance[v] + v.getWeight(n))

    return distance


g = Graph()
g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)

g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

d = bellman_ford(g, g.getVertex(0))
print('Distances from {}: '.format(0), end="\n")
print("********************")
for v in d:
    print('Distance to {}: {}'.format(v.getId(), d[v]))
print()