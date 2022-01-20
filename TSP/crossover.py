import copy
import random
from TSP import individual


# edge recombination 边重组
def edge_crossover(N, population, crossoverProbability):
    newPopulation = copy.deepcopy(population)
    flag = True
    for index, pop in enumerate(population):
        p = random.uniform(0, 1)
        if p < crossoverProbability:
            if flag:
                fa = index
                flag = False
                pass

            else:
                flag = True
                ma = index
                num = {}
                for i, v in enumerate(population[fa].gene):
                    if i == 0:
                        t = []
                        t.append(population[fa].gene[-1])
                        t.append(population[fa].gene[i+1])
                        num.update({v: t})
                        pass
                    elif i == N-1:
                        t = []
                        t.append(population[fa].gene[i-1])
                        t.append(population[fa].gene[0])
                        num.update({v: t})
                        pass
                    else:
                        t = []
                        t.append(population[fa].gene[i-1])
                        t.append(population[fa].gene[i+1])
                        num.update({v: t})
                        pass
                    pass

                for i, v in enumerate(population[ma].gene):

                    if i == 0:
                        # 改进后 加负号
                        f1 = True
                        f2 = True
                        for j, ps in enumerate(num[v]):
                            if population[ma].gene[-1] == ps:
                                num[v][j] = 0-num[v][j] # 加负号
                                f1 = False
                                break
                                pass

                            if population[ma].gene[i+1] == ps:
                                num[v][j] = 0-num[v][j] # 加负号
                                f2 = False
                                break
                                pass

                            pass

                        if f1:
                            num[v].append(population[ma].gene[-1])
                            pass

                        if f2:
                            num[v].append(population[ma].gene[i+1])
                            pass

                        # 改进前 不加负号
                        # if population[ma].gene[-1] not in num[v]:
                        #     num[v].append(population[fa].gene[-1])
                        #     pass
                        #
                        # if population[ma].gene[i+1] not in num[v]:
                        #     num[v].append(population[fa].gene[i+1])
                        #     pass

                        pass

                    elif i == N-1:

                        # 改进后 加负号
                        f1 = True
                        f2 = True
                        for j, ps in enumerate(num[v]):
                            if population[ma].gene[i-1] == ps:
                                num[v][j] = 0 - num[v][j]  # 加负号
                                f1 = False
                                break
                                pass

                            if population[ma].gene[0] == ps:
                                num[v][j] = 0 - num[v][j]  # 加负号
                                f2 = False
                                break
                                pass

                            pass

                        if f1:
                            num[v].append(population[ma].gene[i-1])
                            pass

                        if f2:
                            num[v].append(population[ma].gene[0])
                            pass

                        # 改进前 不加负号
                        # if population[ma].gene[i-1] not in num[v]:
                        #     num[v].append(population[fa].gene[i-1])
                        #     pass
                        #
                        # if population[ma].gene[0] not in num[v]:
                        #     num[v].append(population[fa].gene[0])
                        #     pass

                        pass

                    else:

                        # 改进后 加负号
                        f1 = True
                        f2 = True
                        for j, ps in enumerate(num[v]):
                            if population[ma].gene[i-1] == ps:
                                num[v][j] = 0 - num[v][j]  # 加负号
                                f1 = False
                                break
                                pass

                            if population[ma].gene[i + 1] == ps:
                                num[v][j] = 0 - num[v][j]  # 加负号
                                f2 = False
                                break
                                pass

                            pass

                        if f1:
                            num[v].append(population[ma].gene[i-1])
                            pass

                        if f2:
                            num[v].append(population[ma].gene[i + 1])
                            pass

                        # 改进前 不加负号
                        # if population[ma].gene[i-1] not in num[v]:
                        #     num[v].append(population[ma].gene[i-1])
                        #     pass
                        #
                        # if population[ma].gene[i+1] not in num[v]:
                        #     num[v].append(population[ma].gene[i+1])
                        #     pass

                        pass
                    pass

                # print('num', num)
                # offstring
                offStringFa = []
                offStringMa = []

                offStringFa.append(population[fa].gene[0])
                offStringMa.append(population[ma].gene[0])

                # 父亲子代
                it = 0
                while len(offStringFa) < N:

                    t1 = num[offStringFa[it]] # 找到当前城市的邻接城市
                    r = [] # 存邻接城市的信息
                    t2 = 0 # 最后一个负号城市, 假设为第一个
                    idx = 0
                    f = False
                    for k in t1: # 遍历每个邻接城市的邻接城市
                        if abs(k) not in offStringFa:
                            if k < 0:
                                r.append(num[0-k])
                                t2 = idx
                                # idx += 1
                                pass

                            else:
                                r.append(num[k])
                                # idx += 1
                                pass
                            f = True
                            pass
                        else:
                            r.append([0, 0, 0, 0, 0])
                            pass
                        idx += 1

                        pass

                    if f:
                        # t2 位置一定有，因为r是offString中没有的
                        # print('t2', t2)
                        cy = t1[t2]
                        # print('cy it', cy, it)
                        min = len(r[t2])
                        for idx, c in enumerate(r):
                            if t1[idx] not in offStringFa:
                                # print(t1[idx], offStringFa)
                                if len(c) < min:
                                    min = len(c)
                                    cy = t1[idx]
                                    pass
                                pass

                            pass
                        pass

                    else:
                        for t3 in range(N):
                            if t3+1 not in offStringFa:
                                cy = t3+1
                                # print('aaaa', t3+1, it)
                                break
                                pass
                            pass
                        pass
                    # if abs(cy) in offStringFa:
                    #     print(cy, it, t2)
                    # if abs(cy) not in offStringFa:
                    #     offStringFa.append(abs(cy))
                    #     it += 1
                    #     pass
                    offStringFa.append(abs(cy))
                    it += 1

                    pass

                # 母亲子代
                it = 0
                while len(offStringMa) < N:

                    t1 = num[offStringMa[it]]  # 找到当前城市的邻接城市
                    r = []  # 存邻接城市的信息
                    t2 = 0  # 最后一个负号城市, 假设为第一个
                    idx = 0
                    f = False
                    for k in t1:  # 遍历每个邻接城市的邻接城市

                        if abs(k) not in offStringMa:
                            if k < 0:
                                r.append(num[0-k])
                                t2 = idx
                                # idx += 1
                                pass

                            else:
                                r.append(num[k])
                                # idx += 1
                                pass
                            f = True
                            pass
                        else:
                            r.append([0, 0, 0, 0, 0])
                            pass
                        idx += 1
                        pass

                    if f:
                        # print('t2', t2)
                        cy = t1[t2]
                        min = len(r[t2])
                        for idx, c in enumerate(r):
                            if t1[idx] not in offStringMa:
                                if len(c) < min:
                                    min = len(c)
                                    cy = t1[idx]
                                    pass
                                pass

                            pass
                        pass

                    else:
                        for t3 in range(N):
                            if t3 + 1 not in offStringMa:
                                cy = t3 + 1
                                break
                                pass
                            pass
                        pass

                    offStringMa.append(abs(cy))

                    it += 1
                    pass
                # print(sorted(offStringFa))
                # print(sorted(offStringMa))
                # population[fa].gene = offStringFa
                # population[ma].gene = offStringMa
                child1 = individual.individual(offStringFa, 0, 0, 0, 0)
                child2 = individual.individual(offStringMa, 0, 0, 0, 0)
                newPopulation.append(child1)
                newPopulation.append(child2)
                pass

            pass

        pass
    return newPopulation


