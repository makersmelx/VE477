import sys


class Edge:
    def __init__(self, u, v, w):
        u: int
        v: int
        w: int
        self.start = u
        self.end = v
        self.weight = w
        # count as the distance of v
        self.res = 0

    def get_edge_weight(self):
        return self.weight

    def set_edge_weight(self, val):
        self.weight = val


class Vertex:
    def __init__(self, init_name):
        init_name: str
        self.distance = sys.maxsize
        self.visited = False
        self.name = init_name
        self.prev = init_name

    def get_vertex_value(self):
        return self.distance

    def set_vertex_value(self, val):
        self.distance = val


class SparseGraph:
    edges: list = []
    vertice: list = []
    name_map: dict = {}
    edge_num: int = 0
    vertex_num: int = 0

    def add_edge(self, u, v, w):
        u: str
        v: str
        w: int
        u_id = self.name_map[u]
        v_id = self.name_map[v]
        new_edge = Edge(u_id, v_id, w)
        self.edges[u_id].append(new_edge)
        self.edge_num += 1

    def remove_edge(self, u, v):
        u: str
        v: str
        u_id = self.name_map[u]
        v_id = self.name_map[v]
        self.edge_num -= 1
        for j, edge in enumerate(self.edges[u_id]):
            if edge.end == v_id:
                del(self.edges[u_id][j])

    def add_vertex(self, string):
        if string not in self.name_map:
            self.name_map[string] = self.vertex_num
            self.vertex_num += 1
            new_vertex = Vertex(string)
            self.vertice.append(new_vertex)
            self.edges.append([])

    def remove_vertex(self, u):
        # Assume u is valid
        u: str
        u_id: int
        if u not in self.name_map:
            return
        u_id = self.name_map[u]
        del self.name_map[u]
        self.vertex_num -= 1
        del self.vertice[u_id]
        del self.edges[u_id]
        for edge_joint in self.edges:
            for j, edge in enumerate(edge_joint):
                if edge.end == u_id:
                    del edge_joint[j]

    def is_adjacent(self, u, v):
        u: str
        v: str
        u_id = self.name_map[u]
        v_id = self.name_map[v]
        for edge in self.edges[u_id]:
            edge: Edge
            if edge.end == v_id:
                return True
        for edge in self.edges[v_id]:
            if edge.end == u_id:
                return True
        return False

    def print_graph(self):
        print("============================")
        for row in self.edges:
            for column in row:
                if column is not None:
                    print(column.weight, end=" ")
            print("")
        print("============================")

