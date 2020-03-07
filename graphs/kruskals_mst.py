from graphs.implementation import Graph, Vertex


class G(Graph):
    def __len__(self):
        return len(self.vertList)

    def __iter__(self):
        return iter(self.vertList.values())

    def display(self):
        print('Vertices: ', end='')
        for v in self.getVertices():
            print(v, end=' ')

        print()
        print('Edges: ')
        for v in self:
            for dest in v.getConnections():
                w = v.getWeight(dest)
                print('(src={}, dest={}, weight={}) '.format(v.getId(),
                                                             dest.getId(), w))


def kruskal_mst(g):
    mst = G()

    if len(g) == 1:
        # m = g
        u = next(iter(g))
        mst.addVertex(u.getId())
        return mst

    edges = []
    edge_index = 0

    for v in g:
        for n in v.getConnections():
            if (v, n, v.getWeight(n)) not in edges:
                edges.append((v, n, v.getWeight(n)))

    # sort the edges
    edges = sorted(edges, key=lambda x: x[2])

    # initially, each vertex is in its own component
    components = {}
    for i, v in enumerate(g):
        components[v] = i

    # loop until mst has the same number of vertices as g
    while len(mst) < len(g):
        u, v, w = edges[edge_index]
        edge_index += 1

        # if adding edge (u, v) will not form a cycle
        if components[u] != components[v]:
            if u.getId() not in mst:
                mst.addVertex(u.getId())
            if v.getId() not in mst:
                mst.addVertex(v.getId())
            mst.addEdge(u.getId(), v.getId(), w)
            # Uncomment for undirected graphs
            # mst.addEdge(v.getId(), u.getId(), w)

            # merge components of u and v
            for a in g:
                if components[a] == components[v]:
                    components[a] = components[u]

    mst.display()


g = G()
g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)

g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

# g.display()

kruskal_mst(g)
