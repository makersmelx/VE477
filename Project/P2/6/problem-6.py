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

    def remove_child(self, node):
        if self.child == self.child.right:
            self.child = None
        elif self.child == node:
            self.child = node.right
            node.right.self = self
        node.left.right = node.right
        node.right.left = node.left


class FibHeap:
    __min: Node = None
    __size: int = 0
    __value_dict = {}

    def empty(self):
        return self.__size == 0

    def minimum(self):
        return self.__min.value

    def get_size(self):
        return self.__size

    def extract_min(self):
        z = self.__min
        if z is not None:
            p: Node
            q: Node
            while z.child is not None:
                p = z.child
                p.parent = None
                if p == p.right:
                    z.child = None
                else:
                    p.left.right = p.right
                    p.right.left = p.left
                    z.child = p.right
                self.__merge_into_root(p)
            self.__size -= 1
            if self.__size == 0:
                self.__min = None
            else:
                self.__min = z.right
                z.left.right = z.right.left
                z.left.right = z.right
                self.__consolidate()
            return z.value

    def insert(self, key, value):
        n = Node(key, value)
        self.__merge_into_root(n)
        self.__value_dict[value] = n
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
        new_heap.__min = self.__min
        last = h2.__min.left
        h2.__min.left = new_heap.__min.left
        new_heap.__min.left.right = h2.__min
        new_heap.__min.left = last
        new_heap.__min.left.right = new_heap.__min
        if h2.__min.key < new_heap.__min.key:
            new_heap.__min = h2.__min
        new_heap.__size = self.__size + h2.__size
        return new_heap

    def delete(self, value):
        x = self.__value_dict.get(value, None)
        if x is None:
            return
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
        array = [None] * self.__size
        itr = self.__min
        while True:
            x = itr
            itr = itr.right
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
            if itr == self.__min:
                break
        self.__min = None
        for it in array:
            if it is not None:
                self.__merge_into_root(it)

    def __heap_link(self, y, x):
        x: Node
        y: Node
        y.left.right = y.right
        y.right.left = y.left
        if x.child is None:
            y.left = y.right = y
            y.parent = x
            x.child = y
        else:
            y.left = x.child
            y.right = x.child.right
            x.child.right.left = y
            x.child.right = y
            y.parent = x
        x.degree += 1

    def __merge_into_root(self, node):
        if self.__min is None:
            node.right = node.left = node
            self.__min = node
        else:
            node.right = self.__min.right
            node.left = self.__min
            self.__min.right.left = node
            self.__min.right = node
            if node.key < self.__min.key:
                self.__min = node


def make_heap():
    return FibHeap()


if __name__ == '__main__':
    A = [x for x in range(40, 60)]
    B = [x for x in range(10, 30)]
    print("A\n")
    print(A)
    print("="*100, "\nB\n")
    print(B)
    print("=" * 100, "\n\n")
    print("\033[1;30;47mNext is Delete and Extract_min Demo\033[0m\n")
    tmp = input()
    H1 = make_heap()
    H1_compare = make_heap()
    H2 = make_heap()
    for i in A:
        H1.insert(i, str(i) + "th horseCow")
        H1_compare.insert(i, str(i)+"th horseCow")
    for i in B:
        H2.insert(i, str(i) + "th SickMadCow")
    H1_compare.delete("41th horseCow")
    H1_compare.delete("45th horseCow")
    print("\nNot deleted\n")
    for i in range(5):
        if i == 1 or i == 4:
            print("\033[1;35m%s\033[0m" % H1.extract_min(), end="  ")
        else:
            print(H1.extract_min(), end="  ")

    print()
    print("=" * 100, "\nDeleted\n")

    for i in range(0, 5):
        if i == 1 or i == 4:
            print("\033[1;35m%s\033[0m" % H1_compare.extract_min(), end="  ")
        else:
            print(H1_compare.extract_min(), end="  ")

    print()
    print("=" * 100, "\n\n")

    print("\033[1;30;47mNext is Union Demo\033[0m\n")
    tmp = input()
    H = H1.union(H2)
    for i in range(H.get_size()):
        print(H.extract_min(), end="  ")
        if i % 5 == 4:
            print()
