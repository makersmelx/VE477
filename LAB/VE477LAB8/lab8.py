import random
import time
import numpy as np


def random_search(A, k):
    n = len(A)
    visited = [1 for i in range(n)]
    while sum(visited) != 0:
        i = random.randint(0, n-1)
        if (A[i] == k):
            return i
        visited[i] = 0
    return -1


def linear_search(A, k):
    A: list
    for i, p in enumerate(A):
        # print(i, end=" ")
        if p == k:
            return i
    print()
    return -1


def scramble_search(A, k):
    random.shuffle(A)
    return linear_search(A, k)


if __name__ == '__main__':
    number = 1000000
    times = 1000
    random_time = []
    linear_time = []
    scramble_time = []
    for k in range(times):
        print("The", k, "Process")
        A = [random.randint(1, number) for i in range(number)]
        k = random.randint(1, number)
        start = time.time()
        print(random_search(A, k), "time:", time.time() - start)
        linear_time.append(time.time() - start)

        start = time.time()
        print(linear_search(A, k), "time:", time.time() - start)
        random_time.append(time.time()-start)

        start = time.time()
        print(scramble_search(A, k), "time:", time.time() - start)
        scramble_time.append(time.time() - start)
    print("Random average: ", np.mean(random_time))
    print("Linear average: ", np.mean(linear_time))
    print("Scramble average: ", np.mean(scramble_time))
