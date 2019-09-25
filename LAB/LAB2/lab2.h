#ifndef LAB2_H
#define LAB2_H
#include <stdio.h>
#include <stdlib.h>
#define MAX 1000
typedef struct _edge
{
    int u, v, w;
} Edge;
typedef struct _result
{
    int u, v;
} Result;
int *parent;
Result *res;
Edge *graph;
int Find(int);
void Union(int, int);
void UFset(int);
int kruskal(int);
int Ecmp(const void *, const void *);
int Rcmp(const void *, const void *);
int prim(int, int);
#endif