# oder crossover 顺序交叉
def oder_crossover(N, population, crossoverProbability):
    newPopulation = copy.deepcopy(population)
    flag = True
    for idx, pop in enumerate(population):

        p = random.uniform(0, 1)
        if p < crossoverProbability:
            if flag:
                fa = idx
                flag = False
                pass
            else:
                flag = True
                ma = idx
                # print('*************************')
                # print(population[fa])
                # print(population[ma])
                l = random.randint(0, N-1)
                r = random.randint(l, N-1)
                # print(l, r)
                numFa = []
                for i, g in enumerate(population[fa].gene):
                    t = (r+i) % N
                    if population[fa].gene[t] not in population[ma].gene[l:r]:
                        numFa.append(population[fa].gene[t])
                        pass
                    pass
                # print('numFa', numFa)
                numMa = []
                for i, g in enumerate(population[ma].gene):
                    t = (r + i) % N
                    if population[ma].gene[t] not in population[fa].gene[l:r]:
                        numMa.append(population[ma].gene[t])
                        pass
                    pass
                # print('numMa', numMa)

                tempMa = copy.deepcopy(population[ma])
                m = len(numFa)
                for i, g in enumerate(tempMa.gene):
                    t = (r+i) % N
                    if i < m:
                        tempMa.gene[t] = numFa[i]
                        pass
                    pass

                tempFa = copy.deepcopy(population[fa])
                m = len(numMa)
                for i, g in enumerate(tempFa.gene):
                    t = (r + i) % N
                    if i < m:
                        tempFa.gene[t] = numMa[i]
                        pass
                    pass

                newPopulation.append(tempMa)
                newPopulation.append(tempFa)
                # print(population[fa])
                # print(population[ma])
                # print('--------------------')
                pass
            pass
        pass
    return newPopulation


