import math


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = self.child = self.left = self.right = None
        self.degree = 0
        self.mark = False

    def iterate(self):
        itr = itself = self
        while True:
            yield itr
            itr = itr.right
            if itr == itself:
                break

    def add_child(self, node):
        if self.child is None:
            self.child = node
        else:
            node.right = self.child.right
            node.left = self.child
            self.child.right.left = node
            self.child.right = node

    def remove_child(self, node):
        if self.child == self.child.right:
            self.child = None
        elif self.child == node:
            self.child = node.right
            node.right.self = self
        node.left.right = node.right
        node.right.left = node.left


class FibHeap:
    __root: Node = None
    __min: Node = None
    __size: int = 0

    def minium(self):
        return self.__min

    def extract_min(self):
        z = self.__min
        if z is not None:
            if z.child is not None:
                children = [x for x in z.child.iterate()]
                for ch_itr in children:
                    self.__merge_into_root(ch_itr)
                    ch_itr.parent = None
            self.__remove_from_root(z)
            if z == z.right:
                self.__min = self.__root = None
            else:
                self.__min = z.right
                self.__consolidate()
            self.__size -= 1
        return z

    def insert(self, key, value=None):
        n = Node(key, value)
        n.left = n.right = n
        self.__merge_into_root(n)
        if self.__min is None or n.key < self.__min.key:
            self.__min = n
        self.__size += 1

    def decrease_key(self, x, k):
        if k > x.key:
            return None
        x.key = k
        y = x.parent
        if y is not None and x.key < y.key:
            self.__cut(x, y)
            self.__cascading_cut(y)
        if x.key < self.__min.key:
            self.__min = x

    def union(self, h2):
        new_heap = FibHeap()
        new_heap.__root, new_heap.__min = self.__root, self.__min
        last = h2.__root.left
        h2.__root.left = new_heap.__root.left
        new_heap.__root.left.right = h2.__root
        new_heap.__root.left = last
        new_heap.__root.left.right = new_heap.__root
        if h2.__min.key < new_heap.__min.key:
            new_heap.__min = h2.__min
        new_heap.__size = self.__size + h2.__size
        return new_heap

    def delete(self, x):
        x: Node
        self.decrease_key(x, self.__min.key - 1)
        return self.extract_min()

    def __cut(self, x, y):
        x: Node
        y: Node
        y.remove_child(x)
        y.degree -= 1
        self.__merge_into_root(x)
        x.parent = None
        x.mark = False

    def __cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if y.mark is False:
                y.mark = True
            else:
                self.__cut(y, z)
                self.__cascading_cut(z)

    def __consolidate(self):
        array = [None] * int(math.log(self.__size) * 2)
        nodes = [w for w in self.__root.iterate()]
        for x in nodes:
            d = x.degree
            while array[d] is not None:
                y = array[d]
                if x.key > y.key:
                    temp = x
                    x, y = y, temp
                self.__heap_link(y, x)
                array[d] = None
                d += 1
            array[d] = x
        for it in array:
            if it is not None:
                if it.key < self.__min.key:
                    self.__min = it

    def __heap_link(self, y, x):
        x: Node
        y: Node
        self.__remove_from_root(y)
        y.left = y.right = y
        x.add_child(y)
        x.degree += 1
        y.parent = x
        y.mark = False

    def __merge_into_root(self, node):
        if self.__root is None:
            self.__root = node
        else:
            node.right = self.__root.right
            node.left = self.__root
            self.__root.right.left = node
            self.__root.right = node

    def __remove_from_root(self, node):
        if node == self.__root:
            self.__root = node.right
        node.left.right = node.right
        node.right.left = node.left


def make_heap():
    return FibHeap()


if __name__ == '__main__':
    A = [x for x in range(40, 60)]
    B = [x for x in range(10, 30)]
    H1 = make_heap()
    H2 = make_heap()
    for i in A:
        H1.insert(i, i)
    for i in B:
        H2.insert(i, i)
    for i in range(0, 2):
        print(H1.extract_min().key)
    H = H1.union(H2)
    print(H.extract_min().key)


