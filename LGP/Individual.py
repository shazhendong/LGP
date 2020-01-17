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
            and the aviliable operators (arr_operators in {'add','sub','mul','div','and','or','not'}).
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
        for x in range(len):
            print(self.generate_one_operation())


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

    def toString(self):
        print(self.arr_registers_output)
        print(self.arr_registers_arithmatic)
        print(self.arr_registers_var)
        return 'ok'

    