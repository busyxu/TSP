

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