# cycle crossover 循环交叉
def cycle_crossover(N, population, crossoverProbability):
    newPopulation = copy.deepcopy(population)
    flag = True
    for idx, pop in enumerate(population):
        p = random.uniform(0, 1)
        if p < crossoverProbability:
            if flag:
                fa = idx
                flag = False
                pass
            else:
                flag = True
                ma = idx
                # childFa = copy.deepcopy(population[fa])
                # childMa = copy.deepcopy(population[ma])
                childFa = [0]*N
                # t1 = 0
                t = 0
                childFa[0] = population[fa].gene[0]
                while population[fa].gene[0] != population[ma].gene[t]:
                    for i, s in enumerate(population[fa].gene):
                        if population[ma].gene[t] == s:
                            t = i
                            childFa[t] = population[fa].gene[i]
                            break
                            pass
                        pass
                    pass
                for i, s in enumerate(population[ma].gene):
                    if childFa[i] == 0:
                        childFa[i] = s
                        pass
                    pass

                childMa = [0] * N
                # t1 = 0
                t = 0
                childMa[0] = population[ma].gene[0]
                while population[ma].gene[0] != population[fa].gene[t]:
                    for i, s in enumerate(population[ma].gene):
                        if population[fa].gene[t] == s:
                            t = i
                            childMa[t] = population[ma].gene[i]
                            break
                            pass
                        pass
                    pass
                for i, s in enumerate(population[fa].gene):
                    if childMa[i] == 0:
                        childMa[i] = s
                        pass
                    pass

                child1 = individual.individual(childFa, 0, 0, 0, 0)
                child2 = individual.individual(childMa, 0, 0, 0, 0)
                newPopulation.append(child1)
                newPopulation.append(child2)

                pass
            pass
        pass
    return newPopulation


