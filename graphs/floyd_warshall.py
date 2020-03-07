from pythonds import Graph


#  Works only for directed ones
#  Shortest distance shows inf for reverse
def floyd_warshall(g):
    # convert graph to adjacent list representation
    distance = {v: dict.fromkeys(g, float('inf')) for v in g}

    for v in g:
        distance[v][v] = 0
        for n in v.getConnections():
            distance[v][n] = v.getWeight(n)

    for k in g:
        for i in g:
            for j in g:
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    print_shortest_distance(distance, g)


def print_shortest_distance(d, g):
    for i in d:
        for j in g:
            print(f"{i.getId()} --> {j.getId()}   {d[i][j]}")


g = Graph()
g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)

g.addEdge(0, 1, 5)
g.addEdge(0, 3, 10)
g.addEdge(1, 2, 3)
g.addEdge(2, 3, 1)

floyd_warshall(g)