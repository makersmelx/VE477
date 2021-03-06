#include "lab2.h"
int kruskal(int e)
{
    int num = 0;
    int u, v;
    UFset(e);
    for (int i = 0; i < e; i++)
    {
        u = graph[i].u;
        v = graph[i].v;
        if (Find(u) != Find(v))
        {
            res[num].u = graph[i].u;
            res[num].v = graph[i].v;
            num++;
            Union(u, v);
        }
    }
    return num;
}