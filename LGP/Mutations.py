# This file implemented mutations
import random


def onePoint_mutation(arr_program, creator):
    loc = random.randint(0,len(arr_program)-1)
    print(loc)
    newInstruction = creator.generate_one_operation()
    arr_program[loc] = newInstruction
    return arr_program