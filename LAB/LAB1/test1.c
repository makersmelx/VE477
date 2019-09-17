#include "dictionary.h"
#include <stdio.h>
#include <string.h>

void print(void *dictionary)
{
    printf("Original: {");
    void *element = minimum(dictionary);
    while (element != NULL)
    {
        int key = getkey(element);
        int value = getvalue(element);
        printf("%d:%d, ", key, value);
        element = successor(dictionary, key);
    }
    printf("}.\n");
}

void print_reverse(void *dictionary)
{
    printf("Reversed: {");
    void *element = maximum(dictionary);
    while (element != NULL)
    {
        int key = getkey(element);
        int value = getvalue(element);
        printf("%d:%d, ", key, value);
        element = predecessor(dictionary, key);
    }
    printf("}.\n");
}

int main()
{
    void *dictionary = initializer();
    int n; // n is the number of operations performed to the dictionary
    scanf("%d", &n);
    char buffer[100];
    for (int i = 0; i < n; ++i)
    {
        printf("%d\n", i);
        scanf("%s", buffer);
        if (strcmp(buffer, "insert") == 0)
        {
            int key, value;
            scanf("%d", &key);
            scanf("%d", &value);
            insert(dictionary, key, value);
        }
        else if (strcmp(buffer, "delete") == 0)
        {
            int key;
            scanf("%d", &key);
            delete (dictionary, key);
        }
        else if (strcmp(buffer, "search") == 0)
        {
            int key;
            scanf("%d", &key);
            void *element = search(dictionary, key);
            if (element != NULL)
            {
                int value = getvalue(element);
                printf("The value is %d.\n", value);
            }
        }
        printf("***Print Dictionary***\n");
        print(dictionary);
        print_reverse(dictionary);
        printf("****Print Finished****\n");
    }
    free_dict(dictionary);
    return 0;
}