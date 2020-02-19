import ArithmeticOperations
import LogicOperations
import random

class individual:
    def __init__(self, arr_registers_output, arr_registers_arithmatic, arr_registers_var, arr_operators):
        '''
        This function initialize the basic compoents for an LGP individual, including:
            the name of output registers (arr_registers_output), 
            the name of arithmatic registers (arr_registers_arithmatic),
            the name of feature values (arr_registers_var),
            and the aviliable operators (arr_operators in {'add','sub','mul','div','and','or','not','if'}).
        '''
        self.arr_registers_output = arr_registers_output
        self.arr_registers_arithmatic = arr_registers_arithmatic
        self.arr_registers_var = arr_registers_var
        self.arr_operators = arr_operators

    def generate_program(self, len):
        '''
        This function return a program with a lenth of len.
        '''
        self.target_registers = self.arr_registers_output + self.arr_registers_arithmatic
        self.oprand_registers = self.arr_registers_output + self.arr_registers_arithmatic + self.arr_registers_var
        #program = ['#Program start\n']
        #for x in range(len):
        #    program = program + [self.generate_one_operation()]
        program = [self.generate_one_operation() for x in range(len)]
        return program

    def generate_one_operation(self):
        op = random.choice(self.arr_operators)
        if op == 'add':
            target = random.choice(self.target_registers)
            oprand1 = random.choice(self.oprand_registers)
            oprand2 = random.choice(self.oprand_registers)
            return ArithmeticOperations.add(target,oprand1,oprand2)
        if op == 'sub':
            target = random.choice(self.target_registers)
            oprand1 = random.choice(self.oprand_registers)
            oprand2 = random.choice(self.oprand_registers)
            return ArithmeticOperations.sub(target,oprand1,oprand2)
        if op == 'mul':
            target = random.choice(self.target_registers)
            oprand1 = random.choice(self.oprand_registers)
            oprand2 = random.choice(self.oprand_registers)
            return ArithmeticOperations.mul(target,oprand1,oprand2)
        if op == 'div':
            target = random.choice(self.target_registers)
            oprand1 = random.choice(self.oprand_registers)
            oprand2 = random.choice(self.oprand_registers)
            return ArithmeticOperations.div_protected(target,oprand1,oprand2)
        if op == 'and':
            target = random.choice(self.target_registers)
            oprand1 = random.choice(self.oprand_registers)
            oprand2 = random.choice(self.oprand_registers)
            return LogicOperations.AND(target,oprand1,oprand2)
        if op == 'or':
            target = random.choice(self.target_registers)
            oprand1 = random.choice(self.oprand_registers)
            oprand2 = random.choice(self.oprand_registers)
            return LogicOperations.OR(target,oprand1,oprand2)
        if op == 'not':
            target = random.choice(self.target_registers)
            oprand1 = random.choice(self.oprand_registers)
            return LogicOperations.NOT(target,oprand1)
        if op == 'if':
            oprand1 = random.choice(self.oprand_registers)
            oprand2 = random.choice(self.oprand_registers)
            cond_op = random.choice(['>=','==','<='])
            condition = ''
            if cond_op == '>=':
                condition = LogicOperations.GEQ_If(oprand1, oprand2)
            if cond_op == '==':
                condition = LogicOperations.EQ_If(oprand1, oprand2)
            if cond_op == '<=':
                condition = LogicOperations.SEQ_If(oprand1, oprand2)
            return LogicOperations.IF(condition)

    def toString(self):
        print(self.arr_registers_output)
        print(self.arr_registers_arithmatic)
        print(self.arr_registers_var)
        return 'ok'

def compile_program(arr_program):
    # this function compile the array of program to byte code
    # preprocessing
    arr = arr_program.copy()
    arr = Fix_Program_lastLineAsIF(arr)
    arr = indentation(arr)
    #print(arr)
    codeInString = ''.join([str(elem) for elem in arr])
    #print(codeInString)
    return compile(codeInString, 'gpindividual', 'exec')

def printProgram(arr_program):
    # this function print a program
    # preprocessing
    arr = arr_program.copy()
    arr = Fix_Program_lastLineAsIF(arr)
    arr = indentation(arr)
    codeInString = ''.join([str(elem) for elem in arr])
    return codeInString

def indentation(arr):
    # this function make sure if statement works. it add indentation befor the first line after if statement
    # this function assume the if operation skip one line only
    level = 0
    for i in range(len(arr)):
        if arr[i].split(' ')[0] == 'if':
            level = level+1
            arr[i] = arr[i] + '\t'*level
            continue
        level = 0
    return arr

def Fix_Program_lastLineAsIF(arr):
    # this function fix issues of if statements apperaing at the end of the program.
    for i in range(len(arr)-1,-1,-1):
        if arr[i].split(' ')[0] == 'if':
            arr[i] = '# ' + arr[i]
            continue
        break
    return arr