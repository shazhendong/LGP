# This py file is part of LGP package, which consists of all avaliable logic opeartions as class.
# 
# 

def AND(r, a1, a2):
    #return string specifying r = a1 and a2
    eq = ' = '
    op = ' and '
    return r + eq + a1 + op + a2

def OR(r, a1, a2):
    #return string specifying r = a1 or a2
    eq = ' = '
    op = ' or '
    return r + eq + a1 + op + a2

def NOT(r, a1):
    #return string specifying r = not a1
    eq = ' = '
    op = 'or '
    return r + eq + op + a1