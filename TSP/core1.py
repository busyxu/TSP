import sys
import copy
import random
import numpy as np
import math
import matplotlib.pyplot as plt
import xlrd

# 惩罚，比如超过背包容量后的适应度=punish
punish = 0.1
# 个体数
IndividualTotal = 200
# 进化次数
maxEvolve = 600
# 交叉概率
crossoverProbability = 0.7
# 变异概率
mutationProbability = 0.2

# 城市
class city(object):
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        pass
    def __str__(self):
        return '[%s %s %s]\n' % (self.id, self.x, self.y)
    pass

# 个体
class individual(object):
    def __init__(self, gene, value, fitness, lp, rp):
        self.gene = gene
        self.value = value
        self.fitness = fitness
        self.lp = lp
        self.rp = rp
        pass

    def __str__(self, *args, **kwargs):
        print(self.gene)
        return '[value=%s fitness=%s lp=%s rp=%s]\n' % (self.value, self.fitness, self.lp, self.rp)

    __repr__ = __str__
    pass


# 初始化种群 基因表从1开始
def initPopulation(IndividualTotal, N):
    population = []
    ca = 0
    while ca < IndividualTotal:

        # 通过random随机打乱数组方法
        gene = []
        for i in range(N):
            gene.append(i+1)
            pass
        random.shuffle(gene)

        ## 自行编写方法
        # gene = [random.randint(1, N) for i in range(N)]
        # temp = [0 for i in range(N+1)]
        # temp[0] = -1
        # for i, p in enumerate(gene):
        #     if temp[p] == 1:
        #         gene[i] = 0
        #         pass
        #     else:
        #         temp[p] = 1
        #         pass
        #
        #     pass
        # rnum = []
        # # 将基因表中没有的归档
        # for i, v in enumerate(temp):
        #     if v == 0:
        #         rnum.append(i)
        #         pass
        #     pass
        #
        # j = 0
        # for i, p in enumerate(gene):
        #     if p == 0:
        #         gene[i] = rnum[j]
        #         j += 1
        #         pass
        #     pass


        t = individual(gene, 0, 0, 0, 0)
        population.append(t)
        ca += 1
        pass

    return population


def dt_function(citys):
    n = len(citys)
    dt = [[0]*n for i in range(n)]
    for i, c1 in enumerate(citys):
        for j, c2 in enumerate(citys):
            dt[i][j] = math.sqrt((c1.x-c2.x)**2 + (c1.y-c2.y)**2)
            pass
        pass

    return dt

# 适应度评估函数
def FitnessFunction(population, N, dt):
    totalFitness = 0
    for i in population:
        i.value = 0
        i.fitness = 0
        wt = 0
        for j in range(N-1):
            c1 = i.gene[j]
            c2 = i.gene[j+1]
            i.value += dt[c1-1][c2-1]
            pass
        i.value += dt[N-1][0]
        i.fitness = 1.0/i.value
        totalFitness += i.fitness
        pass

    lastP = 0.0
    for i in population:
        p = i.fitness / totalFitness
        i.lp = lastP
        i.rp = lastP + p
        lastP = i.rp
        pass

    pass

# 最优个体
def BestIndividual(population):
    # max = 0.0
    min = sys.maxsize
    for i in population:
        # if i.fitness > max:
        #     max = i.fitness
        #     best = i
        #     pass
        if i.value < min:
            min = i.value
            best = i
            pass
        pass
    return best


# 更新总群
def selectPopulation(IndividualTotal, population):
    newPopulation = []
    best = BestIndividual(population)
    newPopulation.append(best)
    for i in range(IndividualTotal-1):
        p1 = random.randint(0, IndividualTotal-1)
        p2 = random.randint(0, IndividualTotal-1)
        while p1 == p2:
            p1 = random.randint(0, IndividualTotal-1)
            p2 = random.randint(0, IndividualTotal-1)
            pass

        if population[p1].value <= population[p2].value:
            newPopulation.append(copy.deepcopy(population[p1]))
            pass
        else:
            newPopulation.append(copy.deepcopy(population[p2]))
            pass

        # flag = True
        # for pop in population:
        #     if p >= pop.lp and p < pop.rp:
        #         newPopulation.append(copy.deepcopy(pop))
        #         flag = False
        #         break
        #         pass
        #     pass
        # if flag:
        #     newPopulation.append(copy.deepcopy(best))
        #     pass

        pass
    return newPopulation

