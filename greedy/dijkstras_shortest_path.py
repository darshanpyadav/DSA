from pythonds import PriorityQueue, Graph, Vertex


def dijsktras(g, start):
    unvisited = set(g)
    distance = dict.fromkeys(g, float('inf'))
    distance[start] = 0

    while unvisited != set():
        closest = min(unvisited, key=lambda v: distance[v])
        unvisited.remove(closest)

        for n in closest.getConnections():
            if n in unvisited:
                new_distance = distance[closest] + closest.getWeight(n)
                if distance[n] > new_distance:
                    distance[n] = new_distance
    return distance


# Using priority queue -> O((V+E)logV)
def dijkstras_pq(g, start):
    pq = PriorityQueue()
    start.setDistance(0)
    # O(V)
    pq.buildHeap([(v.getDistance(), v) for v in g])

    while not pq.isEmpty():
        # O(logV) * O(V) = O(V*logV)
        closest = pq.delMin()
        for n in closest.getConnections():
            new_distance = closest.getDistance() + closest.getWeight(n)
            if new_distance < n.getDistance():
                n.setDistance(new_distance)
                n.setPred(closest)
                # O(E*logV)
                pq.decreaseKey(n, new_distance)


g = Graph()
g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)

g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
d = dijsktras(g, g.getVertex(0))
print('Distances from {}: '.format(0), end="\n")
print("********************")
for v in d:
    print('Distance to {}: {}'.format(v.getId(), d[v]))
print()

d_p = dijkstras_pq(g, g.getVertex(0))
print('Distances from {}: '.format(0), end="\n")
print("********************")
for v in g:
    print('Distance to {}: {}'.format(v.getId(), v.getDistance()))
print()