import FibHeap
import SparseGraph

if __name__ == "__main__":
    edge_heap = FibHeap.FibHeap()
    graph = SparseGraph.SparseGraph()
    input_size = int(input())
    for i in range(0, input_size):
        u, v, w = input().split(' ')
        graph.add_vertex(str(u))
        graph.add_vertex(str(v))
        graph.add_edge(str(u), str(v), int(w))
    s = str(input().strip("\r"))
    t = str(input().strip("\r"))
    graph.vertice[graph.name_map[s]
                  ].prev = "You_will_never_use_this_as_node_name"
    graph.vertice[graph.name_map[s]].distance = 0
    graph.vertice[graph.name_map[s]].visited = True
    for edge in graph.edges[graph.name_map[s]]:
        graph.vertice[edge.end].distance = edge.weight
        graph.vertice[edge.end].prev = s
        edge.res = edge.weight
        edge_heap.insert(edge.res, edge)
    while not edge_heap.empty():
        smallest_edge = edge_heap.extract_min()
        v_id = smallest_edge.end
        if graph.vertice[v_id].visited:
            continue
        graph.vertice[v_id].visited = True
        for edge in graph.edges[v_id]:
            test_vertex = edge.end
            if (not graph.vertice[test_vertex].visited) and \
                    graph.vertice[test_vertex].distance > graph.vertice[v_id].distance + edge.weight:
                graph.vertice[test_vertex].distance = edge.res = graph.vertice[v_id].distance + edge.weight
                edge_heap.insert(edge.res, edge)
                graph.vertice[test_vertex].prev = graph.vertice[v_id].name
    for i in graph.vertice:
        if (i.visited == False):
            print(i.name, False)
    result = []
    string_tmp = t
    while string_tmp != "You_will_never_use_this_as_node_name":
        result.append(string_tmp)
        x = graph.name_map[string_tmp]
        string_tmp = graph.vertice[x].prev
    result.reverse()
    print(result)
    # print(graph.vertice[graph.name_map[t]].distance)
