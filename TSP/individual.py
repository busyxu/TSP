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