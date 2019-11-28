import EdmondsKarp as EK
import DenseGraph as DG


class Bipartite:

    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.adj = [[0 for i in range(self.right)] for j in range(self.left)]

    def add_edge(self, left, right):
        if self.adj[left][right] == 0:
            self.adj[left][right] = 1
        else:
            print("Already connected.")

    def max_match(self):
        graph = DG.DenseGraph()
        graph.add_vertex("source")
        graph.add_vertex("sink")
        for i in range(self.left):
            graph.add_vertex(str(i+1))
        for i in range(self.right):
            graph.add_vertex(str(-i-1))
        for i in range(self.left):
            graph.add_edge("source", str(i+1), 1)
        for i in range(self.right):
            graph.add_edge(str(-i-1), "sink", 1)
        for i in range(self.left):
            for j in range(self.right):
                if self.adj[i][j] == 1:
                    graph.add_edge(str(i+1), str(-j-1), 1)
        return EK.Ed_karp(graph, "source", "sink")


if __name__ == '__main__':
    G = Bipartite(5, 4)
    print(G.adj)
    G.add_edge(0, 0)
    G.add_edge(1, 0)
    G.add_edge(1, 2)
    G.add_edge(2, 1)
    G.add_edge(2, 2)
    G.add_edge(2, 3)
    G.add_edge(3, 2)
    G.add_edge(4, 2)
    G.add_edge(4, 3)
    print(G.max_match())
