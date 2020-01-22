from Individual import individual
import Individual
import Mutations

creator = individual(['O_0', 'O_1'], ['A_0','A_1'],['V_0','V_1'],['add','sub','mul','div','and','or','not','if'])
p = creator.generate_program(4)
print(Individual.printProgram(p))

print('----------')
p = Mutations.onePoint_mutation(p, creator)

print(Individual.printProgram(p))



