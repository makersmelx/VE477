#ifndef DICTIONARY_H
#define DICTIONARY_H
// define your only data structure here, you may define dictionary, elements, etc...
void *initializer();

void *search(void *dictionary, int key);

void insert(void *dictionary, int key, int value);

void delete (void *dictionary, int key);

void *minimum(void *dictionary);

void *maximum(void *dictionary);

void *predecessor(void *dictionary, int key);

void *successor(void *dictionary, int key);

int getkey(void *element);

int getvalue(void *element);

void free_dict(void *dictionary);
#endif