# edge recombination
def edge_crossover(N, population):
    # newPopulation = copy.deepcopy(population)
    flag = False
    for index, pop in enumerate(population):
        p = random.uniform(0, 1)
        if p < crossoverProbability:
            if flag == False:
                fa = index
                flag = True
                pass

            elif flag == True:

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
                population[fa].gene = offStringFa
                population[ma].gene = offStringMa
                # newPopulation.append(offStringFa)
                # newPopulation.append(offStringMa)
                pass

                flag = False

                pass


            pass

        pass
    # return newPopulation
    pass

# oder crossover
def oder_crossover(N, population):
    flag = True
    for idx, pop in enumerate(population):
        p = random.uniform(0, 1)
        if p < crossoverProbability:
            if flag:
                fa = idx
                flag = False
                pass
            else:
                ma = idx
                l = random.randint(0, N-1)
                r = random.randint(l, N-1)
                numFa = []
                for i, g in enumerate(population[fa].gene):
                    t = (r+i) % N
                    if population[fa].gene[t] not in population[ma].gene[l:r]:
                        numFa.append(population[fa].gene[t])
                        pass
                    pass
                numMa = []
                for i, g in enumerate(population[ma].gene):
                    t = (r + i) % N
                    if population[ma].gene[t] not in population[fa].gene[l:r]:
                        numMa.append(population[ma].gene[t])
                        pass
                    pass
                m = len(numFa)
                for i, g in enumerate(population[ma].gene):
                    t = (r+i) % N
                    if i < m:
                        population[ma].gene[t] = numFa[i]
                        pass
                    pass

                m = len(numMa)
                for i, g in enumerate(population[fa].gene):
                    t = (r + i) % N
                    if i < m:
                        population[fa].gene[t] = numMa[i]
                        pass
                    pass
                pass
            pass
        pass
    pass


# 变异
def mutation(N, population):
    for pop in population:
        p = random.uniform(0, 1)
        if p < mutationProbability:
            cnt = random.randint(0, int(N/2))  # 变异个数
            while cnt > 0:
                l = random.randint(1, N-1)
                r = random.randint(1, N-1)
                t = pop.gene[l]
                pop.gene[l] = pop.gene[r]
                pop.gene[r] = t
                cnt -= 1
                pass

            pass
        pass
    pass


if __name__ == '__main__':

    book = xlrd.open_workbook('eil51tsp.xlsx')  # 打开一个excel
    sheet = book.sheet_by_index(0)  # 根据顺序获取sheet
    citys = []
    for i in range(sheet.nrows):  # 0 1 2 3 4 5
        if i == 0:
            continue
        row = sheet.row_values(i)
        t = city(row[0], row[1], row[2])
        citys.append(t)
        pass
    N = sheet.nrows - 1

    dt = dt_function(citys)
    population = initPopulation(IndividualTotal, N)
    FitnessFunction(population, N, dt)
    for i in range(maxEvolve):
        if i % 30 == 0:
            num = []
            index = []
            best = BestIndividual(population)
            print(best)
            # print(sorted(best.gene))
            print('**********************************')
            # for pop in population:
            #     print(pop)
            #     pass
            pass

        population = selectPopulation(IndividualTotal, population)
        edge_crossover(N, population)
        # oder_crossover(N, population)
        mutation(N, population)
        FitnessFunction(population, N, dt)
        pass
    best = BestIndividual(population)
    print('***************最优解**************')
    print(best)
