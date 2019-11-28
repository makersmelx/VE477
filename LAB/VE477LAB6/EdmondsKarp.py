import DenseGraph as DG
import queue


def BFS(graph, source, sink, prev):
    graph: DG.DenseGraph
    source: str
    sink: str
    prev: list
    visited = [False] * graph.vertex_num
    # Save indexs not itself
    q = queue.Queue()
    q.put(graph.name_map[source])
    while not q.empty():
        u = q.get()
        for v in range(len(graph.edges[u])):
            if visited[v] == False and graph.edges[u][v] > 0:
                q.put(v)
                visited[v] = True
                prev[v] = u
    return True if visited[graph.name_map[sink]] else False


def Ed_karp(graph, source, sink):
    graph: DG.DenseGraph
    source: str
    sink: str
    prev = [-1] * graph.vertex_num
    max_flow = 0
    while BFS(graph, source, sink, prev):
        path_flow = float("Inf")
        it = graph.name_map[sink]
        while it != graph.name_map[source]:
            path_flow = min(path_flow, graph.edges[prev[it]][it])
            it = prev[it]
        max_flow += path_flow
        v = graph.name_map[sink]
        while v != graph.name_map[source]:
            u = prev[v]
            graph.edges[u][v] -= path_flow
            graph.edges[v][u] += path_flow
            v = prev[v]
    return max_flow


if __name__ == '__main__':
    graph = DG.DenseGraph()
    edge_num = int(input())
    for i in range(edge_num):
        u, v, w = input().split(' ')
        graph.add_vertex(str(u))
        graph.add_vertex(str(v))
        graph.add_edge(str(u), str(v), int(w))
    source = input()
    sink = input()
    # graph.print_graph()
    print(Ed_karp(graph, source, sink))
