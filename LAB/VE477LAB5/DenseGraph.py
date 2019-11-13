import sys


class Edge:
    def __init__(self, u, v, w):
        u: int
        v: int
        w: int
        self.start = u
        self.end = v
        self.weight = w

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


class DenseGraph:
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
        self.edges[u_id][v_id] = new_edge
        self.edge_num += 1

    def remove_edge(self, u, v):
        u: str
        v: str
        u_id = self.name_map[u]
        v_id = self.name_map[v]
        self.edge_num -= 1
        self.edges[u_id][v_id] = None

    def add_vertex(self, string):
        if string not in self.name_map:
            self.name_map[string] = self.vertex_num
            # print(self.name_map[string])
            self.vertex_num += 1
            new_vertex = Vertex(string)
            self.vertice.append(new_vertex)
            for edge_joint in self.edges:
                edge_joint.append(None)
            empty_row = [None]*self.vertex_num
            self.edges.append(empty_row)

    def remove_vertex(self, u):
        # Assume u is valid
        u: str
        u_id: int
        if u in self.name_map:
            u_id = self.name_map[u]
            del self.name_map[u]
            self.vertex_num -= 1
            del self.vertice[u_id]
            del self.edges[u_id]
            for edge_joint in self.edges:
                del edge_joint[u_id]

    def is_adjacent(self, u, v):
        u: str
        v: str
        u_id = self.name_map[u]
        v_id = self.name_map[v]
        if self.edges[u_id][v_id] is not None:
            return True
        return False

    def print_graph(self):
        print("============================")
        for row in self.edges:
            for column in row:
                if column is None:
                    print(0, end=" "),
                else:
                    print(column.weight, end=" ")
            print("")
        print("============================")


