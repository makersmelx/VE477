import SparseGraph

if __name__ == "__main__":
    graph = SparseGraph.SparseGraph()
    input_size = int(input())
    for i in range(0, input_size):
        u, v, w = input().split(' ')
        graph.add_vertex(str(u))
        graph.add_vertex(str(v))
        graph.add_edge(str(u), str(v), int(w))
    s = str(input().strip("\r"))
    t = str(input().strip("\r"))
    graph.vertice[graph.name_map[s]].prev = "You_will_never_use_this_as_node_name"
    graph.vertice[graph.name_map[s]].distance = 0
    for edge in graph.edges[graph.name_map[s]]:
        graph.vertice[edge.end].distance = edge.weight
        graph.vertice[edge.end].prev = s
    for i in range(0, graph.vertex_num):
        for edge_joint in graph.edges:
            for edge in edge_joint:
                if graph.vertice[edge.end].distance > graph.vertice[edge.start].distance + edge.weight:
                    graph.vertice[edge.end].distance = graph.vertice[edge.start].distance + edge.weight
                    graph.vertice[edge.end].prev = graph.vertice[edge.start].name
    result = []
    string_tmp = t
    while string_tmp != "You_will_never_use_this_as_node_name":
        result.append(string_tmp)
        string_tmp = graph.vertice[graph.name_map[string_tmp]].prev
    result.reverse()
    print(result)
    # print(graph.vertice[graph.name_map[t]].distance)

