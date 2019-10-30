# This py file is part of LGP package, which consists of all avaliable math opeartions as class.
# 
# 

class add:
    def __init__(self, o1, o2):
        self.oprand1 = o1
        self.oprand2 = o2
    
    def equals(self):
        return self.oprand1[0] + self.oprand2[0]

class subtract:
    def __init__(self, o1, o2):
        self.oprand1 = o1
        self.oprand2 = o2
    
    def equals(self):
        return self.oprand1[0] - self.oprand2[0]

class multiplication:
    def __init__(self, o1, o2):
        self.oprand1 = o1
        self.oprand2 = o2
    
    def equals(self):
        return self.oprand1[0] * self.oprand2[0]

class protectedDivition:
    # protected division, return 0 if divided by 0
    def __init__(self, o1, o2):
        self.oprand1 = o1
        self.oprand2 = o2
    
    def equals(self):
        if self.oprand2[0] == 0:
            return 0
        else:
            return self.oprand1[0] / self.oprand2[0]
