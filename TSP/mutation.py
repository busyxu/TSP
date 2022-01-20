import random
import copy


# 变异
def mutation(N, population, mutationProbability):

    newPopulation = copy.deepcopy(population)

    for pop in population:
        p = random.uniform(0, 1)
        if p < mutationProbability:
            tempP = copy.deepcopy(pop)
            cnt = random.randint(0, int(N/2))  # 变异个数
            while cnt > 0:
                l = random.randint(0, N-1)
                r = random.randint(0, N-1)
                t = tempP.gene[l]
                tempP.gene[l] = tempP.gene[r]
                tempP.gene[r] = t
                cnt -= 1
                pass
            newPopulation.append(tempP)
            pass
        pass

    return newPopulation