# PMX 部分匹配交叉
def PMX_crossover(N, population, crossoverProbability):
    newPopulation = copy.deepcopy(population)
    flag = True
    for idx, pop in enumerate(population):
        p = random.uniform(0, 1)
        if p < crossoverProbability:
            if flag:
                fa = idx
                flag = False
                pass
            else:
                flag = True
                ma = idx
                l = random.randint(0, N - 1)
                r = random.randint(l, N - 1)
                # print(population[fa].gene)
                # print(population[ma].gene)
                # print(l, r)
                mapFa = {}
                mapMa = {}
                for i, s in enumerate(population[fa].gene[l:r]):
                    t = population[ma].gene[l+i]
                    # tt = t
                    while t in population[fa].gene[l:r] and t != s:
                        for j, v in enumerate(population[fa].gene[l:r]):
                            if t == v:
                                t = population[ma].gene[l+j]
                                break
                                pass
                            pass
                        pass
                    # if s == t:
                    #     t = population[ma].gene[l+i]
                    #     pass
                    mapFa.update({s: t})
                    pass

                for i, s in enumerate(population[ma].gene[l:r]):
                    t = population[fa].gene[l+i]
                    # tt = t
                    while t in population[ma].gene[l:r] and t != s:
                        for j, v in enumerate(population[ma].gene[l:r]):
                            if t == v:
                                t = population[fa].gene[l+j]
                                break
                                pass
                            pass
                        pass
                    # if s == t:
                    #     t = population[ma].gene[l+i]
                    #     pass

                    mapMa.update({s: t})
                    pass


                # print(mapFa)
                # print(mapMa)


                childFa = [0]*N
                childMa = [0]*N

                for i in range(N):
                    # print('i', i)
                    if i >= l and i < r:
                        childFa[i] = population[ma].gene[i]
                        pass
                    elif population[fa].gene[i] in population[ma].gene[l:r]:
                        childFa[i] = mapMa[population[fa].gene[i]]
                        pass
                    else:
                        childFa[i] = population[fa].gene[i]
                        pass
                    pass

                # print('fa', childFa)


                for i in range(N):
                    if i >= l and i < r:
                        childMa[i] = population[fa].gene[i]
                        pass
                    elif population[ma].gene[i] in population[fa].gene[l:r]:
                        childMa[i] = mapFa[population[ma].gene[i]]
                        pass
                    else:
                        childMa[i] = population[ma].gene[i]
                        pass
                    pass
                # print('ma', childMa)

                child1 = individual.individual(childFa, 0, 0, 0, 0)
                child2 = individual.individual(childMa, 0, 0, 0, 0)
                newPopulation.append(child1)
                newPopulation.append(child2)

                pass
            pass
        pass
    return newPopulation


# position_based_crossover 基于位置交叉
def position_based_crossover(N, population, crossoverProbability):
    newPopulation = copy.deepcopy(population)
    flag = True
    for idx, pop in enumerate(population):
        p = random.uniform(0, 1)
        if p < crossoverProbability:
            if flag:
                fa = idx
                flag = False
                pass
            else:
                flag = True
                ma = idx
                size = random.randint(0, N)
                rnum = []
                childFa = [0]*N
                for i, v in enumerate(population[fa].gene):
                    p = random.uniform(0, 1)
                    if p < size/N:
                        rnum.append(v)
                        childFa[i] = v
                        pass
                    pass
                numFa = []
                for v in population[ma].gene:
                    if v not in rnum:
                        numFa.append(v)
                        pass
                    pass
                c = 0
                for i, v in enumerate(childFa):
                    if v == 0:
                        childFa[i] = numFa[c]
                        c += 1
                        pass
                    pass


                rnum = []
                childMa = [0] * N
                for i, v in enumerate(population[ma].gene):
                    p = random.uniform(0, 1)
                    if p < size / N:
                        rnum.append(v)
                        childMa[i] = v
                        pass
                    pass
                numMa = []
                for v in population[fa].gene:
                    if v not in rnum:
                        numMa.append(v)
                        pass
                    pass
                c = 0
                for i, v in enumerate(childMa):
                    if v == 0:
                        childMa[i] = numMa[c]
                        c += 1
                        pass
                    pass

                child1 = individual.individual(childFa, 0, 0, 0, 0)
                child2 = individual.individual(childMa, 0, 0, 0, 0)
                newPopulation.append(child1)
                newPopulation.append(child2)

                pass
            pass
        pass
    return newPopulation