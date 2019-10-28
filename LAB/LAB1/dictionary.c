// define your only data structure here, you may define dictionary, elements, etc...
#include "dictionary.h"
#include <stdio.h>
#include <stdlib.h>
typedef struct _node
{
    int key;
    int value;
    struct _node *prev;
    struct _node *next;
} Node, *pNode;

typedef struct _dlist
{
    Node *head;
    Node *tail;
} Dlist;

void *initializer()
{
    Dlist *dlist = (Dlist *)malloc(sizeof(Dlist));
    dlist->head = (Node *)malloc(sizeof(Node));
    dlist->tail = (Node *)malloc(sizeof(Node));
    dlist->head->next = dlist->tail;
    dlist->tail->prev = dlist->head;
    return dlist;
}

void *search(void *dictionary, int key)
{
    Dlist *tmpDlist = dictionary;
    Node *tmp = tmpDlist->head->next;
    while (tmp != tmpDlist->tail)
    {
        if (tmp->key == key)
        {
            return tmp;
        }
        else if (tmp->key < key)
        {
            tmp = tmp->next;
        }
        else
        {
            break;
        }
    }
    return NULL;
}
//add after tmp
void insert(void *dictionary, int key, int value)
{
    Dlist *tmpDlist = dictionary;
    Node *tmp = tmpDlist->head;
    while (tmp != tmpDlist->tail)
    {
        if (tmp->next == tmpDlist->tail || tmp->next->key > key)
        {

            Node *newNode = (Node *)malloc(sizeof(Node));
            newNode->key = key;
            newNode->value = value;
            newNode->prev = tmp;
            newNode->next = tmp->next;
            tmp->next->prev = newNode;
            tmp->next = newNode;
            break;
        }
        else if (tmp->next->key == key)
        {
            tmp->next->value = value;
            break;
        }
        else
        {
            tmp = tmp->next;
        }
    }
    // int x = tmp->next->next == tmpDlist->tail;
    // int y = tmpDlist->tail->prev == tmp->next;
    // printf("Testing: %d, %d\n", tmp->next->next->prev->key, tmp->next->next->prev->value);
}

void delete (void *dictionary, int key)
{

    Dlist *tmpDList = dictionary;
    Node *tmp = tmpDList->head->next;
    while (tmp != tmpDList->tail)
    {
        if (tmp->key == key)
        {
            Node *p = tmp;
            p->prev->next = p->next;
            p->next->prev = p->prev;
            free(p);
            break;
        }
        else if (tmp->key < key)
        {
            tmp = tmp->next;
        }
        else
        {
            break;
        }
    }
}

void *minimum(void *dictionary)
{
    Dlist *tmpDlist = dictionary;
    return tmpDlist->head->next == tmpDlist->tail ? NULL : tmpDlist->head->next;
}

void *maximum(void *dictionary)
{
    Dlist *tmpDlist = dictionary;
    return tmpDlist->tail->prev == tmpDlist->head ? NULL : tmpDlist->tail->prev;
}

void *predecessor(void *dictionary, int key)
{
    Node *tmp = search(dictionary, key);
    Dlist *tmpDlist = dictionary;
    return tmp->prev == tmpDlist->head ? NULL : tmp->prev;
}

void *successor(void *dictionary, int key)
{
    Node *tmp = search(dictionary, key);
    Dlist *tmpDlist = dictionary;
    // printf("Testing: key:%d, value:%d, loc:%d\n", tmp->key, tmp->value, x);
    return tmp->next == tmpDlist->tail ? NULL : tmp->next;
}

int getkey(void *element)
{
    Node *tmp = element;
    return tmp->key;
}

int getvalue(void *element)
{
    Node *tmp = element;
    return tmp->value;
}

void free_dict(void *dictionary)
{

    Dlist *tmpDlist = dictionary;
    Node *p = tmpDlist->head->next, *q;
    while (p != tmpDlist->tail)
    {
        q = p->next;
        free(p);
        p = q;
    }
    free(tmpDlist->head);
    free(tmpDlist->tail);
    free(tmpDlist);
}
