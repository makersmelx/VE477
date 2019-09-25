#include "lab2.h"
int Ecmp(const void *a, const void *b)
{
    Edge *e1 = (Edge *)a;
    Edge *e2 = (Edge *)b;
    return e1->w - e2->w;
}

int Rcmp(const void *a, const void *b)
{
    Result *r1 = (Result *)a;
    Result *r2 = (Result *)b;
    return (r1->u == r2->u) ? (r1->v - r2->v) : (r1->u - r2->u);
}