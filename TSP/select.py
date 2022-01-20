import random
import sys
import copy

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
def vs_select(IndividualTotal, population):
    Plen = len(population)
    newPopulation = []
    best = BestIndividual(population)
    newPopulation.append(best)
    k = 0
    while k < IndividualTotal:
        p1 = random.randint(0, Plen-1)
        p2 = random.randint(0, Plen-1)
        while p1 == p2:
            p1 = random.randint(0, Plen-1)
            p2 = random.randint(0, Plen-1)
            pass

        if population[p1].value <= population[p2].value:
            newPopulation.append(copy.deepcopy(population[p1]))
            pass
        else:
            newPopulation.append(copy.deepcopy(population[p2]))
            pass

        k += 1
        pass
    return newPopulation


# 更新总群
def roulette_select(IndividualTotal, population):
    # Plen = len(population)
    newPopulation = []
    best = BestIndividual(population)
    newPopulation.append(best)
    k = 0
    while k < IndividualTotal:

        flag = True
        p = random.uniform(0, 1)
        for pop in population:
            if p >= pop.lp and p < pop.rp:
                newPopulation.append(copy.deepcopy(pop))
                flag = False
                break
                pass
            pass
        if flag:
            newPopulation.append(copy.deepcopy(best))
            pass
        k += 1
        pass
    return newPopulation