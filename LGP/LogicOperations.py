# This py file is part of LGP package, which consists of all avaliable logic opeartions as class.
# 
# 

def AND(r, a1, a2):
    #return string specifying r = a1 and a2
    eq = ' = '
    op = ' and '
    return r + eq + a1 + op + a2 + '\n'

def OR(r, a1, a2):
    #return string specifying r = a1 or a2
    eq = ' = '
    op = ' or '
    return r + eq + a1 + op + a2 + '\n'

def NOT(r, a1):
    #return string specifying r = not a1
    eq = ' = '
    op = 'not '
    return r + eq + op + a1 + '\n'

def IF(str_condition):
    # return string specifying if statement
    return 'if ' + str_condition + ':' + '\n'

def GEQ_If(a1, a2):
    # return string specifying a1 >= a2
    return a1 + ' >= ' + a2

def EQ_If(a1, a2):
    # return string specifying a1 == a2
    return a1 + ' == ' + a2

def SEQ_If(a1, a2):
    # return string specifying a1 == a2
    return a1 + ' <= ' + a2