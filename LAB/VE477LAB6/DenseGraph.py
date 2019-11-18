import sys


class Vertex:
    def __init__(self, init_name):
        init_name: str
        self.name = init_name


class DenseGraph:
    edges: list = []
    name_map: dict = {}
    edge_num: int = 0
    vertex_num: int = 0

    def add_edge(self, u, v, w):
        u: str
        v: str
        w: int
        u_id = self.name_map[u]
        v_id = self.name_map[v]
        self.edges[u_id][v_id] = w
        self.edge_num += 1

    def remove_edge(self, u, v):
        u: str
        v: str
        u_id = self.name_map[u]
        v_id = self.name_map[v]
        self.edge_num -= 1
        self.edges[u_id][v_id] = 0

    def add_vertex(self, string):
        if string not in self.name_map:
            self.name_map[string] = self.vertex_num
            # print(self.name_map[string])
            self.vertex_num += 1
            new_vertex = Vertex(string)
            for edge_joint in self.edges:
                edge_joint.append(0)
            empty_row = [0]*self.vertex_num
            self.edges.append(empty_row)

    def remove_vertex(self, u):
        # Assume u is valid
        u: str
        u_id: int
        if u in self.name_map:
            u_id = self.name_map[u]
            del self.name_map[u]
            self.vertex_num -= 1
            del self.edges[u_id]
            for edge_joint in self.edges:
                del edge_joint[u_id]

    def is_adjacent(self, u, v):
        u: str
        v: str
        u_id = self.name_map[u]
        v_id = self.name_map[v]
        if self.edges[u_id][v_id] > 0:
            return True
        return False

    def print_graph(self):
        print("============================")
        for row in self.edges:
            for column in row:
                print(column, end=" ")
            print("")
        print("============================")
