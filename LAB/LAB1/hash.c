#include "hash.h"
#include <stdio.h>
#include <stdlib.h>

typedef struct _node
{
    int key;
    int value;
    struct _node *next;
} Node;

typedef struct _sLink
{
    Node *head;
    struct _sLink *next;
} sLink;

typedef struct _hash
{
    sLink *head;
} Hash;

void *initializer(int size)
{
    size = size / 3;
    Hash *h = (Hash *)malloc(sizeof(Hash));
    h->head = (sLink *)malloc(sizeof(sLink));
    sLink *tmp = h->head;
    for (int i = 0; i < size - 1; i++)
    {
        tmp->head = (Node *)malloc(sizeof(Node));
        tmp->head->next = NULL;
        tmp->next = (sLink *)malloc(sizeof(sLink));
        tmp = tmp->next;
    }
    tmp->head = (Node *)malloc(sizeof(Node));
    tmp->head->next = NULL;
    tmp->next = NULL;
    return h;
}
// EFFECT: initialize an empty hash table with number of buckets specified by size

void insert(void *hashtable, int size, int key, int value)
{
    size = size / 3;
    int res = key % size;
    Hash *h = hashtable;
    sLink *tmp = h->head;
    for (int i = 0; i < res; i++)
    {
        tmp = tmp->next;
        //printf("Get tHere\n");
    }
    Node *index = tmp->head;
    while (index->next != NULL)
    {
        //printf("Get Here\n");
        index = index->next;
        if (index->key == key)
        {
            index->value = value;
            return;
        }
    }
    index->next = (Node *)malloc(sizeof(Node));
    index->next->key = key;
    index->next->value = value;
    index->next->next = NULL;
}
// EFFECT: If the key does not exist, insert an element(a key-value pair) to hash table. If key already exists, update the value.

void delete (void *hashtable, int size, int key)
{
    size = size / 3;
    int res = key % size;
    Hash *h = hashtable;
    sLink *tmp = h->head;
    for (int i = 0; i < res; i++)
    {
        tmp = tmp->next;
    }
    Node *index = tmp->head;
    while (index->next != NULL)
    {
        if (index->next->key == key)
        {
            Node *p = index->next;
            index->next = p->next;
            free(p);
            break;
        }
        index = index->next;
    }
}
// EFFECT: Delete an element(key-value pair) specified by the key. If it does not exist, do nothing

void *search(void *hashtable, int size, int key)
{
    size = size / 3;
    int res = key % size;
    Hash *h = hashtable;
    sLink *tmp = h->head;
    for (int i = 0; i < res; i++)
    {
        tmp = tmp->next;
    }
    Node *index = tmp->head;
    while (index->next != NULL)
    {
        index = index->next;
        if (index->key == key)
        {
            return index;
        }
    }
    return NULL;
}
// EFFECT: Given a hash table, return the pointer to the element(key-value pair) specified by the key, return NULL if not found.

int getValue(void *element)
{
    Node *tmp = element;
    return tmp->value;
}
// EFFECT: obtain the value of the element

void freeHashtable(void *hashtable, int size)
{
    Hash *h = hashtable;
    sLink *tmp = h->head, *delTmp;
    for (int i = 0; i < size / 3; i++)
    {
        Node *p = tmp->head, *q;
        while (p != NULL)
        {
            q = p->next;
            free(p);
            p = q;
        }
        delTmp = tmp->next;
        free(tmp);
        tmp = delTmp;
    }
    free(h);
}
