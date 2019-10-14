def gale(man, woman, pairNum):
    res = []
    freeM = []
    woman_cur = []
    man_propose = [[0 for i in range (pairNum)]for i in range (pairNum)]

    for i in range(0, pairNum):
        freeM.append(i)
        woman_cur.append(-1)

    while len(freeM) > 0:
        m = freeM[0]
        purpose_woman = 0
        while man_propose[m][man[m][purpose_woman]] == 1:
            purpose_woman +=1;

        w = man[m][purpose_woman]
        man_propose[m][w] = 1
        if woman_cur[w] == -1:
            freeM.pop(0)
            woman_cur[w] = m
        else:
            greenHat = woman_cur[w]
            green = 0
            if woman[w].index(m) < woman[w].index(greenHat):
                woman_cur[w] = m
                freeM.append(greenHat)
                freeM.pop(0)


    for i in range(0, pairNum):
        res.append([woman_cur[i], i])
    return res


def sortRule(list):
    return list[0]

if __name__ == '__main__':
    pairNum = int(input().strip())
    man = []
    woman = []
    for i in range(0, pairNum):
        l = list(map(int, input().strip().split()))
        man.append(l)
    input()
    for i in range(0, pairNum):
        woman.append(list(map(int, input().split())))

    resList = gale(man,woman,pairNum)
    resList.sort(key=sortRule)
    print(resList)