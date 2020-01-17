# This py file is part of LGP package, which consists of all avaliable math opeartions as class.
# 
# 

def add(r, a1, a2):
    #return string specifying r = a1 + a2
    eq = ' = '
    op = ' + '
    return r + eq + a1 + op + a2

def sub(r, a1, a2):
    #return string specifying r = a1 - a2
    eq = ' = '
    op = ' - '
    return r + eq + a1 + op + a2


def mul(r, a1, a2):
    #return string specifying r = a1 * a2
    eq = ' = '
    op = ' * '
    return r + eq + a1 + op + a2

def div_protected(r, a1, a2):
    #return string specifying r = a1 / a2, if a2 = 0 then r = 0
    eq = ' = '
    op = ' / '
    protectCondition = ' if ' + a2 + ' != 0 else 0'
    return r + eq + a1 + op + a2 + protectCondition
