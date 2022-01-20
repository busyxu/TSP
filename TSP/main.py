from TSP import input, init, select, fitness, crossover, mutation


if __name__ == '__main__':

    # 种群大小
    IndividualTotal = 200
    # 进化次数
    maxEvolve = 500
    # 交叉概率
    crossoverProbability = 0.7
    # 变异概率
    mutationProbability = 0.3

    citys = input.input_city()
    N = len(citys)
    dt = init.dt_function(citys)

    population = init.init_population(IndividualTotal, N)
    fitness.FitnessFunction(population, N, dt)
    for i in range(maxEvolve):

        if i % 20 == 0:
            num = []
            index = []
            best = select.BestIndividual(population)
            print(best)
            # print(sorted(best.gene))
            print('****************第', i, '代******************')
            # for pop in population:
            #     print(pop)
            #     print(sorted(pop.gene))
            #     pass
            pass

        population = select.vs_select(IndividualTotal, population) # 竞标赛选择算子
        # population = select.roulette_select(IndividualTotal, population) # 轮盘赌选择算子
        population = crossover.edge_crossover(N, population, crossoverProbability) # 边重组交叉算子 ER
        # population = crossover.oder_crossover(N, population, crossoverProbability) # 顺序交叉算子 OX
        # population = crossover.cycle_crossover(N, population, crossoverProbability)  # 循环交叉算子 CR
        # population = crossover.PMX_crossover(N, population, crossoverProbability)  # 部分匹配交叉算子 CR
        # population = crossover.position_based_crossover(N, population, crossoverProbability)  # 基于位置交叉算子  PBX
        population = mutation.mutation(N, population, mutationProbability)
        fitness.FitnessFunction(population, N, dt)

        pass
    best = select.BestIndividual(population)
    print('***************最优解**************')
    print(best)


    pass

"""
545
550
719
618
613
"""
