#include "lab2.h"

int main()
{
    int v = 0, e = 0;
    scanf("%d", &e);
    scanf("%d", &v);
    parent = malloc(sizeof(int) * MAX);
    graph = malloc(sizeof(Edge) * MAX);
    res = malloc(sizeof(Result) * MAX);
    for (int i = 0; i < e; i++)
    {
        int tmpU = 0, tmpV = 0;
        scanf("%d %d %d", &tmpU, &tmpV, &graph[i].w);
        int min = tmpU < tmpV ? tmpU : tmpV;
        int max = tmpU > tmpV ? tmpU : tmpV;
        graph[i].u = min;
        graph[i].v = max;
    }
    qsort(graph, e, sizeof(Edge), Ecmp);
    //switch between kruskal and prim

    int MSTNum = kruskal(e);
    //int MSTNum = prim(e,v);

    qsort(res, MSTNum, sizeof(Result), Rcmp);
    for (int i = 0; i < MSTNum; i++)
    {
        printf("%d--%d\n", res[i].u, res[i].v);
    }
    free(graph);
    free(res);
}
