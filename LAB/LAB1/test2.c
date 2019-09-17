#include "hash.h"
#include <stdio.h>
#include <string.h>

int main()
{
    int size;
    scanf("%d", &size);
    void *hashtable = initializer(size);
    int n;
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
            insert(hashtable, size, key, value);
        }
        else if (strcmp(buffer, "delete") == 0)
        {
            int key;
            scanf("%d", &key);
            delete (hashtable, size, key);
        }
        else if (strcmp(buffer, "search") == 0)
        {
            int key;
            scanf("%d", &key);
            void *element = search(hashtable, size, key);
            if (element != NULL)
            {
                int value = getValue(element);
                printf("The value is %d.\n", value);
            }
        }
        printf("***End***\n");
    }
    freeHashtable(hashtable, size);
    return 0;
}
