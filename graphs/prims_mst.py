from pythonds import PriorityQueue, Graph
import sys


def prim(G, start):
    pq = PriorityQueue()
    start.setDistance(0)
    #  O(V)
    pq.buildHeap([(v.getDistance(), v) for v in G])

    while not pq.isEmpty():
        closest = pq.delMin()
        for n in closest.getConnections():
            newCost = closest.getWeight(n)
            if n in pq and newCost < n.getDistance():
                n.setPred(closest)
                n.setDistance(newCost)
                pq.decreaseKey(n, newCost)

    return G
                

g = Graph()
g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)

g.addEdge(0, 1, 10)
g.addEdge(1, 0, 10)
g.addEdge(0, 2, 6)
g.addEdge(2, 0, 6)
g.addEdge(0, 3, 5)
g.addEdge(3, 0, 5)
g.addEdge(1, 3, 15)
g.addEdge(3, 1, 15)
g.addEdge(2, 3, 4)
g.addEdge(3, 2, 4)

p = prim(g, g.getVertex(0))

for v in p:
    if v.getDistance() != sys.maxsize and v.getPred() is not None:
        print(f'src={v.getPred().getId()}, dest={v.getId()}, weight={v.getDistance()}')