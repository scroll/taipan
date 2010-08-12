class inventory(object):
    def __init__(self, **kwargs):
        self.commodities = ['opium', 'silk', 'arms', 'general']
        self.opium = 0
        self.silk = 0
        self.arms = 0
        self.general = 0
        self.size = 50

    def overloaded(self):
        if self.vacant() < 0:
            return True
        else:
            return False

    def vacant(self):
        vacant = 0
        for i in self.commodities:
            vacant += self.__dict__[i]
        return self.size - vacant
        
        




