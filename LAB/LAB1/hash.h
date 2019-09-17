#ifndef HASH_H
#define HASH_H
void *initializer(int size);
// EFFECT: initialize an empty hash table with number of buckets specified by size

void insert(void *hashtable, int size, int key, int value);

void delete(void *hashtable, int size, int key);
// EFFECT: Delete an element(key-value pair) specified by the key. If it does not exist, do nothing

void* search(void* hashtable, int size, int key);
// EFFECT: Given a hash table, return the pointer to the element(key-value pair) specified by the key, return NULL if not found.

int getValue(void* element);
// EFFECT: obtain the value of the element

void freeHashtable(void* hashtable, int size);

#endif //HASH_HASH_H
