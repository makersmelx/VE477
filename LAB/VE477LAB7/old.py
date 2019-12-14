import numpy as np


def Pivot(N, B, A, b, c, v, l, e):
    # print(e)
    new_b = np.zeros(len(b))
    new_b[e] = b[l] / A[l, e]
    new_A = np.zeros((np.size(A, 0), np.size(A, 1)))
    for j in N:
        if j == e:
            continue
        new_A[e, j] = A[l, j] / A[l, e]
    new_A[e, l] = 1 / A[l, e]
    # print(new_A)
    for i in B:
        if i == l:
            continue
        new_b[i] = b[i] - A[i, e] * new_b[e]
        for j in N:
            if j == e:
                continue
            new_A[i, j] = A[i, j] - A[i, e] * new_A[e, j]
        new_A[i, l] = -A[i, e] * new_A[e, l]
    v = v + c[e] * new_b[e]
    new_c = np.zeros(len(c))
    for j in N:
        if j == e:
            continue
        new_c[j] = c[j] - c[e] * new_A[e, j]
    new_c[l] = -c[e] * new_A[e, l]
    N.remove(e)
    N.append(l)
    B.remove(l)
    B.append(e)
    return N, B, new_A, new_b, new_c, v


def calculate(N, B, A, b, c, v, duality):
    m = np.size(A, 0)
    n = np.size(A, 1)
    while len(N) > 0 and c.max() > 0:
        e = np.where(c == c.max())[0][0]
        d = np.zeros(m)
        for i in range(np.size(A, 0)):
            if i in B and A[i, e] > 0:
                d[i] = b[i] / A[i, e]
            else:
                d[i] = float("inf")
        l = np.where(d == d.min())[0][0]
        if d[l] != float("inf"):
            N, B, A, b, c, v = Pivot(N, B, A, b, c, v, l, e)
        else:
            return np.zeros(n), -1
    print("==============================")
    print(b, "\n", c)
    print("==============================")
    if duality:
        x = [0 for i in range(np.size(c))]
        for i in range(np.size(c)):
            if i in N:
                x[i] = c[i]
        y = [0 for i in range(n)]
        for i in range(n):
            if i in B:
                y[i] = b[i]
        return x, y, -v
    else:
        x = [0 for i in range(n)]
        for i in range(n):
            if i in B:
                x[i] = b[i]
        return x, [], v


def Init(A, b, c):
    m = np.size(A, 0)
    n = np.size(A, 1)
    k = np.where(b == b.min())[0][0]
    N = [i for i in range(n)]
    B = [n + i for i in range(m)]
    A = np.vstack((np.zeros([n, m+n]), np.hstack((A, np.zeros([m, m])))))
    b = np.hstack((np.zeros(n), b))
    c = np.hstack((c, [0 for i in range(m)]))
    v = 0
    if b[k+n] >= 0:
        return N, B, A, b, c, v
    A = np.hstack((A, np.zeros([np.size(A, 0), 1])))  # add x0
    A = np.vstack((A, np.zeros([1, np.size(A, 1)])))
    b = np.hstack((b, [0]))
    tmp_c = np.zeros(np.size(c) + 1)  # add x0
    tmp_c[-1] = -1  # -x0
    for i in B:
        A[i, m+n] = -1  # set x0 args
    N.append(m+n)
    l = n + k
    N, B, A, b, tmp_c, v = Pivot(N, B, A, b, tmp_c, v, l, m + n)
    v0 = 0
    m = np.size(A, 0)
    n = np.size(A, 1)
    while len(N) > 0 and tmp_c.max() > 0:
        e = np.where(tmp_c == tmp_c.max())[0][0]
        d = np.zeros(m)
        for i in range(np.size(A, 0)):
            if i in B and A[i, e] > 0:
                d[i] = b[i] / A[i, e]
            else:
                d[i] = float("inf")
        l = np.where(d == d.min())[0][0]
        if d[l] != float("inf"):
            N, B, A, b, tmp_c, v = Pivot(N, B, A, b, tmp_c, v, l, e)
        else:
            print("Error!")
    x0 = [0 for i in range(n)]
    for i in range(n):
        if i in B:
            x0[i] = b[i]
    if x0[-1] != 0:
        return - 1, -1, -1, -1, -1, -1
    if (n - 1) in B:
        # print("!")
        N, B, A, b, tmp_c, v = Pivot(N, B, A, b, tmp_c, v, n - 1, N[0])
    A = A[0: (m-1), 0:(n-1)]
    b = b[0:(n - 1)]
    # print(A)
    # print(b)
    # print(B)
    N.remove(n-1)
    res_c = np.zeros(np.size(c))
    for i in range(np.size(c)):
        res_c[i] = float(c[i])
    for i in range(len(res_c)):
        if res_c[i] != 0 and i in B:
            for j in range(len(res_c)):
                if j == i:
                    continue
                if j in N:
                    res_c[j] = res_c[j] + float(A[i, j] * res_c[i] * (-1))
            v = v + b[i] * res_c[i]
            res_c[i] = 0
            # print("$", res_c, "$")
    # print(res_c)
    return N, B, A, b, res_c, v


def dual(A, b, c):
    if np.size(A, 1) >= np.size(A, 0):
        return A, b, c, 0
    else:
        new_A = np.transpose(A)
        new_A *= -1
        new_b = np.array(c)
        new_b *= -1
        new_c = np.array(b)
        new_c *= -1
        return new_A, new_b, new_c, 1


def simplex(A, b, c, duality):
    m = np.size(A, 0)
    n = np.size(A, 1)
    N, B, A, b, c, v = Init(A, b, c)
    x = []
    # print(A)
    # print(b)
    # print(c)
    x, y, v = calculate(N, B, A, b, c, v, duality)
    if duality:
        print("Solution: ", x[len(x) - m:])
        print("Dual solution: ", y[:n])
        print("Value:", v)
    else:
        print("Solution: ", x[:n])
        print("Value:", v)


if __name__ == '__main__':
    # A = np.matrix([[1, 1, 3], [2, 2, 5], [4, 1, 2]])
    # b = np.array([30, 24, 36])
    # c = np.array([3, 1, 2])
    # A, b, c, duality = dual(A, b, c)
    # simplex(A, b, c, duality)
    # print("=======No symmetric\n\n")
    # A = np.matrix([[2, -1], [1, -5]])
    # b = np.array([2, -4])
    # c = np.array([2, -1])
    # A, b, c, duality = dual(A, b, c)
    # simplex(A, b, c, duality)
    print("=====================\n\nTest case!")
    A = np.matrix([[-1/2, -1], [-2, -2], [-1, -4]])
    b = np.array([-6, -14, -13])
    c = np.array([-24, -60])
    # print(simplex(A, b, c, 0))
    A, b, c, duality = dual(A, b, c)
    simplex(A, b, c, duality)
