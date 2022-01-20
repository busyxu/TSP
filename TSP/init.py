import random
from TSP import individual
import math

# 构造距离矩阵
def dt_function(citys):
    n = len(citys)
    dt = [[0]*n for i in range(n)]
    for i, c1 in enumerate(citys):
        for j, c2 in enumerate(citys):
            dt[i][j] = math.sqrt((c1.x-c2.x)**2 + (c1.y-c2.y)**2)
            pass
        pass

    return dt

# 初始化种群 基因表从1开始
def init_population(IndividualTotal, N):
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


        t = individual.individual(gene, 0, 0, 0, 0)
        population.append(t)
        ca += 1
        pass

    return population