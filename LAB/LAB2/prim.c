#include "lab2.h"
int prim(int e, int v)
{
    int *edgeMark = malloc(sizeof(int) * e);
    int *used = malloc(sizeof(int) * v);
    int finished = 0;
    int num = 0;
    for (int i = 0; i < v; i++)
    {
        used[i] = 0;
    }
    for (int i = 0; i < e; i++)
    {
        edgeMark[i] = 0;
    }
    while (finished == 0)
    {
        for (int i = 0; i < e; i++)
        {
            if (edgeMark[i] == 1)
                continue;
            if (i == 0 || used[graph[i].u] + used[graph[i].v] == 1)
            {
                used[graph[i].u] = 1;
                used[graph[i].v] = 1;
                edgeMark[i] = 1;
                res[num].u = graph[i].u;
                res[num].v = graph[i].v;
                num++;
                break;
            }
        }
        for (int i = 0; i < v; i++)
        {
            if (used[i] == 0)
            {
                break;
            }
            if (i == v - 1)
            {
                finished = 1;
            }
        }
    }
    free(edgeMark);
    free(used);
    return num;
}
