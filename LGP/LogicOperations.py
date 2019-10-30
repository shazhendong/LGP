# This py file is part of LGP package, which consists of all avaliable logic opeartions as class.
# 
# 

class AND:
    def __init__(self, o1, o2, o3):
        self.oprand1 = o1
        self.oprand2 = o2
        self.oprand3 = o3
    
    def equals(self):
        self.oprand3[0] =  self.oprand1[0] and self.oprand2[0]

class OR:
    def __init__(self, o1, o2, o3):
        self.oprand1 = o1
        self.oprand2 = o2
        self.oprand3 = o3
    
    def equals(self):
        self.oprand3[0] =  self.oprand1[0] or self.oprand2[0]

class XOR:
    def __init__(self, o1, o2, o3):
        self.oprand1 = o1
        self.oprand2 = o2
        self.oprand3 = o3
    
    def equals(self):
        self.oprand3[0] =  self.oprand1[0] ^ self.oprand2[0]