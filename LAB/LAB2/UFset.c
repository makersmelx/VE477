#include "lab2.h"
void UFset(int e)
{
    for (int i = 0; i < e; i++)
    {
        parent[i] = -1;
    }
}

int Find(int x)
{
    if (parent[x] < 0)
    {
        return x;
    }
    return parent[x] = Find(parent[x]);
}

void Union(int u, int v)
{
    int r1 = Find(u);
    int r2 = Find(v);
    if (r1 > r2)
    {
        parent[r2] += parent[r1];
        parent[r1] = r2;
    }
    else
    {
        parent[r1] += parent[r2];
        parent[r2] = r1;
    }
}