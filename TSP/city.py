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